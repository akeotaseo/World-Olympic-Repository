# -*- coding: utf-8 -*-
import xbmc, xbmcgui, sys
from resources.lib.modules import check
from updatervar import *

if not setting('updaterversion') == 'false':

	xbmcgui.Dialog().notification("[B][COLOR orange]Ελεγχος για ενημερώσεις[/COLOR][/B]", "...", icon='special://home/addons/plugin.program.downloader19/icon.gif', sound=False)
	check.notifyT()
	check.autoenable()
	check.var()
	check.delete()
	check.installation()
	check.zip2() 
	check.players()
	check.zip3()
	check.zip4()
	check.zip5()
	check.pvr()
	check.setsetting()
	check.database()
	
	from resources.lib.modules.check import wait_for_kodi
	wait_for_kodi("Ενημέρωση Αποθετηρίων Database")

	# 1. Έλεγχος μενού skin (Καθαρό αυθεντικό κάλεσμα, χωρίς διακοπή της ροής)
	check.xmlskin() 
		
	# 🚀 Η ροή συνεχίζει κανονικά και εκτελεί το τελικό φρεσκάρισμα των αποθετηρίων
	check.UpdateAddonRepos()

else:
	xbmcgui.Dialog().notification('[B][COLOR orange]Καλά να περάσετε![/COLOR][/B]', Dialog_not_Updater, icon_Build, sound=False)
	xbmc.sleep(2000)
	xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"general.addonupdates","value":0}}')
	xbmc.sleep(2000)
	xbmc.executebuiltin('UpdateLocalAddons()')
	xbmc.executebuiltin('UpdateAddonRepos()')
	xbmc.executebuiltin('ActivateWindow(AddonBrowser)')
