import os, xbmc, xbmcgui, glob, shutil
from updatervar import *

def tools_menu():
    funcs = (click1, click2, click3, click4, click5, click6, click7, click8, click9, click10, click11, click12, click13, click14, click15,
             click16, click17, click18, click19, click20, click21, click22, click23)
    selection = xbmcgui.Dialog().select('[B][COLOR=orange]~ Εργαλεία World Updater ~[/COLOR][/B]', 
['[B][COLOR=white]Ενεργοποίηση όλων των πρόσθετων ...[/COLOR][/B]',

 '[B][COLOR=white]Έλεγχος Αναβάθμισης Πρόσθετων ...[/COLOR][/B]',
 
 '[B][COLOR=white]Καθαρισμός παρόχων-Cache[/COLOR][/B]',
 
 '[B][COLOR=white]Αν δεν εμφανίζονται τα Widgets ή τα Εικονίδια ...[/COLOR][/B]',
 
 '[B][COLOR=orange]Advanced Settings [COLOR=white](Wizard)[/COLOR][/B]',
 
 '[B][COLOR=white]Εγκατάσταση Binary Addons[/COLOR][/B]',
 
 '[B][COLOR=white]Επιλογή Api Key [COLOR red]YouTube[/COLOR][/B]',
 
 '[B][COLOR=white]Επαναφορά αρχικού μενού[/COLOR][/B]',
 
 '[B][COLOR=white]Εξουσιοδότηση [COLOR lime]Trakt ...[/COLOR][/B]',
 
 '[B][COLOR=white]Authorize-Reset [COLOR lime]Derbid...[/COLOR][/B]',
 
 '[B][COLOR=white]Εργαλεία G.K.N.Wizard[/COLOR][/B]',
 
 '[B][COLOR=white]Διαγραφή PVR Stalker[/COLOR][/B]',
 '[B][COLOR=white]Ρυθμίσεις [COLOR lime]ResolveURL[/COLOR][/B]',
#'[B][COLOR=white]Διαγραφή Indigo...[/COLOR][/B]',
 '[B][COLOR=lime]Καθαρή Εγκατάσταση Build [B][COLOR blue]*G.K.N.Wizard*[/COLOR][/B]',
 '[B][COLOR=blue]G.K.N.[COLOR=white]Wizard[/COLOR][/B]',
 '[B][COLOR=white]Αφαίρεση πρόσθετων[/COLOR][/B]',
 
 '[B][COLOR=white]Save Data[/COLOR][/B]',
 
 '[B][COLOR=white]Reload Skin[/COLOR][/B]',
 
 '[B][COLOR=white]Enable/Disable Addons[/COLOR][/B]',
 
 '[B][COLOR=white]Speed Test[/COLOR][/B]',
 
 '[B][COLOR=white]Εργαλεία AliveGR[/COLOR][/B]',
 
 '[B][COLOR=orange]Απενεργοποίηση [COLOR=white]αυτόματων ενημερώσεων του Downloader Startup[/COLOR][/B]',
 '[B][COLOR=lime]Ενεργοποίηση [COLOR=white]αυτόματων ενημερώσεων του Downloader Startup[/COLOR][/B]'])

    if selection:
        if selection < 0:
            return
        func = funcs[selection-23]
        return func()
    else:
        func = funcs[selection]
        return func()
    return 


def click1():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.downloader19/?mode=25,return)')

def click2():
    xbmc.executebuiltin('UpdateLocalAddons')
    xbmc.executebuiltin('UpdateAddonRepos')
    # xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/addonupdatesprog.py")')

def click3():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=clearcache)')
    xbmc.sleep(2000)
    if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
        xbmc.sleep(1000)
        xbmc.executebuiltin('SendClick(11)')
        xbmc.sleep(500)
        xbmc.executebuiltin('RunPlugin(plugin://plugin.program.downloader19/?mode=23)')
        xbmc.sleep(5000)
        xbmc.executebuiltin("Action(Close)")

xbmc.sleep(1000)


    # xbmc.executebuiltin('PlayMedia("plugin://plugin.program.G.K.N.Wizard/?mode=clearthumb")')
    # xbmc.sleep(15000)
    # xbmc.executebuiltin('PlayMedia("plugin://plugin.program.G.K.N.Wizard/?mode=convertpath")')
    # xbmc.sleep(10000)
    # xbmc.executebuiltin("ReloadSkin()")


def click4():
    
    xbmcgui.Dialog().notification("Παρακαλώ Περιμένετε...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/Pleasewait.png', sound=True)
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=clearthumb)')
    xbmc.sleep(1000)
    xbmc.executebuiltin('SendClick(11)')
    xbmc.sleep(15000)
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=convertpath)')
    xbmc.sleep(10000)
    xbmc.executebuiltin("ReloadSkin()")
    xbmc.executebuiltin('ActivateWindow(10000)')
    xbmcgui.Dialog().notification("Εντάξει!", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/itsok.jpg', sound=True)

def click5():
        choice = xbmcgui.Dialog().yesno('World Tools', '[COLOR white]Για να επιτύχουμε καλύτερο streaming του Βίντεο, αλλάζουμε την τιμή στο Video Cache size από αυτήν που έχει μπαίνοντας στο *Advanced Settings Configurator* σε 120 μέχρι 150! Μετά πατάμε Write File και κάνουμε επανεκκίνηση το Kodi για να καταχωρηθούν οι αλλαγές! [B][COLOR red]Tip:[/COLOR][/B] [COLOR white]Για καλύτερο buffering πατάμε παύση [COLOR lime](||)[COLOR white] στην Έναρξη του Βίντεο για μερικά λεπτά.[/COLOR]',
                                        nolabel='[COLOR red]Άκυρο[/COLOR]',yeslabel='[COLOR lime]Advanced Settings[/COLOR]')

        if choice == 1: xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=autoadvanced)')

def click6():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.downloader19/?mode=16,return)')

def click7():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.downloader19/?mode=1,return)')

def click8():
    xmlskinversion2046()
    # xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloaderstartup/UpdaterMatrix_8.py")')

def click9():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.video.blacklodge/?action=authTrakt)')

def click10():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.downloader19/?mode=24,return)')

def click11():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.G.K.N.Wizard/?mode=maint,return)')

def click12():
        choice = xbmcgui.Dialog().yesno('[B][COLOR orange]World[/COLOR][/B]', '[COLOR white]Επιθυμείτε την διαγραφή του PVR Stalker ?[/COLOR]',
                                        nolabel='[COLOR orange]Άκυρο[/COLOR]',yeslabel='[COLOR lime]Διαγραφή[/COLOR]')

        if choice == 1: [xbmc.executebuiltin("Action(Close)"), xbmc.sleep(1000), xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}'),
                         xbmc.sleep(5000), xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')]
        base_path = xbmc.translatePath('special://home/addons')
        dir_list = glob.iglob(os.path.join(base_path, "pvr.stalker"))
        for path in dir_list:
            if os.path.isdir(path):
                shutil.rmtree(path)
            if os.path.exists(base_path): xbmcgui.Dialog().notification("[B][COLOR orange]World[/COLOR][/B]", "[COLOR white]Το PVR Stalker αφαιρέθηκε με επιτυχία![/COLOR]", icon='special://skin/icon.png')

def click13():
    xbmc.executebuiltin('Addon.OpenSettings(script.module.resolveurl)')


    #import resolveurl
    #resolveurl.display_settings()




    #base_path = xbmcvfs.translatePath('special://home/addons')
    #dir_list = glob.iglob(os.path.join(base_path, "plugin.program.indigo"))
    #for path in dir_list:
        #if os.path.isdir(path):
            #shutil.rmtree(path)

    #base_path = xbmcvfs.translatePath('special://home/userdata/addon_data')
    #dir_list = glob.iglob(os.path.join(base_path, "plugin.program.indigo"))
    #for path in dir_list:
        #if os.path.isdir(path):
            #shutil.rmtree(path)

    #base_path = xbmcvfs.translatePath('special://home/addons')
    #dir_list = glob.iglob(os.path.join(base_path, "script.tvaddons.debug.log"))
    #for path in dir_list:
        #if os.path.isdir(path):
            #shutil.rmtree(path)

    #xbmcgui.Dialog().ok("[COLOR orange]World Updater-Tools[/COLOR]", "[COLOR white]Bye Bye --> plugin.program.indigo[/COLOR]")

def click14():
    xbmc.executebuiltin('ActivateWindow(10001,"plugin://plugin.program.G.K.N.Wizard/?mode=viewbuild&name=World%20-Nexus-")')

def click15():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.G.K.N.Wizard)')

def click16():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=removeaddons)')

def click17():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.G.K.N.Wizard/?mode=savedata)')

def click18():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=forceskin)')

def click19():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.G.K.N.Wizard/?mode=enableaddons,return)')

def click20():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.G.K.N.Wizard/?mode=speedtest,return)')

def click21():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.AliveGR/?action=settings&title=%ce%95%cf%81%ce%b3%ce%b1%ce%bb%ce%b5%ce%af%ce%b1")')

def click22():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.downloader19/?mode=29,return)')

def click23():
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.downloader19/?mode=30,return)')



def xmlskinversion2046():
    addon_downloader19       = xbmcaddon.Addon('plugin.program.downloader19')
    setting_downloader19     = addon_downloader19.getSetting
    setting_set_downloader19 = addon_downloader19.setSetting
    if setting_downloader19('xmlskinversion')=='2046':
        xbmcgui.Dialog().ok('[COLOR red] Skin[/COLOR] Menu Tools', 'Η επιλογή αυτή είναι διαθέσιμη μόνο στο Προκαθορισμένο Skin')
    else:
        xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloaderstartup/PY/skin/SkinUp/set_setting_FixSkin.py")')






tools_menu()

#def click24():
#        choice = xbmcgui.Dialog().yesno('[B][COLOR orange]World[/COLOR][/B]', '[COLOR white]      Επιθυμείτε την απενεργοποίηση των ενημερώσεων [CR]                        του World Updater ?[/COLOR]',
#                                        nolabel='[COLOR lime]Ενεργοποίηση[/COLOR]',yeslabel='[COLOR orange]Απενεργοποίηση[/COLOR]')
#        if choice == 1: [xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "plugin.program.downloader19","enabled":false}}'), xbmcgui.Dialog().ok("[COLOR lime]World Updater-Tools[/COLOR]", "[COLOR orange]Απενεργοποήθηκαν οι αυτόματες ενημερώσεις         του World Updater.[/COLOR]")]
#        else:
#            xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "plugin.program.downloader19","enabled":true}}')



