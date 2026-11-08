import xbmc, xbmcgui, xbmcvfs, sys, json, os, re, glob, shutil, xbmcaddon, urllib.request

# 🛑 ΤΟ ΑΚΑΡΙΑΙΟ ΜΠΛΟΚΑΡΙΣΜΑ (ΠΑΝΩ-ΠΑΝΩ):
if xbmc.getCondVisibility('Window.IsActive(10040)') or xbmc.getCondVisibility('Window.IsActive(2139)') or xbmc.getCondVisibility('Window.IsActive(progressdialog)') or xbmc.getCondVisibility('Window.IsActive(notification)'):
	xbmc.log("[World_Updater] Εντοπίστηκε ανοιχτό παράθυρο ή ειδοποίηση στην εκκίνηση. Ακαριαίο μπλοκάρισμα.", xbmc.LOGINFO)
	xbmc.executebuiltin('ActivateWindow(10040,"addons://outdated/")')
	sys.exit()

# 🛡️ THE GLOBAL DYNAMIC BOOT SHIELD (Μία φορά το initialization του Monitor)
monitor = xbmc.Monitor()
boot_timeout = 30
elapsed_time = 0

while not xbmc.getCondVisibility('Window.IsVisible(home)') and elapsed_time < boot_timeout and not monitor.abortRequested():
	xbmc.sleep(500)
	elapsed_time += 0.5

xbmc.log(f"[World_Updater] Η αρχική οθόνη φορτώθηκε σε {elapsed_time}s. Έναρξη Updater...", xbmc.LOGINFO)

# 🟢 [ΔΙΚΛΕΙΔΑ ΑΣΦΑΛΕΙΑΣ] - Από εδώ και κάτω συνεχίζει ο αυθεντικός σου κώδικας 100% απαράλλακτος
profile_dir = xbmcvfs.translatePath('special://home/userdata/addon_data/plugin.program.downloader19')
addons_dir = xbmcvfs.translatePath('special://home/addons/plugin.program.downloader19')

lock_files = ['delete_lock.txt', 'database_lock.txt', 'install_lock.txt']
for lock_name in lock_files:
	full_lock_path = os.path.join(profile_dir, lock_name)
	if os.path.exists(full_lock_path):
		try:
			os.remove(full_lock_path)
			xbmc.log(f"[World_Updater] [Δικλείδα Ασφαλείας] Το παλιό αρχείο {lock_name} σβήστηκε.", xbmc.LOGINFO)
		except:
			pass

old_trigger = os.path.join(addons_dir, 'build_update_trigger.txt')
if os.path.exists(old_trigger):
	try: os.remove(old_trigger)
	except: pass

def disable_screensaver():
	""" 🔒 ΑΠΕΝΕΡΓΟΠΟΙΗΣΗ SCREENSAVER """
	try:
		if not os.path.exists(profile_dir):
			os.makedirs(profile_dir)

		backup_file = os.path.join(profile_dir, 'screensaver_backup.txt')
		req_get = '{"jsonrpc":"2.0","method":"Settings.GetSettingValue","params":{"setting":"screensaver.mode"},"id":1}'
		res_get = json.loads(xbmc.executeJSONRPC(req_get))
		current_ss = res_get['result']['value']
		
		if not os.path.exists(backup_file):
			with open(backup_file, 'w', encoding='utf-8') as f:
				f.write(current_ss)
				
		xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":""},"id":1}')
		xbmc.log(f"[World_Updater] Ο screensaver απενεργοποιήθηκε. Backup: {current_ss}", xbmc.LOGINFO)
	except Exception as e:
		xbmc.log(f"[World_Updater] Αποτυχία διαχείρισης screensaver: {str(e)}", xbmc.LOGERROR)

disable_screensaver()

# 🚀 BATCH JSON-RPC CALLS (Όλα σε ένα string για ταχύτητα)
json_commands = [
	'{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.stalker","enabled":false},"id":1}',
	'{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":false},"id":1}',
	'{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"addons.updatemode","value":1},"id":1}',
	'{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"general.addonupdates","value":1},"id":1}'
]
for cmd in json_commands:
	xbmc.executeJSONRPC(cmd)

xbmc.sleep(200) 
xbmcgui.Dialog().notification("[B][COLOR orange]...[/COLOR][/B]", "   ", sound=False, icon='special://home/addons/plugin.program.downloader19/resources/media/autoexec.png')
xbmc.sleep(1000) 
xbmcgui.Dialog().notification("[COLOR white]Έναρξη World Updater...[/COLOR]", "[B][COLOR orange]Καλώς ήρθατε![/COLOR][/B]", sound=False, icon='special://home/addons/plugin.program.downloader19/resources/media/World.png')

from resources.lib.modules import check
from updatervar import *

if __name__ == '__main__':
	if setting('notifyversion') == '0':
		xbmcgui.Dialog().ok('[B][COLOR blue]Πρώτη Εγκατάσταση[/COLOR][/B]', 'Περιμένετε να ολοκληρωθούν [COLOR lime]οι ενημερώσεις των Προσθέτων[/COLOR][CR]και η Εγκατάσταση των [B]binary add-ons[/B].')
		check.notifyT()
		xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"general.addonupdates","value":0},"id":1}')
		xbmc.sleep(500)
		xbmc.executebuiltin('UpdateAddonRepos()')
		xbmc.executebuiltin('UpdateLocalAddons()')
		xbmc.executebuiltin('ActivateWindow(AddonBrowser)')
	else:
		check.zip1()
		external_script = xbmcvfs.translatePath('special://home/addons/plugin.program.downloader19/check_build_updates.py')
		update_trigger = xbmcvfs.translatePath('special://home/addons/plugin.program.downloader19/build_update_trigger.txt')
		
		if os.path.exists(update_trigger):
			xbmc.log("[World_Updater] Η σημαία build_update_trigger.txt ανιχνεύτηκε!", xbmc.LOGINFO)
			try: os.remove(update_trigger)
			except: pass
			
			xbmcgui.Dialog().notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False)
			
			file_timeout = 8.0
			file_elapsed = 0.0
			while not os.path.exists(external_script) and file_elapsed < file_timeout and not monitor.abortRequested():
				xbmc.sleep(200)
				file_elapsed += 0.2
			
			if os.path.exists(external_script):
				xbmc.sleep(500)
				xbmc.log(f"[World_Updater] Το check_build_updates.py εκτελείται...", xbmc.LOGINFO)
				xbmc.executebuiltin(f'RunScript("{external_script}")')
			else:
				xbmc.log("[World_Updater] Κρίσιμο Σφάλμα: Timeout αρχείου.", xbmc.LOGERROR)

		elif not setting('updaterversion') == 'false':
			xbmc.log("[World_Updater] Έναρξη καθημερινού ελέγχου...", xbmc.LOGINFO)
			check.UpdateAddonRepos()
		else:
			xbmc.log("[World_Updater] Αυτόματες ενημερώσεις απενεργοποιημένες.", xbmc.LOGINFO)
			xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"general.addonupdates","value":0},"id":1}')
			xbmc.sleep(200)
			xbmc.executebuiltin('UpdateLocalAddons()')
			xbmc.executebuiltin('UpdateAddonRepos()')

	# 🔄 ΟΜΑΔΟΠΟΙΗΜΕΝΟ TRACKER LOOP (ΠΟΥΠΟΥΛΟ)
	update_interval = 2 * 60 * 60  
	time_counter = 0

	skin_strings_to_reset = [
		'HubFromWidget', 'TrailerCheckID', 'HubMovieTitle', 'HubMoviePlot', 
		'HubMovieCast', 'HubMovieDirector', 'HubMovieWriter', 'HubMovieGenre', 
		'HubMovieYear', 'HubMovieRating', 'HubMovieStudio', 'HubMovieCountry', 
		'HubMoviePoster', 'HubMovieFanart', 'HubMovieTagLine', 'HubMovieDuration', 'HubMovieEndTime'
	]

	while not monitor.abortRequested():
		if monitor.waitForAbort(1.0):
			break

		if xbmc.getCondVisibility('Window.IsVisible(home)') and not xbmc.getCondVisibility('Window.IsVisible(6199)'):
			if xbmc.getInfoLabel('Skin.String(TrailerCheckID)') != '':
				for skin_str in skin_strings_to_reset:
					xbmc.executebuiltin(f'Skin.ResetString({skin_str})')

		time_counter += 1 
		if time_counter >= update_interval:
			time_counter = 0 
			xbmc.executebuiltin('UpdateAddonRepos()')
