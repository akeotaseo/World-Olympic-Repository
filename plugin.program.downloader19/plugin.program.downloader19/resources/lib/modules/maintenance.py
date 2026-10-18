import os, shutil, sqlite3
import xbmc, xbmcgui
from xbmc import log
from updatervar import *

def purge_db(db):
	if os.path.exists(db):
		try:
			conn = sqlite3.connect(db)
			cur = conn.cursor()
		except Exception as e:
			log("DB Connection Error: %s" % str(e), xbmc.LOGDEBUG)
			return False
	else: 
		log('%s not found.' % db, xbmc.LOGINFO)
		return False
	cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
	for table in cur.fetchall():
		if table[0] == 'version': 
			log('Data from table `%s` skipped.' % table[0], xbmc.LOGDEBUG)
		else:
			try:
				cur.execute("DELETE FROM %s" % table[0])
				conn.commit()
				log('Data from table `%s` cleared.' % table[0], xbmc.LOGDEBUG)
			except Exception as e:
				log("DB Remove Table `%s` Error: %s" % (table[0], str(e)), xbmc.LOGERROR)
	conn.close()
	log('%s DB Purging Complete.' % db, xbmc.LOGINFO)

def clear_packages():
	file_count = len([name for name in os.listdir(packages)])
	for filename in os.listdir(packages):
		file_path = os.path.join(packages, filename)
		try:
			   if os.path.isfile(file_path) or os.path.islink(file_path):
			   	os.unlink(file_path)
			   elif os.path.isdir(file_path):
			   	shutil.rmtree(file_path)
		except Exception as e:
			log('Failed to delete %s. Reason: %s' % (file_path, e), xbmc.LOGINFO)
	xbmc.sleep(1000)
	xbmcgui.Dialog().ok(addon_name, str(file_count)+' packages cleared.' )
	return

def clear_thumbnails():
	try:
		if os.path.exists(os.path.join(user_path, 'Thumbnails')):
			shutil.rmtree(os.path.join(user_path, 'Thumbnails'))
	except Exception as e:
			log('Failed to delete %s. Reason: %s' % (os.path.join(user_path, 'Thumbnails'), e), xbmc.LOGINFO)
			return
	try:
		if os.path.exists(os.path.join(db_path, 'Textures13.db')):
			os.unlink(os.path.join(db_path, 'Textures13.db'))
	except:
		purge_db(textures_db)
	xbmc.sleep(1000)
	xbmcgui.Dialog().ok(addon_name, 'Thumbnails have been deleted. Reboot Kodi to refresh thumbs.')
	return

def advanced_settings():
    selection = xbmcgui.Dialog().select('[COLOR orange]Επιλέξτε το μέγεθος Ram της συσκευής σας[/COLOR]',
                                       ['[COLOR orange] ==> [COLOR lime]50MB[/COLOR]',
                                        '[COLOR orange]1GB[COLOR white] RAM ==> [COLOR lime]70MB[/COLOR]',
                                        '[COLOR orange]1GB[COLOR white] έως [COLOR orange]1.5GB[COLOR white] RAM ==> [COLOR lime]90MB[/COLOR]',
                                        '[COLOR orange]1.5GB[COLOR white] έως [COLOR orange]2GB[COLOR white] RAM ==> [COLOR lime]110MB[/COLOR]',
                                        '[COLOR orange]2GB[COLOR white] έως [COLOR orange]3GB[COLOR white] RAM ==> [COLOR lime]120MB[/COLOR]',
                                        '[COLOR orange]3GB[COLOR white] και πάνω RAM ==> [COLOR lime]130MB[/COLOR]',
                                        '[COLOR orange] ==> [COLOR lime]150MB[/COLOR]',
                                        '[COLOR orange] ==> [COLOR lime]160MB[/COLOR]',
                                        '[COLOR orange] ==> [COLOR lime]180MB[/COLOR]',
                                        '[B][COLOR red]Διαγραφή [COLOR grey]αποθηκευμένου xml - [COLOR orange]Advanced Settings[/COLOR][/B]'])
    if selection==0:
        xml = os.path.join(advancedsettings_folder, '50.xml')
    elif selection==1:
        xml = os.path.join(advancedsettings_folder, '70.xml')
    elif selection==2:
        xml = os.path.join(advancedsettings_folder, '90.xml')
    elif selection==3:
        xml = os.path.join(advancedsettings_folder, '110.xml')
    elif selection==4:
        xml = os.path.join(advancedsettings_folder, '120.xml')
    elif selection==5:
        xml = os.path.join(advancedsettings_folder,'130.xml')
    elif selection==6:
        xml = os.path.join(advancedsettings_folder,'150.xml')
    elif selection==7:
        xml = os.path.join(advancedsettings_folder,'160.xml')
    elif selection==8:
        xml = os.path.join(advancedsettings_folder,'180.xml')
    elif selection==9:
        if os.path.exists(advancedsettings_xml):
            os.unlink(advancedsettings_xml)
        xbmc.sleep(1000)
#        deleted = xbmcgui.Dialog().ok(addon_name, 'Διαγράφηκαν οι απαραίτητες ρυθμίσεις.[CR]Το Kodi θα κλείσει τώρα για να εφαρμόσει τις ρυθμίσεις.')
        yes_enable = dialog.yesno(addon_name, '[B][COLOR lime]Το advancedsettings.xml διαγράφηκε με επιτυχία![/COLOR][CR][CR]Επιθυμείτε να κλείσει το kodi για να αποθηκευτούν οι αλλαγές τώρα?[/B]', nolabel='[B][COLOR orange]Οχι[/COLOR][/B]',yeslabel='[B][COLOR lime]Ναι[/COLOR][/B]')
        if yes_enable:
            os._exit(1)
        else:
            return
    else:
        return
    if os.path.exists(advancedsettings_xml):
        os.unlink(advancedsettings_xml)
    shutil.copyfile(xml, advancedsettings_xml)
    xbmc.sleep(1000)
#    apply = xbmcgui.Dialog().ok(addon_name, 'Έχουν οριστεί οι απαραίτητες ρυθμίσεις.[CR]Το Kodi θα κλείσει τώρα για να εφαρμόσει τις ρυθμίσεις.')
    yes_enable = dialog.yesno(addon_name, '[B][COLOR lime]Έχουν οριστεί οι απαραίτητες ρυθμίσεις![/COLOR][CR][CR]Επιθυμείτε να κλείσει το kodi για να αποθηκευτούν οι αλλαγές τώρα?[/B]', nolabel='[B][COLOR orange]Οχι[/COLOR][/B]',yeslabel='[B][COLOR lime]Ναι[/COLOR][/B]')
    if yes_enable:
        os._exit(1)
    else:
        return