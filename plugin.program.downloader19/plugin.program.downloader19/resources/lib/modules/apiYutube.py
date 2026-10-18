
import sys, json, xbmc, xbmcplugin
import xml.etree.ElementTree as ET
from xbmc import log
from urllib.request import urlopen
from urllib.request import Request
from updatervar import *
from resources.lib.modules.utils import addDir

def ApiMenu():
	req = Request(api_youtube, headers = headers)
	response = urlopen(req).read()
	try:
		apis = json.loads(response)['apis']
		for build in apis:
			name = (build.get('name', ''))
			url = (build.get('url', ''))
			icon = (build.get('icon', addon_icon))
			fanart = (build.get('fanart', addon_fanart))
			description = (build.get('description', 'No Description Available.'))
			if url.endswith('.zip'):
				addDir(name,url,3,icon,fanart,description,name2=name,isFolder=False)
			else:
				addDir('Invalid build URL. Please contact the build creator.','','','','','',isFolder=False)
	except:
		apis = ET.fromstring(response)
		for build in apis.findall('build'):
			try:
				name = build.get('name')
			except:
				name = ''
			try:
				url = build.find('url').text
			except:
				url = ''
			try:
				icon = build.find('icon').text
			except:
				icon = addon_icon
			try:
				fanart = build.find('fanart').text
			except:
				fanart = addon_fanart
			try:
				description = build.find('description').text
			except:
				description = 'No Description Available.'
			if url.endswith('.zip'):
				addDir(name,url,3,icon,fanart,description,name2=name,isFolder=False)
			else:
				addDir('Invalid build URL. Please contact the build creator.','','','','','',isFolder=False)
	xbmcplugin.endOfDirectory(int(sys.argv[1]))