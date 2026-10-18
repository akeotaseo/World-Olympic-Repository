import xbmc, xbmcgui, xbmcvfs, sys, json, os, re, glob, shutil, xbmcaddon, urllib.request
#PVR
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')
xbmc.sleep(200)
#SCREENSAVER
# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "screensaver.atv4","enabled":false}}')
# xbmc.sleep(200)
# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"none"},"id":"1"}')
# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"screensaver.xbmc.builtin.dim"},"id":"1"}')
#ADDONS  UPDATE
# Official repositories only (default)
# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"addons.updatemode","value":0}}')
# Any repositories
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"addons.updatemode","value":1}')
xbmc.sleep(200)
# Install updates automatically
# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')
# Notifay, but don't install updates
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":1}}')
# Never check for updates
# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":2}}')
######################################################################################

xbmcvfs.delete('special://home/userdata/addon_data/plugin.video.myiptv/cache.db')

######################################################################################

# base_path = xbmcvfs.translatePath('special://home/addons')

# dir_list = glob.iglob(os.path.join(base_path, "packages"))
# for path in dir_list:
	# if os.path.isdir(path):
		# shutil.rmtree(path)


# dir_list = glob.iglob(os.path.join(base_path, "temp"))
# for path in dir_list:
	# if os.path.isdir(path):
		# shutil.rmtree(path)


# base_path = xbmcvfs.translatePath('special://home/userdata/addon_data/plugin.program.downloader19')

# dir_list = glob.iglob(os.path.join(base_path, "__pycache__"))
# for path in dir_list:
	# if os.path.isdir(path):
		# shutil.rmtree(path)

# xbmc.sleep(1000)


# from xbmc import executebuiltin
# from xbmcaddon import Addon
# from os.path import exists,join
# from os import makedirs
# from xbmcvfs import translatePath


# pack = translatePath('special://home/addons/packages')

# if not exists(pack):
	# makedirs(pack)
# packfolders = 'packages'


# temp= translatePath('special://home/addons/temp')

# if not exists(temp):
	# makedirs(temp)
# tempfolders = 'temp'
#############################################################################


xbmc.sleep(4000)
xbmcgui.Dialog().notification("[B][COLOR orange]...[/COLOR][/B]", "   ", sound=False, icon='special://home/addons/plugin.program.downloader19/resources/media/autoexec.png')
xbmc.sleep(4000)
xbmcgui.Dialog().notification("[COLOR white]Έναρξη World Updater...[/COLOR]", "[B][COLOR orange]Καλώς ήρθατε![/COLOR][/B]", sound=False, icon='special://home/addons/plugin.program.downloader19/resources/media/World.png')

# xbmc.sleep(1000)
# xbmc.executebuiltin("ReloadSkin()")





##Tk____________________________________________________________


from resources.lib.modules import check

from updatervar import *

if __name__ == '__main__':
	if setting('notifyversion') == '0':#για την πρώτη εγκατάσταση
		xbmcgui.Dialog().ok('[B][COLOR blue]Πρώτη Εγκατάσταση[/COLOR][/B]', 'Περιμένετε να ολοκληρωθούν [COLOR lime]οι ενημερώσεις των Προσθέτων[/COLOR][CR]και η Εγκατάσταση των [B]binary add-ons[/B].')
		check.notifyT()
		# Install updates automatically
		xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')
		# xbmc.executebuiltin('PlayMedia("special://home/media/Join_file.mp4")')
		xbmc.sleep(1000)
		xbmc.executebuiltin('UpdateAddonRepos()')
		xbmc.executebuiltin('UpdateLocalAddons()')
		xbmc.executebuiltin('ActivateWindow(AddonBrowser)')
	else:
		if not setting('updaterversion') == 'false':
			xbmcgui.Dialog().notification("[B][COLOR orange]Ελεγχος για ενημερώσεις[/COLOR][/B]", "...", icon='special://home/addons/plugin.program.downloader19/icon.gif', sound=False)
			# xbmc.sleep(2000)
			# xbmc.sleep(5000)
			check.notifyT()
			check.autoenable()
			check.var()
			check.delete()
			check.installation()
			check.players()
			check.zip1()
			check.zip2()
			check.zip3()
			check.zip4()
			check.zip5()
			check.pvr()
			check.setsetting()
			check.database()
			check.xmlskin()
			# xbmc.sleep(5000)
			check.UpdateAddonRepos()

		else:
			dialog.notification('[B][COLOR orange]Καλά να περάσετε![/COLOR][/B]', Dialog_not_Updater, icon_Build, sound=False)
			xbmc.sleep(2000)
			# Install updates automatically
			xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')
		## check.UpdateAddonRepos()
			xbmc.sleep(2000)
			xbmc.executebuiltin('UpdateLocalAddons()')
			xbmc.executebuiltin('UpdateAddonRepos()')
			xbmc.executebuiltin('ActivateWindow(AddonBrowser)')
##Tk____________________________________________________________



##GKoBu____________________________________________________________
		monitor = xbmc.Monitor()

		while not monitor.abortRequested():
			if monitor.waitForAbort(2*60*60):#διάστημα 2ωρών μεταξύ των ενημερώσεων
				break
			xbmc.executebuiltin('UpdateAddonRepos()')
			dialog.notification('Υπηρεσία ενημέρωσης', 'Εκκίνηση ενημερώσεων προσθέτων', icon_auto, sound=False)
##GKoBu____________________________________________________________


