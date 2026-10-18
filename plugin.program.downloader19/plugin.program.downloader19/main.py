# -*- coding: utf-8 -*-

import os, sys, shutil, json, base64, xbmc, xbmcplugin, xbmcaddon, xbmcgui
import xml.etree.ElementTree as ET
from xbmc import log
from updatervar import *
from zipfile import ZipFile
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import unquote_plus
from resources.lib.modules.utils import addDir, play_video
from resources.lib.modules import skinSwitch
from resources.lib.modules.downloader import downloader, downloader_b
from resources.lib.modules.save_data import save_check, save_backup, save_restore, save_menu
from resources.lib.modules.backup_restore import backup_build, restore_menu, restore_build, get_backup_folder, reset_backup_folder
from resources.lib.modules.parser import Parser
from resources.lib.modules import control, cache



args = parse_qs(sys.argv[2][1:])
KODIV  = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
handle = int(sys.argv[1])


def currSkin():
    return xbmc.getSkinDir()
def percentage(part, whole):
    return 100 * float(part)/float(whole)


def MainMenu():
    addDir('Maintenance','',33,icon_Settings_t,addon_fanart,'',isFolder=True)
    addDir('YouTube Api Key','',1,icon_YouTube,addon_fanart,'',isFolder=True)
    addDir('Εγκατάσταση Binary Addons','',16,icon_install,addon_fanart,'',isFolder=False)
    addDir('Εργαλεία World  Build','',14,icon_tools,addon_fanart,'',isFolder=False)
    addDir('Εξουσιοδότηση/Επαναφορά Derbid','',24,icon_realdebrid,addon_fanart,'',isFolder=False)
    addDir('Μήνυμα καταγραφής ενημερώσεων','',100,icon_m,addon_fanart,'Bring up the notifications dialog',isFolder=False)
    addDir('Ρυθμίσεις World  Updater-Tools','',2,icon_Settings_1,addon_fanart,'',isFolder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def subMenu_maintenance():
    addDir('[B][COLOR white]Καθαρισμός Παρόχων[/COLOR][/B]','',23,icon_Build,addon_fanart,'',isFolder=False)
    addDir('[B][COLOR white]Καθαρισμός Packages[/COLOR][/B]','',6,icon_Build,addon_fanart,'',isFolder=False)
    addDir('[B][COLOR white]Καθαρισμός Thumbnails[/COLOR][/B]','',7,icon_Build,addon_fanart,'',isFolder=False)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def main_backup_restore():
    addDir('Αντίγραφο ασφαλείας Build','',18,icon_backup,addon_fanart,'Backup Build', isFolder=False)
    addDir('Επαναφορά Αντιγράφου ασφαλείας','',19, icon_restore,addon_fanart,'Restore Backup')
    addDir('Αλλαγή τοποθεσίας αντιγράφων ασφαλείας','',21,icon_b1,addon_fanart,'Change the location where backups will be stored and accessed.', isFolder=False)
    addDir('Επαναφορά θέσης αντιγράφου ασφαλείας','',22,icon_b2,addon_fanart,'Set the backup location to its default.', isFolder=False)

def main_enable_addons():
    addDir('Ενεργοποιήστε όλα τα πρόσθετα τώρα','',25,icon_enable,addon_fanart,'',isFolder=False)
    addDir('Ενεργοποίηση όλων των πρόσθετων κατά την επόμενη εκκίνηση','',26,icon_Build,addon_fanart,'',isFolder=False)
    addDir('Ακύρωση της επόμενης εκκίνησης','',27,icon_Build,addon_fanart,'',isFolder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def main_maintenance():
    addDir('Advanced Settings','',4,icon_Settings,addon_fanart,'',isFolder=False)
    addDir('Ενεργοποίηση πρόσθετων','',28,icon_enable,addon_fanart,'',isFolder=True)
    addDir('Αντίγραφο ασφαλείας & Επαναφορά Build','',17,icon_save,addon_fanart,'',isFolder=True)
    addDir('Καθαρισμός (Provider-Packages-Thumbnails)','',5,icon_clean,addon_fanart,'',isFolder=True)
    addDir('[COLOR lime]Καθαρή εγκατάσταση Build[/COLOR] [B][COLOR blue]*G.K.N.Wizard*[/COLOR][/B]','',122,icon_Build,addon_fanart,'',isFolder=True)
    addDir('[COLOR red]Απενεργοποίηση[/COLOR] αυτόματων ενημερώσεων του World Build','',29,icon_Build,addon_fanart,'',isFolder=True)
    addDir('[COLOR green]Eνεργοποίηση[/COLOR] αυτόματων ενημερώσεων του World Build','',30,icon_Build,addon_fanart,'',isFolder=True)
    addDir('Speedtest','',31,icon_Speedtest,addon_fanart,'', isFolder=False)
    addDir('View Log','', 32, icon_Log,addon_fanart,'', isFolder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def main_ApiMenu(NAME, NAME2, VERSION, URL, ICON, FANART, DESCRIPTION):
    yes_api = dialog.yesno(NAME, '[COLOR white]Αν το Api Key Youtube έχει υπερβεί το ημερήσιο όριο αναπαραγωγής και δε λειτουργεί, δοκιμάζουμε κάποιο άλλο. Το ημερήσιο όριο αναπαραγωγής ανανεώνεται καθημερινά στις 10:00 π.μ.[CR]Για να μην υπερβαίνετε το ημερήσιο όριο, δημιουργήστε δικό σας API KEY (μια μικρή αναζήτηση στο διαδίκτυο θα σας δείξει τον τρόπο).[/COLOR]', nolabel='Άκυρο', yeslabel='Συνέχεια')
    if yes_api:
        downloader(NAME, NAME2, VERSION, URL)
        dialog.notification("[B][COLOR red]YouTube [COLOR white]Api Key[/COLOR][/B]",'[COLOR white]Επιτυχής καταχώριση κλειδιού![/COLOR]' , icon_YouTube)
    else:
        return


def main_Skinshortcuts(NAME, NAME2, VERSION, URL, ICON, FANART, DESCRIPTION):
    downloader(NAME, NAME2, VERSION, URL)


def main_BuildMenu(NAME, NAME2, VERSION, URL, ICON, FANART, DESCRIPTION):
    yesSave = dialog.yesno('[B][COLOR lime]Εγκατάσταση World Build[/COLOR][/B]', '[COLOR red] ΠΡΟΣΟΧΗ![/COLOR][CR]  Θα πραγματοποιηθεί διαγραφή όλων των αρχείων και[CR]  εκ νέου καθαρή εγκατάσταση του Build από την αρχή![CR][CR] (Ακολουθεί επιλογή διατήρησης στοιχείων κατά την[CR]  νέα εγκατάσταση στη συσκευή μας)', nolabel='[COLOR orange]Ακυρο[/COLOR]', yeslabel='[COLOR lime]Συνέχεια[/COLOR]')
    if yesSave:
        save_menu()
        save_check()
        save_backup()
    else:
        return
    yesInstall = dialog.yesno(NAME, '[COLOR white]Επιθυμείτε να συνεχιστεί η καθαρή εγκατάσταση του Build;[/COLOR]', nolabel='[COLOR orange]Άκυρο[/COLOR]', yeslabel='[COLOR lime]Ναι, επιθυμώ[/COLOR]')
    if yesInstall:
        freshStart()
        downloader_b(NAME, NAME2, VERSION, URL)
        dialog.ok(addon_name, '[COLOR lime]Το Build  εγκαταστάθηκε με επιτυχία ![/COLOR][CR]Στην πρώτη έναρξη δώστε του 5 λεπτά να λάβει τις απαραίτητες ενημερώσεις.[CR]Για τη σωστή λειτουργία των πρόσθετων είναι απαραίτητη η αλλαγή DNS.')
        os._exit(1)
    else:
        return

def main_downloader(NAME, NAME2, VERSION, URL, ICON, FANART, DESCRIPTION):
    downloader(NAME, NAME2, VERSION, URL)

def enable_now():
    yes_enable = dialog.yesno(addon_name, '[B]Θέλετε να ενεργοποιήσετε όλα τα πρόσθετα τώρα;[/B]', nolabel='[B]Ακύρωση[/B]',yeslabel='[B][COLOR lime]Ενεργοποίηση[/COLOR][/B]')
    if yes_enable:
        from resources.lib.modules import addonsEnable
        addonsEnable.enable_addons()
    #    ok = dialog.ok(addon_name, 'Όλα τα πρόσθετα έχουν ενεργοποιηθεί.')
        dialog.notification("[B][COLOR orange]World Build[/COLOR][/B]",'[COLOR white]Τα πρόσθετα [COLOR lime]ενεργοποιήθηκαν[COLOR white] με επιτυχία![/COLOR]' , icon_Build)
    else:
        return
    
def enable_next_start():
    yes_enable = dialog.yesno(addon_name, '[B]Θέλετε να ενεργοποιήσετε όλα τα πρόσθετα στην επόμενη εκκίνηση του Build;[/B]', nolabel='[B]Ακύρωση[/B]',yeslabel='[B][COLOR lime]Ενεργοποίηση[/COLOR][/B]')
    if yes_enable:
        setting_set('autoenable','true')
        dialog.notification("[COLOR white]Η [COLOR lime]Ενεργοποίηση[COLOR white] όλων των πρόσθετων[/COLOR]",'[COLOR white]έχει πλέον οριστεί για την επόμενη εκκίνηση του Build![/COLOR]' , icon_Build)
    #    ok = dialog.ok(addon_name, 'Η ενεργοποίηση όλων των πρόσθετων έχει πλέον οριστεί για την επόμενη εκκίνηση του Build.')
    else:
        return

def disable_downloader_startup():
    yes_enable = dialog.yesno(addon_name, 'Θέλετε να απενεργοποιήσετε τις αυτόματες ενημερώσεις[CR]του World Build στην επόμενη εκκίνηση του Build;', nolabel='Ακύρωση',yeslabel='[COLOR red]Απενεργοποίηση[/COLOR]')
    if yes_enable:
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "service.world.build","enabled":false}}')
        setting_set('updaterversion','false')
        ok = dialog.ok(addon_name, 'Απενεργοποιήσατε τις αυτόματες ενημερώσεις του World Updater!!')
        # exit()
        # xbmc.sleep(500)
        # xbmc.executebuiltin('Dialog.Close(all,true)')
        xbmc.executebuiltin('Action(Back)')
        # xbmc.executebuiltin('Dialog.Close(all,true)')
        # xbmc.executebuiltin('ActivateWindow(10000)')
        
    else:
        # xbmc.executebuiltin('Dialog.Close(all,true)')
        # xbmc.executebuiltin('Action(Back)')
        return
        
def enable_downloader_startup():
    yes_enable = dialog.yesno(addon_name, 'Θέλετε να ενεργοποιήσετε τις αυτόματες ενημερώσεις[CR]του World Build στην επόμενη εκκίνηση του Build;', nolabel='Ακύρωση',yeslabel='[COLOR lime]Ενεργοποίηση[/COLOR]')
    if yes_enable:
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "service.world.build","enabled":true}}')
        setting_set('updaterversion','0')
        ok = dialog.ok(addon_name, 'Eνεργοποιήσατε τις αυτόματες ενημερώσεις του World Updater!!')
        # exit()
        # xbmc.sleep(500)
        # xbmc.executebuiltin('Dialog.Close(all,true)')
        xbmc.executebuiltin('Action(Back)')
        # xbmc.executebuiltin('Dialog.Close(all,true)')
        # xbmc.executebuiltin('ActivateWindow(10000)')
    else:
        # xbmc.executebuiltin('Dialog.Close(all,true)')
        # xbmc.executebuiltin('Action(Back)')
        return
        

def cancel_next_start():
    yes_cancel = dialog.yesno(addon_name, 'Θέλετε να ακυρώσετε την ενεργοποίηση όλων των πρόσθετων κατά την επόμενη εκκίνηση;', nolabel='Διατήρηση Ενεργ/σης',yeslabel='Ακύρωση Ενεργ/σης')
    if yes_cancel:
        setting_set('autoenable','false')
        ok = dialog.ok(addon_name, 'Η ενεργοποίηση των πρόσθετων ακυρώθηκε.')
    else:
        return

def cache_clear():
    cache.clear(withyes=False)


def search_clear():
    cache.delete(control.searchFile, withyes=False)
    control.refresh()
    control.idle()


def BuildMenu():
    req = Request(bzipfile, headers = headers)
    response = urlopen(req).read()
    try:
        builds = json.loads(response)['builds']
        for build in builds:
            name = (build.get('name', ''))
            url = (build.get('url', ''))
            icon = (build.get('icon', addon_icon))
            fanart = (build.get('fanart', addon_fanart))
            description = (build.get('description', 'No Description Available.'))
            if url.endswith('.zip'):
                addDir(name,url,11,icon,fanart,description,name2=name,isFolder=False)
            else:
                addDir('Μη έγκυρη διεύθυνση URL έκδοσης. Επικοινωνήστε με τον δημιουργό του build.','','','','','',isFolder=False)
    except:
        builds = ET.fromstring(response)
        for build in builds.findall('build'):
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
                addDir(name,url,11,icon,fanart,description,name2=name,isFolder=False)
            else:
                addDir('Μη έγκυρη διεύθυνση URL έκδοσης. Επικοινωνήστε με τον δημιουργό του build.','','','','','',isFolder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def freshStart():
    dialog.notification("[B][COLOR red]Διαγραφή[/COLOR][/B]",'[COLOR white]όλων των δεδομένων![/COLOR]' , icon_Build)
    if mode == 11:
        if not currSkin() in ['skin.estuary']:
            skinSwitch.swapSkins('skin.estuary')
            x = 0
            xbmc.sleep(1000)
            while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 150:
                x += 1
                xbmc.sleep(200)
                xbmc.executebuiltin('SendAction(Select)')
            if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
                xbmc.executebuiltin('SendClick(11)')
            else: 
                log('Fresh Install: Skin Swap Timed Out!', xbmc.LOGINFO)
                return False
            xbmc.sleep(1000)
        if not currSkin() in ['skin.estuary']:
            log('Fresh Install: Skin Swap failed.', xbmc.LOGINFO)
            return
        
        if mode==10:
            save_menu()
            save_check()
            save_backup()
            
        dp.create(addon_name, 'Διαγραφή αρχείων και φακέλων...')
        xbmc.sleep(1000)
        dp.update(30, 'Διαγραφή αρχείων και φακέλων...')
        xbmc.sleep(1000)
        for root, dirs, files in os.walk(xbmcPath, topdown=True):
            dirs[:] = [d for d in dirs if d not in EXCLUDES]
            for name in files:
                if name not in EXCLUDES:
                    try:
                        os.remove(os.path.join(root, name))
                    except:
                        log('Unable to delete ' + name, xbmc.LOGINFO)
        dp.update(60, 'Διαγραφή αρχείων και φακέλων...')
        xbmc.sleep(1000)
        for root, dirs, files in os.walk(xbmcPath,topdown=True):
            dirs[:] = [d for d in dirs if d not in EXCLUDES]
            for name in dirs:
                if name not in ["Database","userdata","temp","addons","packages","addon_data"]:
                    try:
                        shutil.rmtree(os.path.join(root,name),ignore_errors=True, onerror=None)
                    except:
                        log('Unable to delete ' + name, xbmc.LOGINFO)
        dp.update(60, 'Διαγραφή αρχείων και φακέλων...')
        xbmc.sleep(1000)
        if not os.path.exists(packages):
            os.mkdir(packages)
        dp.update(100, 'Διαγραφή αρχείων και φακέλων...Ολοκληρώθηκε!')
        xbmc.sleep(2000)
        if mode == 10:
            dialog.ok(addon_name, 'Η διαγραφή ολοκληρώθηκε.[CR] Πατήστε εντάξει για να κλείσει το kodi.')
            os._exit(1)
    else:
        return

def GetParams():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param

params=GetParams()
url=None
name=None
name2=None
version=None
mode=None
iconimage=None
fanart=None
description=None
log(str(params),xbmc.LOGDEBUG)

try:
    url=unquote_plus(params["url"])
except:
    pass
try:
    name=unquote_plus(params["name"])
except:
    pass
try:
    iconimage=unquote_plus(params["iconimage"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass
try:
    fanart=unquote_plus(params["fanart"])
except:
    pass
try:
    description=unquote_plus(params["description"])
except:
    pass
try:
    name2 =unquote_plus(params["name2"])
except:
    pass
try:
    version =unquote_plus(params["version"])
except:
    pass


xbmc.executebuiltin('Dialog.Close(busydialog)')

if mode==None:
    MainMenu()

elif mode==1:
    from resources.lib.modules.apiYutube import ApiMenu
    ApiMenu()

elif mode==2:
    xbmcaddon.Addon(addon_id).openSettings()

elif mode==3:
    main_ApiMenu(name, name2, version, url, iconimage, fanart, description)

elif mode==4:
    from resources.lib.modules import maintenance
    maintenance.advanced_settings()

elif mode==5:
    subMenu_maintenance()

elif mode==6:
    from resources.lib.modules import maintenance
    maintenance.clear_packages()

elif mode==7:
    from resources.lib.modules import maintenance
    maintenance.clear_thumbnails()

elif mode==8:
    from resources.lib.modules import maintenance
    maintenance.advanced_settings()


elif mode==9:
    main_Skinshortcuts(name, name2, version, url, iconimage, fanart, description)

elif mode==10:
    freshStart()

elif mode==11:
    main_BuildMenu(name, name2, version, url, iconimage, fanart, description)

elif mode==12:
    BuildMenu()

elif mode==13:
    from resources.lib.modules.skin import skin_menu

elif mode==14:
    from resources.lib.modules.tools import tools_menu

elif mode==15:
    main_downloader(name, name2, version, url, iconimage, fanart, description)
    xbmc.sleep(2000)
    from resources.lib.modules import addonsEnable
    addonsEnable.enable_addons()

elif mode==16:
    from resources.lib.modules.installer_binary import Installer_Binary_Addons

elif mode == 17:
    main_backup_restore()

elif mode == 18:
    backup_build()

elif mode == 19:
    restore_menu()

elif mode == 20:
    restore_build(url)

elif mode == 21:
    get_backup_folder()

elif mode == 22:
    reset_backup_folder()

elif mode == 23:
    from resources.lib.modules.cache import clear_provider
    clear_provider()
 
#elif mode == 23:
#    play_video(name, url, icon, description)

elif mode == 24:
    from resources.lib.modules.derbid_authorize import derbid_authorize

elif mode == 25:
    enable_now()

elif mode == 26:
    enable_next_start()

elif mode == 27:
    cancel_next_start()

elif mode == 28:
    main_enable_addons()

elif mode == 29:
    disable_downloader_startup()

elif mode == 30:
    enable_downloader_startup()

elif mode == 31:
    from resources.lib.modules.speedtester.addon import run
    run()

elif mode == 32:
    from resources.lib.modules.quick_log import log_viewer
    log_viewer()

elif mode==33:
    main_maintenance()

elif mode==100:
    from resources.lib.GUIcontrol import notify
    d=notify.notify()
    d.doModal()
    del d


elif mode == 122:
    xbmc.executebuiltin('ActivateWindow(10001,"plugin://plugin.program.G.K.N.Wizard/?mode=viewbuild&name=World%20-Omega-")')

xbmcplugin.endOfDirectory(int(sys.argv[1]))