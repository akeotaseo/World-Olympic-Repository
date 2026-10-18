# -*- coding: utf-8 -*-
import sys, xbmc, xbmcgui, xbmcplugin
from inspect import getframeinfo, stack
from urllib.parse import quote_plus, unquote_plus
from updatervar import setting_true,addon_name,addon_version


def addDir(name,url,mode,iconimage,fanart,description, name2='', version='', addcontext=False,isFolder=True):
	u=sys.argv[0]+"?url="+quote_plus(url)+"&mode="+str(mode)+"&name="+quote_plus(name)+"&icon="+quote_plus(iconimage) +"&fanart="+quote_plus(fanart)+"&description="+quote_plus(description)+"&name2="+quote_plus(name2)+"&version="+quote_plus(version)
	ok=True
	liz=xbmcgui.ListItem(name)
	liz.setArt({'fanart':fanart,'icon':'DefaultFolder.png','thumb':iconimage})
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description,})
	if addcontext:
		contextMenu = []
		liz.addContextMenuItems(contextMenu)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)

def play_video(name, url, icon, description):
	xbmcplugin.setPluginCategory(int(sys.argv[1]), name)
	url = unquote_plus(url)
	if url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png'):
		string = "ShowPicture(%s)" %url
		xbmc.executebuiltin(string)
		return
	liz = xbmcgui.ListItem(name)
	liz.setInfo('video', {'title': name, 'plot': description})
	liz.setArt({'thumb': icon, 'icon': icon})
	xbmc.Player().play(url, liz)

def Log(msg,msgtype):
	logit =False
	if msgtype =='debug' and setting_true('logging.debug'):
		logit = True
	elif msgtype == 'action' and setting_true('logging.actions'):
		logit = True
	elif msgtype == 'info' and setting_true('logging.info'):
		logit = True
	else:
		return
	if logit:
		fileinfo = getframeinfo(stack()[1][0])
		xbmc.log('*__{}__{}*{} Python file name = {} Line Number = {}'.format(addon_name,addon_version,msg,fileinfo.filename,fileinfo.lineno), level=xbmc.LOGINFO)
	else:pass