 # -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcvfs, sys, json, os, re, glob, shutil, xbmcaddon
from threading import Thread
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"screensaver.xbmc.builtin.dim"},"id":"1"}')
##MANALAB____________________________________________________________
xbmc.executebuiltin('RunScript("special://home/addons/skin.19MatrixWorld/xml/_get_ip.py")')
xbmcgui.Dialog().notification("MyWANIP__MyCountry", "IPServiceRunning", icon='special://home/addons/skin.19MatrixWorld/media/_get_ip.png', sound=False)
##MANALAB____________________________________________________________


dp = xbmcgui.DialogProgressBG()

HOME           = xbmcvfs.translatePath('special://home/')
ADDONS         = os.path.join(HOME,     'addons')
ADDONPATH      = os.path.join(ADDONS, 'plugin.program.downloader19')
FANART         = os.path.join(ADDONPATH, 'fanart.jpg')
ICON           = os.path.join(ADDONPATH, 'icon.png')
SKINFOLD       = os.path.join(ADDONPATH, 'resources', 'skins', 'DefaultSkin', 'media')
ADDONTITLE     = '[B]World Υπηρεσία Ενημέρωσης[/B]'

class MainMonitor(xbmc.Monitor):
    def __init__(self):
        super(MainMonitor, self).__init__()

monitor = MainMonitor()

ACTION_PREVIOUS_MENU            =  10   ## ESC action
ACTION_NAV_BACK                 =  92   ## Backspace action
ACTION_MOVE_LEFT                =   1   ## Left arrow key
ACTION_MOVE_RIGHT               =   2   ## Right arrow key
ACTION_MOVE_UP                  =   3   ## Up arrow key
ACTION_MOVE_DOWN                =   4   ## Down arrow key
ACTION_MOUSE_WHEEL_UP           = 104   ## Mouse wheel up
ACTION_MOVE_MOUSE               = 107   ## Down arrow key
ACTION_SELECT_ITEM              =   7   ## Number Pad Enter
ACTION_BACKSPACE                = 110   ## ?
ACTION_MOUSE_LEFT_CLICK         = 100
ACTION_MOUSE_LONG_CLICK         = 108


##########################
### Converted to XML
##########################

def progress(msg="", t=1, image=ICON, dw='Progress.xml'):
        class MyWindow(xbmcgui.WindowXMLDialog):
            def __init__(self, *args, **kwargs):
                if monitor.waitForAbort(0.5):
                    sys.exit()
                # xbmc.sleep(500)
                self.title = '[COLOR white]%s[/COLOR]' % ADDONTITLE
                self.image = image
                if "ERROR" in kwargs["msg"]:
                    self.image = os.path.join(SKINFOLD, 'Icons', 'defaulticonerror.png')
                self.fanart = FANART
                self.msg = '[COLOR darkorange]%s[/COLOR]' % kwargs["msg"]
                if "ERROR" in kwargs["msg"]:
                    self.msg = '[COLOR red]%s[/COLOR]' % kwargs["msg"]


            def onInit(self):
                self.fanartimage = 101
                self.titlebox = 102
                self.imagecontrol = 103
                self.textbox = 104
                self.showdialog()

            def showdialog(self):
                self.getControl(self.imagecontrol).setImage(self.image)
                self.getControl(self.fanartimage).setImage(os.path.join(SKINFOLD, 'Background', 'progress-dialog-bg.png'))
                self.getControl(self.fanartimage).setColorDiffuse('9FFFFFFF')
                self.getControl(self.textbox).setText(self.msg)
                self.getControl(self.titlebox).setLabel(self.title)
                w_id = str(xbmcgui.getCurrentWindowDialogId())
                x_ = 0
                while x_ < t and xbmc.getCondVisibility("Window.isVisible({})".format(w_id)) and not monitor.abortRequested():
                    x_ += 1
                    if monitor.waitForAbort(1):
                        sys.exit()
                self.close()
                
            def onAction(self,action):
                if   action == ACTION_PREVIOUS_MENU: self.close()
                elif action == ACTION_NAV_BACK: self.close()

        cw = MyWindow( dw , ADDONPATH, 'DefaultSkin', title=ADDONTITLE, fanart=FANART, image=image, msg='[B]'+msg+'[/B]', t=t)
        cw.doModal()
        del cw

def percentage(part, whole):
    return 100 * float(part)/float(whole)

def UpdatesStatus():
    request='{"jsonrpc":"2.0","method":"XBMC.GetInfoLabels","params":{"labels": ["System.AddonUpdateCount"] },"id":1}'
    response = xbmc.executeJSONRPC(request)
    response_result = json.loads(response)
    num = response_result['result']['System.AddonUpdateCount']
    return num

def updateprogress():
    xbmc.executebuiltin('ActivateWindow(2139)')
    progress('Παρακαλώ περιμένετε!', t=2)
    xbmc.executebuiltin('UpdateAddonRepos()')
    xbmc.executebuiltin('UpdateLocalAddons()')
    while not UpdatesStatus() >= '0':
        if monitor.waitForAbort(1):
            xbmc.executebuiltin('Dialog.Close(all,true)')
            sys.exit()
    totalupdates = int(UpdatesStatus())
    free_mem = int(re.sub(r'\D', '', xbmc.getInfoLabel('System.FreeMemory')))
    if UpdatesStatus() > '0':
        if free_mem > 200:
            xbmc.executebuiltin('Dialog.Close(all,true)')
            if monitor.waitForAbort(0.5):
                sys.exit()
            xbmc.executebuiltin('ActivateWindow(10040,"addons://outdated/")')
            if UpdatesStatus() > '0':
                progress('Υπάρχουν %s [CR]ενημερώσεις' % UpdatesStatus())
                dp.create('Ενημερώσεις προσθέτων', 'Διαθέσιμες %s ενημερώσεις' % UpdatesStatus())
            else:
                dp.create('Ενημερώσεις προσθέτων', 'Οι ενημερώσεις ολοκληρώθηκαν')
                if monitor.waitForAbort(2):
                    dp.close()
                    sys.exit()
                dp.close()
                if xbmc.getCondVisibility("Window.isVisible(10040)"):
                    # xbmc.executebuiltin('Dialog.Close(all,true)')
                    xbmc.executebuiltin('Action(Back)')
                if monitor.waitForAbort(0.5):
                    sys.exit()
                xbmc.executebuiltin('Dialog.Close(all,true)')
                xbmc.executebuiltin('ActivateWindow(10000)')
                xbmc.sleep(4000)
                xbmcgui.Dialog().notification("To Build φαίνεται ενημερωμένο...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/ok3.png', sound=False)
                xbmc.sleep(4000)
                xbmcgui.Dialog().notification("Για να δούμε τι θα  δούμε...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/thinking_face.png', sound=False)
                xbmc.sleep(4000)
                # xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"screensaver.atv4"},"id":"1"}')
                # xbmc.sleep(200)
                # xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "screensaver.atv4","enabled":true}}')
                return True
            Thread(target=progress_notification, daemon=True).start()
            if monitor.waitForAbort(2):
                dp.close()
                sys.exit()
            x = 0
            dismiss = 1080
            w_id = str(xbmcgui.getCurrentWindowDialogId())
            while not UpdatesStatus() == '0'  and x < dismiss and not monitor.abortRequested() and xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                x += 1
                msg1 = 'Εκκρεμούν %s ενημερώσεις - κλείνω σε %s' % (UpdatesStatus(), str(dismiss-x))
                msg2 = 'Επιστρέφετε με το πλήκτρο back - κλείνω σε %s' % str(dismiss-x)
                if (x % 2) == 0:
                    msg = msg1
                else:
                    msg = msg2
                updateperc = int(percentage(int(UpdatesStatus()), totalupdates))
                dp.update(updateperc, 'Ενημερώσεις προσθέτων', msg)
                if monitor.waitForAbort(1):
                    dp.close()
                    break
                    sys.exit()
            if UpdatesStatus() == '0':
                dp.update(0, 'Ενημερώσεις προσθέτων', 'Οι ενημερώσεις ολοκληρώθηκαν')
                if monitor.waitForAbort(2):
                    dp.close()
                    sys.exit()
                if xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                    xbmc.executebuiltin('Action(Back)')
                    if monitor.waitForAbort(0.5):
                        dp.close()
                        sys.exit()
                dp.close()
            elif x == 1080:
                dp.update(0, 'Ενημερώσεις προσθέτων', 'Λήξη χρόνου, οι ενημερώσεις δεν έχουν ολοκληρωθει')
                if monitor.waitForAbort(2):
                    dp.close()
                    sys.exit()
                if xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                    xbmc.executebuiltin('Action(Back)')
                    if monitor.waitForAbort(0.5):
                        dp.close()
                        sys.exit()
                dp.close()
            else:
                dp.update(0, 'Ενημερώσεις προσθέτων', 'Οι ενημερώσεις θα συνεχιστούν στο background')
                if not xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                    if monitor.waitForAbort(2):
                        dp.close()
                        sys.exit()
                    dp.close()
                    sys.exit()
                elif xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                    if monitor.waitForAbort(2):
                        dp.close()
                        sys.exit()
                    xbmc.executebuiltin('Action(Back)')
                    if monitor.waitForAbort(0.5):
                        dp.close()
                        sys.exit()
            if xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                xbmc.executebuiltin('Action(Back)')
                if monitor.waitForAbort(0.5):
                    sys.exit()
            if xbmc.getCondVisibility("Window.isVisible(10040)"):
                xbmc.executebuiltin('Action(Back)')
            if monitor.waitForAbort(0.5):
                sys.exit()
            xbmc.executebuiltin('Dialog.Close(all,true)')
            xbmc.executebuiltin('ActivateWindow(10000)')
            xbmc.sleep(4000)
            xbmcgui.Dialog().notification("To Build φαίνεται ενημερωμένο...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/ok3.png', sound=False)
            xbmc.sleep(4000)
            xbmcgui.Dialog().notification("Για να δούμε τι θα  δούμε...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/thinking_face.png', sound=False)
            xbmc.sleep(4000)
            # xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"screensaver.atv4"},"id":"1"}')
            # xbmc.sleep(200)
            # xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "screensaver.atv4","enabled":true}}')
            return True
    else:
        progress('Δεν υπάρχουν[CR]ενημερώσεις προσθέτων', t=2)
        xbmc.executebuiltin('Dialog.Close(all,true)')
        xbmc.sleep(2000)
        xbmcgui.Dialog().notification("To Build είναι ενημερωμένο...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/ok.gif', sound=False)
        xbmc.sleep(4000)
        xbmcgui.Dialog().notification("Καλή διασκέδαση!", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/hi.gif', sound=False)
        # xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"screensaver.atv4"},"id":"1"}')
        # xbmc.sleep(200)
        # xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "screensaver.atv4","enabled":true}}')
        return

def progress_notification():
    progress('Περιμένετε να ολοκληρωθούν[CR]οι ενημερώσεις προσθέτων', t=1620, dw='Progress2.xml')
    
if __name__ == '__main__':
    updateprogress()

###############################################################################################################################
# progress('Για μισό λεπτό...', t=5)
# xbmc.sleep(8000)


from xbmc import executebuiltin
from xbmcaddon import Addon
from os.path import exists,join
from os import makedirs
from xbmcvfs import translatePath


xbmcvfs.delete('special://home/addons/plugin.video.vnmedia/service.py')
xbmc.sleep(2000)

pack = translatePath('special://home/addons/packages')

if not exists(pack):
    makedirs(pack)
packfolders = 'packages'


                       #script.artistslideshow
base_path = xbmcvfs.translatePath('special://home/userdata/addon_data/script.artistslideshow')

dir_list = glob.iglob(os.path.join(base_path, "ArtistInformation"))
for path in dir_list:
    if os.path.isdir(path):
        shutil.rmtree(path)


base_path = xbmcvfs.translatePath('special://home/userdata/addon_data/script.artistslideshow')

dir_list = glob.iglob(os.path.join(base_path, "ArtistSlideshow"))
for path in dir_list:
    if os.path.isdir(path):
        shutil.rmtree(path)


                                 # temp
# base_path = xbmcvfs.translatePath('special://home/addons')

# dir_list = glob.iglob(os.path.join(base_path, "temp"))
# for path in dir_list:
    # if os.path.isdir(path):
        # shutil.rmtree(path)


# xbmc.executebuiltin('PlayMedia("plugin://plugin.video.sporthdme/?url=clear&mode=clear&name=%5BB%5D%5BCOLOR+gold%5DClear+Addon+Data%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=C%3A%5CPortableApps%5Ckodi%5Ckodi+World+21%5CKodi%5Cportable_data%5Caddons%5Cplugin.video.sporthdme%5Cicon.png&description=C%3A%5CPortableApps%5Ckodi%5Ckodi+World+21%5CKodi%5Cportable_data%5Caddons%5Cplugin.video.sporthdme%5Cfanart.jpg")")')
# xbmc.sleep(6000)
# xbmc.executebuiltin('PlayMedia("plugin://plugin.video.atlas/?url=&mode=9&name=%5BB%5D%5BCOLOR+white%5D%CE%95%CE%BA%CE%BA%CE%B1%CE%B8%CE%AC%CF%81%CE%B9%CF%83%CE%B7+Cache%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=https%3A%2F%2Fi.imgur.com%2F2cPUPkf.png&description=")')
# xbmc.sleep(5000)
# xbmc.executebuiltin('PlayMedia("plugin://plugin.video.microjen/clear_cache_silent")')
# xbmc.sleep(10000)
# xbmc.executebuiltin('PlayMedia("plugin://plugin.program.downloader19/?url=&mode=23&name=%5BB%5D%5BCOLOR+white%5D%CE%9A%CE%B1%CE%B8%CE%B1%CF%81%CE%B9%CF%83%CE%BC%CF%8C%CF%82+%CE%A0%CE%B1%CF%81%CF%8C%CF%87%CF%89%CE%BD%5B%2FCOLOR%5D%5B%2FB%5D&icon=special%3A%2F%2Fhome%2Faddons%2Fplugin.program.downloader19%2Fresources%2Fmedia%2FWorld.png&fanart=C%3A%5CPortableApps%5Ckodi%5Ckodi+World+21%5CKodi%5Cportable_data%5Caddons%5Cplugin.program.downloader19%5Cfanart.jpg&description=&name2=&version=")')
# xbmc.sleep(4000)
# xbmcgui.Dialog().notification("Εγώ ό,τι ήταν να κάνω το ΄κανα...", "[COLOR lime]good luck...[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/itsok.jpg', sound=True)


# UpdateAddonRepos()