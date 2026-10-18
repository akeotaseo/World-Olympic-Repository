
import xbmc, xbmcgui, xbmcvfs, sys, json, os, re, glob, shutil, subprocess
from updatervar import *
from resources.lib.GUIcontrol import notify
from resources.lib.GUIcontrol.notify import get_notifyversion
from resources.lib.GUIcontrol.txt_updater import get_addonsrepos, get_xmlskin, get_players, get_set_setting, get_var
from resources.lib.GUIcontrol.txt_updater import get_addons_list_installation, get_delete_files, get_zip1, get_zip2, get_zip3, get_zip4, get_zip5
from resources.lib.GUIcontrol.txt_updater import get_pvr
from resources.lib.modules import addonsEnable
from resources.lib.modules import db, addonsEnable
from resources.lib.modules.addonsEnable import enable_addons

addons_list_installation_version = get_addons_list_installation()
notify_version       = get_notifyversion()
addons_repos_version = get_addonsrepos()
xmlskin_version      = get_xmlskin()
players_version      = get_players()
set_setting_version  = get_set_setting()
delete_files_version = get_delete_files()
var_version          = get_var()
zip1_version         = get_zip1()
zip2_version         = get_zip2()
zip3_version         = get_zip3()
zip4_version         = get_zip4()
zip5_version         = get_zip5()
pvr_version          = get_pvr()
dialog = xbmcgui.Dialog()
settings_path = xbmcvfs.translatePath('special://home/backup/skin.19MatrixWorld/')
homeset_path = xbmcvfs.translatePath('special://home/backup/skin.19MatrixWorld/')


def autoenable():
    if setting('autoenable') == 'true':
        addonsEnable.enable_addons()
        setting_set('autoenable','false')
        dialog.notification(Dialog_enable_on, Dialog_enable, icon_Build, sound=False)


def notifyT():
    if not setting('firstrunNotify')=='false':
        if notify_version > int(setting('notifyversion')):
            setting_set('notifyversion', str(notify_version))
            d=notify.notify()
            d.doModal()
            del d
            BG.create(Dialog_U8, Dialog_U6)
            xbmc.sleep(5000)
            BG.close()


def var():
    if var_version > int(setting('varversion')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Var_startup)
        xbmc.sleep(1000)
        xbmc.executebuiltin(XmlSkin_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('varversion', str(var_version))
        BG.update(55, Dialog_U12, '[COLOR green]Var...[/COLOR]')
        xbmc.sleep(1000)
        BG.update(75, Dialog_U12, '[COLOR green]Var...[/COLOR]')
        xbmc.sleep(1000)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()
        xbmc.executebuiltin("ReloadSkin()")


def delete():
    if delete_files_version > int(setting('deleteversion')):
        xbmcvfs.delete('special://home/userdata/addon_data/plugin.program.downloader19/delete_files.py')
        xbmc.sleep(4000)
        xbmc.executebuiltin(Delete_startup)
        BG.create(Dialog_U2, Dialog_U11)
        xbmc.sleep(3000)
        BG.update(33, Dialog_U2, Dialog_U11)
        xbmc.sleep(5000)
        BG.update(63, Dialog_U2, Dialog_U11)
        xbmc.sleep(7000)
        BG.update(100, Dialog_U2, Dialog_U10)
        xbmc.sleep(10000)
        xbmc.executebuiltin(del_startup)
        setting_set('deleteversion', str(delete_files_version))
        BG.update(100, Dialog_U12, Dialog_U2)
        xbmc.sleep(10000)
        BG.update(100, Dialog_U12, Dialog_U2)
        xbmc.sleep(10000)
        BG.close()


def installation():
    if addons_list_installation_version > int(setting('installationversion')):
        xbmcvfs.delete('special://home/userdata/addon_data/plugin.program.downloader19/addons_list_installation.py')
        xbmc.sleep(2000)
        xbmc.executebuiltin(Installation_startup)
        BG.create(Dialog_U12, Dialog_U6)
        xbmc.sleep(3000)
        BG.update(30, Dialog_U12, Dialog_U2)
        xbmc.sleep(4000)
        BG.update(50, Dialog_U12, 'Έλεγχος εγκατάστασης νέων πρόσθετων...')
        xbmc.sleep(5000)
        BG.update(70, Dialog_U12, 'Έλεγχος εγκατάστασης νέων πρόσθετων...')
        xbmc.sleep(5000)
        BG.update(85, Dialog_U1, 'Ο έλεγχος ολοκληρώθηκε...')
        xbmc.sleep(6000)
        xbmc.executebuiltin(install_startup)
        setting_set('installationversion', str(addons_list_installation_version))
        xbmc.sleep(8000)
        BG.update(100, Dialog_U12, Dialog_U2)
        xbmc.sleep(10000)
        BG.update(100, Dialog_U12, Dialog_U2)
        xbmc.sleep(10000)
        BG.close()


def setsetting():
    if set_setting_version > int(setting('setsettingversion')):
        xbmcvfs.delete('special://home/userdata/addon_data/plugin.program.downloader19/set_setting.py')
        xbmc.sleep(4000)
        xbmc.executebuiltin(SetSetting_startup)
        xbmc.sleep(5000)
        setting_set('setsettingversion', str(set_setting_version))
        dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False)
        xbmc.sleep(5000)


def players():
    if players_version > int(setting('playersversion')):
        BG.create(Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(5, Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_Players)
        xbmc.executebuiltin(Players_startup)
        xbmc.sleep(1500)
        BG.update(25, Dialog_U12, Dialog_Players)
        xbmc.sleep(500)
        setting_set('playersversion', str(players_version))
        BG.update(55, Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_Players)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def zip1():
    if zip1_version > int(setting('zip1version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip1_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip1version', str(zip1_version))
        BG.update(55, Dialog_U12, '[COLOR green]Zip1...[/COLOR]')
        xbmc.sleep(500)
        BG.update(75, Dialog_U12, '[COLOR green]Zip1...[/COLOR]')
        xbmc.sleep(500)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def zip2():
    if zip2_version > int(setting('zip2version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(1000)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(1000)
        xbmc.executebuiltin(Zip2_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(1000)
        setting_set('zip2version', str(zip2_version))
        BG.update(35, Dialog_U12, 'install addons')
        xbmc.sleep(1000)
        BG.update(45, Dialog_U12, 'install addons')
        xbmc.sleep(2000)
        BG.update(55, Dialog_U12, 'Παρακαλώ περιμένετε...')
        xbmc.sleep(2000)
        BG.update(65, Dialog_U12, 'Παρακαλώ περιμένετε...')
        xbmc.sleep(2000)
        BG.update(75, Dialog_U12, 'Παρακαλώ περιμένετε...')
        addonsEnable.enable_addons()
        xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Database_Addons33_Enable.py")')
        xbmc.sleep(500)
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')
        BG.update(85, Dialog_U12, '[COLOR green]enable_addons...[/COLOR]')
        xbmc.sleep(3000)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(3000)
        dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False)
        BG.close()

def zip3():
    if zip3_version > int(setting('zip3version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(1000)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(1000)
        xbmc.executebuiltin(Zip3_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(1000)
        setting_set('zip3version', str(zip3_version))
        BG.update(55, Dialog_U12, 'addon_data')
        xbmc.sleep(1000)
        BG.update(75, Dialog_U12, 'addon_data')
        xbmc.sleep(1000)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def zip4():
    if zip4_version > int(setting('zip4version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip4_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip4version', str(zip4_version))
        BG.update(55, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()



def zip5():
    if zip5_version > int(setting('zip5version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip5_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        setting_set('zip5version', str(zip5_version))
        BG.update(40, Dialog_U12, '[COLOR green]manually update addons...[/COLOR]')
        xbmc.sleep(1000)
        BG.update(50, Dialog_U12, '[COLOR lime]manually fix addons...[/COLOR]')
        xbmc.sleep(1000)
        BG.update(60, Dialog_U12, 'Παρακαλώ περιμένετε...')
        xbmc.sleep(500)
        BG.update(70, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        BG.update(80, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def pvr():
    if pvr_version > int(setting('pvrversion')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(1000)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(1000)
        xbmc.executebuiltin(Pvr_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12,'IPTV Simple Client')
        xbmc.sleep(1000)
        BG.update(35, Dialog_U12,'Stalker Client')
        xbmc.sleep(1000)
        BG.update(45, Dialog_U12,'mac_list')
        xbmc.sleep(1000)
        setting_set('pvrversion', str(pvr_version))
        BG.update(50, Dialog_U12, Dialog_U3)
        xbmc.sleep(1000)
        BG.update(60, Dialog_U12, 'Παρακαλώ περιμένετε...')
        xbmc.sleep(2000)
        BG.update(70, Dialog_U12, 'Παρακαλώ περιμένετε...')
        xbmc.sleep(2000)
        BG.update(80, Dialog_U12, 'Παρακαλώ περιμένετε...')
        xbmc.sleep(2000)
        BG.update(90, Dialog_U12, 'Παρακαλώ περιμένετε...')
        xbmc.sleep(2000)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()


def database():
    if addons_repos_version > int(setting('addonsreposversion')):
        xbmcvfs.delete('special://home/userdata/addon_data/plugin.program.downloader19/Database_Addons33.py')
        xbmc.sleep(4000)
        xbmc.executebuiltin(AddonsRepos_startup)
        BG.create(Dialog_U8, Dialog_Database)
        xbmc.sleep(4000)
        BG.update(33, Dialog_U8, Dialog_Database)
        xbmc.sleep(4000)
        BG.update(63, Dialog_U12, Dialog_Database)
        xbmc.sleep(4000)
        BG.update(76, Dialog_U12, Dialog_Database)
        xbmc.sleep(4000)
        xbmc.executebuiltin(database_startup)
        xbmc.sleep(1000)
        addonsEnable.enable_addons()
        BG.update(85, Dialog_U12, '[COLOR lime]enable_addons...[/COLOR]')
        xbmc.sleep(500)
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')
        setting_set('addonsreposversion', str(addons_repos_version))
        xbmc.sleep(5000)
        BG.update(100, Dialog_U1, '[COLOR red]Περιμένετε χωρίς να πατήσετε κάτι...[/COLOR]')
        xbmc.sleep(5000)
        BG.update(100, Dialog_U1, '[COLOR cornflowerblue]Περιμένετε λίγο ακόμα...[/COLOR]')
        xbmc.sleep(5000)
        BG.update(95, Dialog_U9, Dialog_U2)
        xbmc.sleep(2000)
        dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False) 
        xbmc.sleep(2000)
        BG.close()


def xmlskin():
    if not setting('xmlskinversion') == 'false':
        if xmlskin_version > int(setting('xmlskinversion')):
            BG.create(Dialog_U12, Dialog_Xml_Skin)
            BG.update(5, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            BG.update(15, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            xbmc.executebuiltin(XmlSkin_startup)
            xbmc.sleep(1000)
            BG.update(25, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(500)
            setting_set('xmlskinversion', str(xmlskin_version))
            BG.update(55, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            BG.update(75, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            BG.update(80, Dialog_U12, Dialog_U9)
            xbmc.sleep(1000)
            BG.update(90, Dialog_U1, 'Ενημέρωση μενού skin.')
            xbmc.sleep(5000)
            BG.update(95, Dialog_U4, 'Θα ακολουθήσει... επαναφόρτωση του προφίλ')
            xbmc.sleep(3000)
            BG.update(100, Dialog_U4, 'Θα ακολουθήσει... και πάγωμα της εικόνας')
            dialog.notification('[B][COLOR orange]Reload Profile[/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_reloadprofile, sound=False)
            xbmc.sleep(4000)
            xbmc.executebuiltin("LoadProfile(Master user)")
            BG.close()
            xbmc.sleep(15000)

#TEST
def xmlskinTest():
    if not setting('xmlskinversion') == 'false':
        if xmlskin_version > int(setting('xmlskinversion')):
            BG.create(Dialog_U12, Dialog_Xml_Skin)
            BG.update(5, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            BG.update(15, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(200)
            xbmc.executebuiltin(XmlSkin_startup)
            xbmc.sleep(1000)
            BG.update(25, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(500)
            setting_set('xmlskinversion', str(xmlskin_version))
            BG.update(55, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(1000)
            BG.update(75, Dialog_U12, Dialog_Xml_Skin)
            xbmc.sleep(2000)
            BG.update(80, Dialog_U12, Dialog_U9)
            xbmc.sleep(3000)
            BG.update(90, Dialog_U1, '   ')
            xbmc.sleep(4000)
            BG.update(95, 'Ενημέρωση μενού skin' '   ')
            xbmc.sleep(5000)
            BG.update(100, Dialog_U4, '   ')
            # dialog.notification('[B][COLOR orange]Reload Profile[/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_reloadprofile, sound=False)
            xbmc.sleep(5000)
            # xbmc.executebuiltin("LoadProfile(Master user)")
            BG.close()
            xbmc.executebuiltin("ReloadSkin()")
            # xbmcgui.Dialog().ok('Skin World', 'Για να εφαρμοστούν οι αλλαγές, το Kodi πρέπει να κλείσει.')
            # xbmc.sleep(15000)
            # os._exit(1)


def xmlskin3():
    if not setting('xmlskinversion') == 'false':
        if xmlskin_version > int(setting('xmlskinversion')):
            BG.create('Skin World', 'Αντιγραφή.')
            xbmc.sleep(500)
            setting_set('xmlskinversion', str(xmlskin_version))
            BG.close()
            xbmcgui.Dialog().ok('Skin World', 'Για να εφαρμοστούν οι αλλαγές, το Kodi πρέπει να κλείσει.')
            os._exit(1)



def Backup_Skin_Set():
    src_settings = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.19MatrixWorld/settings.xml')
    dst_settings = xbmcvfs.translatePath('special://home/backup/skin.19MatrixWorld/settings.xml')
    addon_downloader19       = xbmcaddon.Addon('plugin.program.downloader19')
    setting_downloader19     = addon_downloader19.getSetting
    # setting_set_downloader19 = addon_downloader19.setSetting
    if not setting_downloader19('xmlskinversion')=='2046':
        xbmc.sleep(500)
        # setting_set_downloader19('xmlskinversion', '2046')
        shutil.copyfile(src_settings, dst_settings)


def Backup_Home_Set():
    src_homeset = xbmcvfs.translatePath('special://home/addons/skin.19MatrixWorld/xml/Home.xml')
    dst_homeset = xbmcvfs.translatePath('special://home/backup/skin.19MatrixWorld/Home.xml')
    addon_downloader19       = xbmcaddon.Addon('plugin.program.downloader19')
    setting_downloader19     = addon_downloader19.getSetting
    # setting_set_downloader19 = addon_downloader19.setSetting
    if not setting_downloader19('xmlskinversion')=='2046':
        xbmc.sleep(500)
        # setting_set_downloader19('xmlskinversion', '2046')
        shutil.copyfile(src_homeset, dst_homeset)

def UpdateAddonRepos():
    xbmc.sleep(1000)
    # Install updates automatically
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')
    xbmc.sleep(1000)
    xbmcgui.Dialog().notification("Add-ons Updates...", "[COLOR green]Enable[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/auto5.png', sound=False)
    xbmc.sleep(2000)
    xbmcgui.Dialog().notification("Check...", "Ελεγχος για ενημερώσεις προσθέτων", icon='special://home/addons/plugin.program.downloader19/resources/media/auto3.png', sound=False)
    xbmc.sleep(2000)
    # xbmcgui.Dialog().notification("Check...", "Ελεγχος για ενημερώσεις προσθέτων", icon='special://home/addons/plugin.program.downloader19/resources/media/auto2.png', sound=False)
    # xbmc.sleep(4000)
    # xbmcgui.Dialog().notification("Check...", "Ελεγχος για ενημερώσεις προσθέτων", icon='special://home/addons/plugin.program.downloader19/resources/media/auto1.png', sound=False)

    # xbmc.sleep(15000)
    # if xbmc.getCondVisibility('integer.IsGreater(System.AddonUpdateCount,0)'):

    xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/addonupdatesprog.py")')
    xbmc.sleep(20000)
    Backup_Skin_Set()
    Backup_Home_Set()
    

    # else: dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False)
    

    # xbmc.executebuiltin('ActivateWindow(2139)')
    #xbmc.executebuiltin('PlayMedia("special://home/media/Bamako.mp4")')
    # xbmc.executebuiltin('PlayMedia("special://home/media/Join_file.mp4")')
    # xbmc.sleep(12000)
        
    # xbmc.executebuiltin('ActivateWindow(2139)')
    # xbmc.sleep(4000)
    # UpdatesStatus()
    
    
    



    # xbmc.executebuiltin('UpdateLocalAddons()')
    # xbmc.sleep(4000)
    # xbmc.executebuiltin('UpdateAddonRepos()')

