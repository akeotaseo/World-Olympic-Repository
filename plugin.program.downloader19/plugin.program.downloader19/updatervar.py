import os, sys, glob, base64, xbmc, xbmcvfs, xbmcaddon, xbmcgui, shutil
from datetime import datetime
from urllib.parse import parse_qs
from urllib.request import Request, urlopen

addon_id        = 'plugin.program.downloader19'
addon           = xbmcaddon.Addon(addon_id)
addoninfo       = addon.getAddonInfo
addon_version   = addoninfo('version')
addon_name      = addoninfo('name')
addon_icon      = addoninfo("icon")
addon_fanart    = addoninfo("fanart")
translatePath   = xbmcvfs.translatePath
addon_profile   = translatePath(addoninfo('profile'))
addon_path      = translatePath(addoninfo('path'))
setting         = addon.getSetting
setting_true    = lambda x: bool(True if setting(str(x)) == "true" else False)
setting_set     = addon.setSetting
local_string    = addon.getLocalizedString
home            = translatePath('special://home/')#     home + 'cache'
dialog          = xbmcgui.Dialog()
dp              = xbmcgui.DialogProgress()
BG              = xbmcgui.DialogProgressBG()
xbmcPath        = os.path.abspath(home)
addons_path     = os.path.join(home, 'addons/')
user_path       = os.path.join(home, 'userdata/')#      user_path + 'profiles.xml'
data_path       = os.path.join(user_path, 'addon_data/')
db_path         = os.path.join(user_path, 'Database/')
addons_db       = os.path.join(db_path,'Addons33.db')
textures_db     = os.path.join(db_path,'Textures13.db')
packages        = os.path.join(addons_path, 'packages/')
resources       = os.path.join(addon_path, 'resources/')
#UpdaterMatrix   = os.path.join(user_path, 'UpdaterMatrix/')
Downloader      = os.path.join(data_path, 'plugin.program.downloader19/')
UpdaterMatrix   = os.path.join(Downloader, 'UpdaterMatrix/')


installed_date  = str(datetime.now())[:-7]
EXCLUDES        = [addon_id, 'packages', 'Addons33.db', 'kodi.log']
user_agent      = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
headers         = {'User-Agent': user_agent}
exists          = os.path.exists
yes_label       = '[COLOR lime]Ναι[/COLOR]'
no_label        = '[COLOR orange]Όχι[/COLOR]'
Background_path = 'Skin.SetImage(CustomDefaultBackground.path,special://home/addons/skin.TechNEWSology/backgrounds/)'
icon            = 'special://home/addons/plugin.program.downloader19/icon.gif'
icon_YouTube    = 'special://home/addons/plugin.program.downloader19/resources/media/youtube.png'
icon_Build      = 'special://home/addons/plugin.program.downloader19/resources/media/World.png'
icon_clean      = 'special://home/addons/plugin.program.downloader19/resources/media/clean.png'
icon_save    = 'special://home/addons/plugin.program.downloader19/resources/media/save.png'
icon_backup  = 'special://home/addons/plugin.program.downloader19/resources/media/backup.png'
icon_restore    = 'special://home/addons/plugin.program.downloader19/resources/media/restore.png'
icon_b1    = 'special://home/addons/plugin.program.downloader19/resources/media/b1.png'
icon_b2    = 'special://home/addons/plugin.program.downloader19/resources/media/b2.png'
icon_Speedtest    = 'special://home/addons/plugin.program.downloader19/resources/media/Speedtest.png'
icon_Log  = 'special://home/addons/plugin.program.downloader19/resources/media/Log.png'
icon_Settings   = 'special://home/addons/plugin.program.downloader19/resources/media/Settings.png'
icon_Settings_t = 'special://home/addons/plugin.program.downloader19/resources/media/Settings_t.png'
icon_Notify     = 'special://home/addons/plugin.program.downloader19/resources/media/Notify.png'
icon_Check      = 'special://home/addons/plugin.program.downloader19/resources/media/Check.png'
icon_update      = 'special://home/addons/plugin.program.downloader19/resources/media/update.png'
icon_enable      = 'special://home/addons/plugin.program.downloader19/resources/media/enable.png'
icon_reloadprofile      = 'special://home/addons/plugin.program.downloader19/resources/media/reloadprofile.png'
icon_rp      = 'special://home/addons/plugin.program.downloader19/resources/media/rp.png'
icon_realdebrid      = 'special://home/addons/plugin.program.downloader19/resources/media/realdebrid.png'
icon_Settings_1 = 'special://home/addons/plugin.program.downloader19/resources/media/Settings_1.png'
icon_ok         = 'special://home/addons/plugin.program.downloader19/resources/media/ok.gif'
icon_ok2         = 'special://home/addons/plugin.program.downloader19/resources/media/ok2.png'
icon_delete         = 'special://home/addons/plugin.program.downloader19/resources/media/delete.png'
icon_tools         = 'special://home/addons/plugin.program.downloader19/resources/media/tools .png'
icon_m         = 'special://home/addons/plugin.program.downloader19/resources/media/m.png'
icon_install         = 'special://home/addons/plugin.program.downloader19/resources/media/install.png'
icon_Skinshortcuts        = 'special://home/addons/plugin.program.downloader19/resources/media/skinshortcuts.png'
icon_auto         = 'special://home/addons/plugin.program.downloader19/resources/media/auto.png'
icon_auto2         = 'special://home/addons/plugin.program.downloader19/resources/media/auto2.png'
icon_auto3         = 'special://home/addons/plugin.program.downloader19/resources/media/auto3.png'
icon_hi         = 'special://home/addons/plugin.program.downloader19/resources/media/hi.gif'

icon_Pleasewait         = 'special://home/addons/plugin.program.downloader19/resources/media/Pleasewait.png'

addon_data_youtube        = translatePath('special://home/userdata/addon_data/plugin.video.youtube')
advancedsettings_xml      =  os.path.join(user_path, 'advancedsettings.xml')
advancedsettings_folder   = os.path.join(resources, 'advancedsettings/')
addon_data_skinshortcuts  = translatePath('special://home/userdata/addon_data/script.skinshortcuts')
addons_data_path          = [translatePath('special://home/addons'), translatePath('special://home/userdata/addon_data')]
Dialog_TechNEWSology      = '[B][COLOR orange]World[/COLOR][/B]'
Dialog_welcome            = '[B][COLOR orange]Καλώς ήρθατε![/COLOR][/B]'
Dialog_Update             = '[COLOR white]Έναρξη World Updater...[/COLOR]'
Dialog_enable_on          = '[COLOR white]Επιλέξατε την ενεργοποίηση όλων των πρόσθετων[/COLOR]'
Dialog_enable             = '[COLOR lime]Τα πρόσθετα έχουν ενεργοποιηθεί![/COLOR]'
Dialog_not_Updater        = '[B]Οι αυτόματες ενημερώσεις είναι απενερ/μένες[/B]'
Dialog_Update_AddonsRepos = 'Αλλαγή αποθετηρίων σε πρόσθετα'
Dialog_LoadProfile        = '[COLOR white]Πατώντας [COLOR lime]Ναι[COLOR white], οι αλλαγές θα πραγματοποιηθούν τώρα[CR](η εικόνα θα παγώσει για λίγα δευτερόλεπτα μέχρι να γίνει επαναφόρτωση του προφίλ).[CR]Πατώντας [COLOR orange]Όχι[COLOR white], οι αλλαγές θα πραγματοποιηθούν στην επόμενη εκκίνηση του Build.[/COLOR]'
Dialog_Xml_Skin           = 'Προσθήκες-Διορθώσεις στα xml του skin ...'
Dialog_Players            = 'Διόρθωση των players TheMovieDb Helper...'
Dialog_ReloadSkin         = 'Θα πραγματοποιηθεί επανεκκίνηση κελύφους'
Dialog_Database           = 'Νέες καταχωρίσεις στην Database...'
Dialog_U1                 = '[B]Αναμονή για ολοκλήρωση ενημέρωσης[/B]'
Dialog_U2                 = 'Περιμένετε χωρίς να πατήσετε κάτι...'
Dialog_U3                 = 'Εισαγωγή στοιχείων...'
Dialog_U4                 = '[B]Ολοκληρώθηκε με επιτυχία[/B]'
Dialog_U5                 = 'To Build είναι ενημερωμένο!'
Dialog_U6                 = 'Έλεγχος για νέες αναβαθμίσεις...'
Dialog_U7                 = '[B][COLOR orange]World[/COLOR][/B]'
Dialog_U8                 = '[B]Έναρξη ενημέρωσης[/B]'
Dialog_U9                 = '[B][COLOR lime]Επιτυχής ενημέρωση[/COLOR][/B]'
Dialog_U10                = 'Διαγραφή αρχείων...'
Dialog_U11                = 'Αναζήτηση αχρείαστων αρχείων...'
Dialog_U12                = '[B]Διαδικασία ενημέρωσης[/B]'


headers_TXT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'}


del_startup               = 'RunScript(special://home/userdata/addon_data/plugin.program.downloader19/delete_files.py)'
install_startup           = 'RunScript(special://home/userdata/addon_data/plugin.program.downloader19/addons_list_installation.py)'
database_startup          = 'RunScript(special://home/userdata/addon_data/plugin.program.downloader19/Database_Addons33.py)'
set_setting_startup       = 'RunScript(special://home/userdata/addon_data/plugin.program.downloader19/set_setting.py)'

tempfile_1  = os.path.join(packages, 'tempfile.zip')
tempfile_2  = os.path.join(packages, 'tempfile_2.zip')
tempfile_3  = os.path.join(packages, 'tempfile_3.zip')
tempfile_4  = os.path.join(packages, 'tempfile_4.zip')
tempfile_5  = os.path.join(packages, 'tempfile_5.zip')
tempfile_6  = os.path.join(packages, 'tempfile_6.zip')
tempfile_7  = os.path.join(packages, 'tempfile_7.zip')
tempfile_8  = os.path.join(packages, 'tempfile_8.zip')
tempfile_9  = os.path.join(packages, 'tempfile_9.zip')
tempfile_10 = os.path.join(packages, 'tempfile_10.zip')
tempfile_11 = os.path.join(packages, 'tempfile_11.zip')
tempfile_12 = os.path.join(packages, 'tempfile_12.zip')
tempfile_13 = os.path.join(packages, 'tempfile_13.zip')
tempfile_14 = os.path.join(packages, 'tempfile_14.zip')
tempfile_15 = os.path.join(packages, 'tempfile_15.zip')



bzipfile = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/Build.txt'
api_youtube = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/Youtube.txt'
notify_url = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/notify.txt'

#notify_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/notify_updater.txt'
#skinshortcuts_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/skinshortcuts_updater.txt'
addonsrepos_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/addonsrepos_updater.txt'
xmlskin_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/xmlskin_updater.txt'
players_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/players_updater.txt'

setting_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/setsetting_updater.txt'
installation_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/addonslistinstallation_updater.txt'
deletefiles_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/deletefiles_updater.txt'
var_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/var_updater.txt'

zip1_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/zip1_updater.txt'
zip2_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/zip2_updater.txt'
zip3_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/zip3_updater.txt'
zip4_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/zip4_updater.txt'
zip5_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/zip5_updater.txt'

pvr_url_updater = 'https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XML/pvr_updater.txt'


#Updater_startup = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Updater_startup.zip&mode=9&name=Εισαγωγή downloader_startup)'
#skinshortcuts_menu = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/skinshortcuts_menu.zip&mode=9&name=Ενημέρωση στο μενού του Skin)'
AddonsRepos_startup  = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/AddonsRepos_startup.zip&mode=9&name=Αλλαγή αποθετηρίων σε πρόσθετα)'
XmlSkin_startup      = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/XmlSkin_startup.zip&mode=9&name==Διορθώσεις στο xml του skin)'
Players_startup      = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Players_startup.zip&mode=9&name=Διορθώσεις στους Players)'
SetSetting_startup   = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/SetSetting_startup.zip&mode=9&name=Ρυθμίσεις πρόσθετων)'
Installation_startup = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Installation_startup.zip&mode=9&name=Εγκατάσταση πρόσθετων)'
Delete_startup       = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Delete_startup.zip&mode=9&name=Διαγραφή...)'
Var_startup          = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Var_startup.zip&mode=9&name=...)'
Zip1_startup         = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Zip1_startup.zip&mode=9&name=Διάφορες διορθώσεις)'
Zip2_startup         = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Zip2_startup.zip&mode=9&name=Addons)'
Zip3_startup         = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Zip3_startup.zip&mode=9&name=data)'
Zip4_startup         = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Zip4_startup.zip&mode=9&name=test)'
Zip5_startup         = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Zip5_startup.zip&mode=9&name=test)'
Pvr_startup         = 'RunPlugin(plugin://plugin.program.downloader19/?url=https://github.com/akeotaseo/world_repo/raw/main/Updater_Matrix/Pvr_startup.zip&mode=9&name=test)'




def isBase64(s):
	if base64.b64encode(base64.b64decode(s)).decode('utf8') == s:
		return True
	else:
		return False
