# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcvfs, sys, json, os, re, glob, shutil, xbmcaddon
from threading import Thread
# 🟢 Ο ΑΥΘΕΝΤΙΚΟΣ ΣΟΥ ΚΩΔΙΚΑΣ (100% ΚΑΘΑΡΟΣ & ΕΛΑΦΡΥΣ)
xbmc.sleep(200)


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
    # 🚀 1. Ανοίγουμε το επίσημο παράθυρο των ενημερώσεων
    xbmc.executebuiltin('ActivateWindow(2139)')
    progress('Παρακαλώ περιμένετε!', t=2)
    # 2. Ενημερώνουμε τα Repositories και τα τοπικά πρόσθετα
    xbmc.executebuiltin('UpdateAddonRepos')   
    xbmc.executebuiltin('UpdateLocalAddons')  
    
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

            # 🚀 Ανοίγουμε το παράθυρο των ξεπερασμένων πρόσθετων
            xbmc.executebuiltin('ActivateWindow(10040,"addons://outdated/")')
            
            # ⏱️ DYNAMIC WAIT LOCK (CHECKMATE V2):
            waiting_time = 0
            while not xbmc.getCondVisibility('Window.IsActive(10040)'):
                xbmc.sleep(100)
                waiting_time += 100
                if waiting_time >= 5000:
                    xbmc.log("[Master_Build] Το παράθυρο 10040 δεν άνοιξε ποτέ. Timeout.", xbmc.LOGWARNING)
                    break
                    
            if xbmc.getCondVisibility('Window.IsActive(10040)'):
                xbmc.sleep(600)
                
                # 🎯 ΚΛΕΙΔΩΝΟΥΜΕ ΤΟ FOCUS ΣΤΗ ΛΙΣΤΑ (ID: 50) ΠΡΙΝ ΤΑ ACTIONS
                xbmc.executebuiltin('Control.SetFocus(50)')
                xbmc.sleep(150)
                
                try:
                    current_updates = int(UpdatesStatus())
                except:
                    current_updates = 0
                    
                if current_updates > 5:
                    xbmc.log(f"[Master_Build] Βρέθηκαν {current_updates} ενημερώσεις (>5). Εκτέλεση Click Bypass.", xbmc.LOGINFO)
                    xbmc.executebuiltin('Action(Down)')
                    xbmc.sleep(250)
                    xbmc.executebuiltin('Action(Select)')
                    xbmc.sleep(500)
                else:
                    xbmc.log(f"[Master_Build] Βρέθηκαν {current_updates} ενημερώσεις (<=3). Παράκαμψη Click Bypass.", xbmc.LOGINFO)

            # 🚀 ΑΦΗΝΟΥΜΕ ΤΑ PROGRESS ΝΑ ΕΜΦΑΝΙΣΤΟΥΝ ΕΛΕΥΘΕΡΑ
            if UpdatesStatus() > '0':
                progress('Υπάρχουν %s [CR]ενημερώσεις' % UpdatesStatus())
                dp.create('Ενημερώσεις προσθέτων', 'Διαθέσιμες %s ενημερώσεις' % UpdatesStatus())
                Thread(target=progress_notification, daemon=True).start()
            else:
                dp.create('Ενημερώσεις προσθέτων', 'Οι ενημερώσεις ολοκληρώθηκαν')
                if monitor.waitForAbort(2):
                    dp.close()
                    sys.exit()
                dp.close()
                
                # 🎯 1η ΚΑΘΥΣΤΕΡΗΣΗ (ΕΞΥΠΝΟ ΦΡΕΝΟ)
                while xbmc.getCondVisibility('Window.IsActive(notification)'):
                    xbmc.sleep(500)
                    if monitor.waitForAbort(0.5):
                        sys.exit()
                        
                if xbmc.getCondVisibility("Window.isVisible(10040)"):
                    xbmc.executebuiltin('Action(Back)')
                    
                if monitor.waitForAbort(0.5):
                    sys.exit()
                    
                # 🎯 2η ΚΑΘΥΣΤΕΡΗΣΗ (ΕΞΥΠΝΟ ΦΡΕΝΟ)
                while xbmc.getCondVisibility('Window.IsActive(notification)'):
                    xbmc.sleep(500)
                    if monitor.waitForAbort(0.5):
                        sys.exit()
                        
                xbmc.executebuiltin('Dialog.Close(all,true)')
                xbmc.executebuiltin('ActivateWindow(10000)')
                xbmc.sleep(4000)
                xbmcgui.Dialog().notification("To Build φαίνεται ενημερωμένο...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/ok3.png', sound=False)
                xbmc.sleep(4000)
                xbmcgui.Dialog().notification("Για να δούμε τι θα  δούμε...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/thinking_face.png', sound=False)
                xbmc.sleep(4000)
                return True

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
            
            # 🎯 ΕΔΩ ΕΙΝΑΙ ΤΟ ΣΗΜΕΙΟ ΤΗΣ ΕΙΚΟΝΑΣ ΣΟΥ: Τακτοποιημένο και καθαρό
            if UpdatesStatus() == '0':
                dp.update(0, 'Ενημερώσεις προσθέτων', 'Οι ενημερώσεις ολοκληρώθηκαν')
                if monitor.waitForAbort(4):
                    dp.close()
                    sys.exit()
                dp.close()
                
                # 🎯 [ΤΟ ΕΞΥΠΝΟ ΦΡΕΝΟ ΣΤΟ LOOP]
                xbmc.log("[Master_Build] (Loop End) Αναμονή για ολοκλήρωση ειδοποιήσεων πρόσθετων...", xbmc.LOGINFO)
                while xbmc.getCondVisibility('Window.IsActive(notification)'):
                    xbmc.sleep(500)
                    if monitor.waitForAbort(0.5):
                        sys.exit()

                if xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                    xbmc.executebuiltin('Action(Back)')
                    if monitor.waitForAbort(0.5):
                        sys.exit()
            elif x == 1080:
                dp.update(0, 'Ενημερώσεις προσθέτων', 'Λήξη χρόνου, οι ενημερώσεις δεν έχουν ολοκληρωθει')
                if monitor.waitForAbort(2):
                    dp.close()
                    sys.exit()
                if xbmc.getCondVisibility("Window.isVisible({})".format(w_id)):
                    xbmc.executebuiltin('Action(Back)')
                    if monitor.waitForAbort(0.5):
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
                        sys.exit()
                        
            # 🎯 [ΕΞΥΠΝΟ ΦΡΕΝΟ ΠΡΙΝ ΤΗΝ ΤΕΛΙΚΗ ΕΞΟΔΟ]
            while xbmc.getCondVisibility('Window.IsActive(notification)'):
                xbmc.sleep(500)
                if monitor.waitForAbort(0.5):
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
            return True
    else:
        progress('Δεν υπάρχουν[CR]ενημερώσεις προσθέτων', t=2)
        xbmc.executebuiltin('Dialog.Close(all,true)')
        xbmc.sleep(4000)
        xbmcgui.Dialog().notification("To Build είναι ενημερωμένο...", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/ok.gif', sound=False)
        xbmc.sleep(4000)
        xbmcgui.Dialog().notification("Καλή διασκέδαση!", "   ", icon='special://home/addons/plugin.program.downloader19/resources/media/hi.gif', sound=False)
        xbmc.sleep(4000)
        return False

def progress_notification():
	progress('Περιμένετε να ολοκληρωθούν[CR]οι ενημερώσεις προσθέτων', t=1080, dw='Progress2.xml')


# 🔥 ΤΟ ΝΕΟ ΘΩΡΑΚΙΣΜΕΝΟ ENTRY POINT
if __name__ == '__main__':


	updateprogress()
	


	# 🔒  ΣΤΟ ΤΕΛΟΣ: ΕΠΑΝΑΦΟΡΑ ΜΟΝΟ ΤΟΥ SCREENSAVER
	try:
		p_dir = xbmcvfs.translatePath('special://home/userdata/addon_data/plugin.program.downloader19')
		b_file = os.path.join(p_dir, 'screensaver_backup.txt')
		
		if os.path.exists(b_file):
			with open(b_file, 'r', encoding='utf-8') as f:
				saved_ss = f.read().strip()
			
			if not saved_ss: 
				saved_ss = "screensaver.xbmc.builtin.dim"
				
			req_res = '{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"' + saved_ss + '"},"id":1}'
			xbmc.executeJSONRPC(req_res)
			os.remove(b_file)
			xbmc.log(f"[Master_Build] Ο screensaver επαναφέρθηκε επιτυχώς στο: {saved_ss}", xbmc.LOGINFO)
		else:
			xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"screensaver.mode","value":"screensaver.xbmc.builtin.dim"},"id":1}')
			xbmc.log("[Master_Build] Δεν βρέθηκε αρχείο backup. Ενεργοποίηση fallback screensaver (dim).", xbmc.LOGINFO)
	except Exception as e:
		xbmc.log(f"[Master_Build] Αποτυχία επαναφοράς screensaver στο τέλος: {str(e)}", xbmc.LOGERROR)
