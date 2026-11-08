import xbmc, xbmcgui, xbmcvfs, sys, json, os, re, glob, shutil, subprocess
import time  # 👈 ΠΡΟΣΘΕΣΕ ΑΥΤΗ ΤΗ ΓΡΑΜΜΗ ΣΤΗΝ ΚΟΡΥΦΗ ΤΟΥ check.py!
from updatervar import *
from xml.dom.minidom import parse
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
# ----------------------------------------------------------------------
# 🎯 Ο ΕΞΥΠΝΟΣ ΕΛΕΓΧΟΣ ΑΝΑΜΟΝΗΣ ΠΟΥ ΣΥΖΗΤΗΣΑΜΕ
# ----------------------------------------------------------------------
def wait_for_kodi(label_name="Διαδικασία"):
    xbmc.sleep(1500) # Καθυστέρηση ασφαλείας για να γραφτούν τα locks
    xbmc.log(f"[Master_Build] Έναρξη ελέγχου background για: {label_name}", xbmc.LOGINFO)
    
    # Διαδρομές και των 3 αρχείων lock
    profile_dir = xbmcvfs.translatePath('special://home/userdata/addon_data/plugin.program.downloader19')
    DELETE_LOCK_FILE = os.path.join(profile_dir, 'delete_lock.txt')
    DATABASE_LOCK_FILE = os.path.join(profile_dir, 'database_lock.txt')
    INSTALL_LOCK_FILE = os.path.join(profile_dir, 'install_lock.txt')
    
    # 🛑 ΤΟ ΑΡΧΙΚΟ, ΤΡΙΠΛΟ ΧΕΙΡΟΦΡΕΝΟ ΜΑΣ
    while (
        # Έλεγχος αν τρέχει οποιοδήποτε από τα 3 κρίσια background βήματα
        os.path.exists(DELETE_LOCK_FILE) or 
        os.path.exists(DATABASE_LOCK_FILE) or
        os.path.exists(INSTALL_LOCK_FILE) or
        
        # Έλεγχος αν το Kodi είναι μπουκωμένο με παράθυρα συστήματος
        xbmc.getCondVisibility("Window.IsActive(busydialog)") or 
        xbmc.getCondVisibility("Window.IsActive(infodialog)") or
        xbmc.getCondVisibility("Window.IsActive(progressdialog)") or
        xbmc.getCondVisibility("Library.IsScanningVideo")
    ):
        xbmc.log(f"[Master_Build] ΠΡΟΣΟΧΗ: Ενεργό Lock ανιχνεύτηκε! Αναμονή 2 δευτερόλεπτα για το βήμα: {label_name}...", xbmc.LOGINFO)
        xbmc.sleep(2000) 
        
    xbmc.log(f"[Master_Build] [ΚΑΘΑΡΟ ΠΕΔΙΟ] Τα locks αφαιρέθηκαν. Προχωράμε στο: {label_name}", xbmc.LOGINFO)
    xbmc.sleep(1000)




# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ DELETE (The Smart Timing Shift)
# ----------------------------------------------------------------------
def delete():
	if delete_files_version > int(setting('deleteversion')):
		xbmcvfs.delete('special://home/userdata/addon_data/plugin.program.downloader19/delete_files.py')
		
		# 🚀 ΑΦΑΙΡΕΘΗΚΕ ΤΟ ΠΕΡΙΤΤΟ SLEEP ΑΠΟ ΕΔΩ - ΞΕΚΙΝΑΕΙ ΑΜΕΣΩΣ ΤΟ NOTIFY
		xbmc.executebuiltin(Delete_startup)
		
		# ⏳ INITIALIZATION DELAY: Δίνουμε 2 δευτερόλεπτα αναμονή για να προλάβει 
		# το delete_files.py να ξεκινήσει και να διαβάσει το 4αρι sleep του.
		xbmc.sleep(2000)
		
		BG.create(Dialog_U2, Dialog_U11)
		xbmc.sleep(3000)
		BG.update(33, Dialog_U2, Dialog_U11)
		xbmc.sleep(4000)
		BG.update(63, Dialog_U2, Dialog_U11)
		xbmc.sleep(4000)
		BG.update(100, Dialog_U2, Dialog_U10)
		xbmc.sleep(2000)
		
		# 🚀 Η εντολή που δίνει την εντολή για τις μαζικές διαγραφές καταλοίπων
		xbmc.executebuiltin(del_startup)
		
		# ⏳ RAM THREAD TIMEOUT (ΜΕΤΑΦΕΡΘΗΚΕ ΕΔΩ): Δίνουμε 3 δευτερόλεπτα χρόνο στη C++ Core 
		# να επεξεργαστεί τη διαγραφή και να καθαρίσει το memory buffer του κινητού/RAM!
		xbmc.sleep(3000)
		
		setting_set('deleteversion', str(delete_files_version))
		BG.update(100, Dialog_U12, Dialog_U2)
		xbmc.sleep(2000)
		BG.close()
		
		# 🔥 ΧΕΙΡΟΦΡΕΝΟ: Περιμένουμε να ολοκληρωθούν οι διαγραφές αρχείων στο background
		wait_for_kodi("Διαγραφή Αρχείων (Delete)")




# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ ZIP2 (Περιμένει να κάτσει η database και τα addons)
# ----------------------------------------------------------------------
def zip2():
    if zip2_version > int(setting('zip2version')):
        
        wait_for_kodi("Προετοιμασία Zip2 (Zip2 Pre-Check)")
            
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(1000)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(1000)
        
        xbmc.executebuiltin(Zip2_startup)
        xbmc.sleep(2000) 
        BG.update(25, Dialog_U12, 'Zip2')
        
        BG.update(25, Dialog_U12, Dialog_U3)
        setting_set('zip2version', str(zip2_version))
        
        BG.update(35, Dialog_U12, 'Γίνεται αποσυμπίεση αρχείων... (1/3)')
        xbmc.sleep(3000)
        BG.update(55, Dialog_U12, 'Γίνεται αντιγραφή αρχείων... (2/3)')
        xbmc.sleep(3000)
        BG.update(75, Dialog_U12, 'Παρακαλώ περιμένετε... (3/3)')
        xbmc.sleep(3000)

                # 🧼 ΔΙΟΡΘΩΜΕΝΟ LABEL: Τώρα λέει ακριβώς τι συμβαίνει εκείνη τη στιγμή!
        BG.update(85, Dialog_U12, 'Μαζική ενεργοποίηση προσθέτων...')

        
        xbmc.executebuiltin('UpdateLocalAddons')
        xbmc.sleep(2000) 
        
        # 🔥 ΕΔΩ ΕΙΝΑΙ Η ΑΛΛΑΓΗ: Καλούμε τη δική μας turbo συνάρτηση!
        turbo_enable_addons_zip2()
        xbmc.sleep(1000) 
        
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')
        
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False)
        BG.close()
        
        wait_for_kodi("Εγκατάσταση Zip2 Addons")




def installation():
    if addons_list_installation_version > int(setting('installationversion')):
        virtual_path = 'special://home/userdata/addon_data/plugin.program.downloader19/addons_list_installation.py'
        real_script_path = xbmcvfs.translatePath(virtual_path)
        script_dir = os.path.dirname(real_script_path)
        
        if os.path.exists(real_script_path):
            try: os.remove(real_script_path)
            except: pass
        xbmc.sleep(1000)
        
        BG.create(Dialog_U12, Dialog_U6)
        BG.update(20, Dialog_U12, 'Έναρξη διαδικασίας λήψης...')
        xbmc.sleep(1000)
        
        # Εκκίνηση λήψης του script
        xbmc.executebuiltin(Installation_startup)
        
        wait_launch = 0
        while not os.path.exists(real_script_path) and wait_launch < 5:
            xbmc.sleep(2000)
            wait_launch += 1
            
        BG.update(50, Dialog_U12, 'Ανάγνωση λίστας προσθέτων...')
        xbmc.sleep(500)

        if os.path.exists(real_script_path):
            # 🎯 ΚΛΕΙΔΩΝΟΥΜΕ ΤΗ VERSION ΠΡΙΝ ΤΗΝ ΕΚΤΕΛΕΣΗ
            setting_set('installationversion', str(addons_list_installation_version))
            
            # 🔄 DYNAMIC PYTHON IMPORT: Φορτώνουμε το script απευθείας στο ίδιο thread
            xbmc.log("[Master_Build] Φόρτωση addons_list_installation.py απευθείας στην Python...", xbmc.LOGINFO)
            try:
                if script_dir not in sys.path:
                    sys.path.append(script_dir)
                
                import addons_list_installation
                import importlib
                importlib.reload(addons_list_installation)
                
                # 🛑 Το thread παγώνει εδώ μέχρι να τελειώσουν όλες οι εγκαταστάσεις!
                addons_list_installation.check_addons_list()
                xbmc.log("[Master_Build] [OK] To addons_list_installation ολοκληρώθηκε επιτυχώς!", xbmc.LOGINFO)
            except Exception as e:
                xbmc.log(f"[Master_Build] Σφάλμα κατά το import του installation script: {str(e)}", xbmc.LOGERROR)
                
        BG.update(100, Dialog_U12, 'Η εγκατάσταση ολοκληρώθηκε!')
        xbmc.sleep(1000)
        BG.close()
        
        # 🎯 Προσθήκη wait_for_kodi για σιγουριά ότι το Kodi επεξεργάστηκε τα πάντα 
        # και έχει σβήσει το install_lock.txt πριν πάμε στο επόμενο βήμα του check.py
        wait_for_kodi("Ολοκλήρωση Εγκατάστασης Addons")



def var():
    if var_version > int(setting('varversion')):
        
        # 🎯 ΦΡΕΝΟ ΣΤΗΝ ΕΝΑΡΞΗ: Περιμένουμε να καθαρίσει το Kodi από προηγούμενες διαγραφές ή notify
        wait_for_kodi("Προετοιμασία Μεταβλητών (Var Pre-Check)")
        
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        
        # Εκτέλεση των startup scripts του skin
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
        
        # 🔄 Ανανέωση του Skin
        xbmc.executebuiltin("ReloadSkin()")
        
        # 🎯 ΦΡΕΝΟ ΣΤΟ ΤΕΛΟΣ: Περιμένουμε 3 δευτερόλεπτα να ολοκληρωθεί το ReloadSkin() 
        # και να ησυχάσει το Kodi πριν δώσουμε τη σκυτάλη στο check.delete()
        xbmc.sleep(3000)
        wait_for_kodi("Ανανέωση Skin (Var Reload)")







# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ PLAYERS (Περιμένει αν γίνει εγκατάσταση/ενημέρωση)
# ----------------------------------------------------------------------
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
        
        # 🔥 ΧΕΙΡΟΦΡΕΝΟ: Αναμονή για την εγκατάσταση των Core Players
        wait_for_kodi("Εγκατάσταση Players")


# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ ZIP1
# ----------------------------------------------------------------------
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
        
        # 🔥 ΧΕΙΡΟΦΡΕΝΟ: Αναμονή για την αποσυμπίεση του Zip1
        wait_for_kodi("Εγκατάσταση Zip1")


# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ ZIP3
# ----------------------------------------------------------------------
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
        
        # 🔥 ΧΕΙΡΟΦΡΕΝΟ: Αναμονή για τη μεταφορά αρχείων addon_data
        wait_for_kodi("Εγκατάσταση Zip3 (Addon Data)")


# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ ZIP4
# ----------------------------------------------------------------------
def zip4():
    if zip4_version > int(setting('zip4version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        xbmc.executebuiltin(Zip4_startup)
        xbmc.sleep(1000)
        BG.update(25, Dialog_U12, '[COLOR ornge]Zip 4[/COLOR]')
        xbmc.sleep(500)
        setting_set('zip4version', str(zip4_version))
        BG.update(55, Dialog_U12, '[COLOR ornge]Zip 4[/COLOR]')
        xbmc.sleep(200)
        BG.update(75, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        BG.update(100, Dialog_U12, Dialog_U9)
        xbmc.sleep(1000)
        BG.close()
        
        # 🔥 ΧΕΙΡΟΦΡΕΝΟ: Αναμονή για το Zip4
        wait_for_kodi("Εγκατάσταση Zip4")


# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ ZIP5
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ ZIP5 (Αλλάζει την τιμή και περιμένει να τελειώσει το background fix)
# ----------------------------------------------------------------------
def zip5():
    if zip5_version > int(setting('zip5version')):
        BG.create(Dialog_U12, Dialog_U2)
        BG.update(5, Dialog_U12, Dialog_U2)
        xbmc.sleep(200)
        BG.update(15, Dialog_U12, Dialog_U3)
        xbmc.sleep(200)
        
        # 🚀 Εκκίνηση του background script για τα fixes/updates των addons
        xbmc.executebuiltin(Zip5_startup)
        xbmc.sleep(1000)
        
        BG.update(25, Dialog_U12, Dialog_U3)
        xbmc.sleep(500)
        
        # 🎯 ΕΓΓΡΑΦΗ ΤΗΣ ΝΕΑΣ ΕΚΔΟΣΗΣ: Γράφεται κανονικά τώρα
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
        
        # 🔥 ΤΟ ΚΛΕΙΔΙ: Περιμένουμε να ολοκληρωθούν όλες οι χειροκίνητες διορθώσεις των addons
        # στο παρασκήνιο, ώστε να προλάβει το Kodi να αποθηκεύσει και τη νέα τιμή στα settings!
        wait_for_kodi("Χειροκίνητες Διορθώσεις Addons (Zip5)")



# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ PVR (Πολύ σημαντικό γιατί πειράζει clients και mac_list)
# ----------------------------------------------------------------------
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
        
        # 🔥 ΧΕΙΡΟΦΡΕΝΟ: Αναμονή για τη ρύθμιση των PVR Clients
        wait_for_kodi("Ρύθμιση PVR")


# ----------------------------------------------------------------------
# ΔΙΟΡΘΩΜΕΝΗ SETSETTING
# ----------------------------------------------------------------------
def setsetting():
    if set_setting_version > int(setting('setsettingversion')):
        xbmcvfs.delete('special://home/userdata/addon_data/plugin.program.downloader19/set_setting.py')
        xbmc.sleep(2000)
        xbmc.executebuiltin(SetSetting_startup )
        xbmc.sleep(5000)
        setting_set('setsettingversion', str(set_setting_version))
        xbmc.sleep(3000)
        xbmc.executebuiltin(set_setting_startup)
        
        # 🔥 ΧΕΙΡΟΦΡΕΝΟ: Αναμονή για την ολοκλήρωση του set_setting script
        wait_for_kodi("Ενημέρωση Ρυθμίσεων (SetSetting)")



def database():
    if addons_repos_version > int(setting('addonsreposversion')):
        
        # 🎯 ΦΡΕΝΟ ΣΤΗΝ ΕΝΑΡΞΗ: Μην αγγίζεις τη βάση αν το Kodi είναι απασχολημένο με προηγούμενα zip/addons
        wait_for_kodi("Προετοιμασία Βάσης Δεδομένων (Database Pre-Check)")
        
        xbmcvfs.delete('special://home/userdata/addon_data/plugin.program.downloader19/Database_Addons33.py')
        xbmc.sleep(4000)
        
        # 🚀 Εκκίνηση της λήψης των Repos
        xbmc.executebuiltin(AddonsRepos_startup)
        
        BG.create(Dialog_U8, Dialog_Database)
        xbmc.sleep(2000)
        BG.update(33, Dialog_U8, Dialog_Database)
        xbmc.sleep(2000)
        BG.update(63, Dialog_U12, Dialog_Database)
        xbmc.sleep(2000)
        BG.update(76, Dialog_U12, Dialog_Database)
        xbmc.sleep(2000)
        
        # Εκτέλεση του δικού σου database script [σε μορφή built-in]
        xbmc.executebuiltin(database_startup)
        xbmc.sleep(1500)
        
        # 🎯 Ενεργοποίηση των Repositories
        addonsEnable.enable_addons()
        
        BG.update(85, Dialog_U12, '[COLOR lime]enable_addons...[/COLOR]')
        xbmc.sleep(500)
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')
        setting_set('addonsreposversion', str(addons_repos_version))
        xbmc.sleep(2000)
        BG.update(100, Dialog_U1, '[B][COLOR red]Περιμένετε χωρίς να πατήσετε κάτι...[/COLOR][/B]')
        xbmc.sleep(2000)
        BG.update(100, Dialog_U1, '[B][COLOR cornflowerblue]Περιμένετε λίγο ακόμα...[/COLOR][/B]')
        xbmc.sleep(2000)
        BG.update(95, Dialog_U9, Dialog_U2)
        xbmc.sleep(2000)
        dialog.notification('[B][COLOR orange]Γίνεται έλεγχος![/COLOR][/B]', '[COLOR white]Παρακαλώ περιμένετε...[/COLOR]', icon_ok2, sound=False) 
        xbmc.sleep(2000)
        BG.close()
        
        # ----------------------------------------------------------------------
        # 🔥 ΤΟ ΣΩΣΤΟ ΧΕΙΡΟΦΡΕΝΟ ΣΤΟ ΤΕΛΟΣ: 
        # Περιμένουμε το database_lock.txt να σβηστεί από το Database_Addons33.py
        # ----------------------------------------------------------------------
        profile_dir = xbmcvfs.translatePath('special://home/userdata/addon_data/plugin.program.downloader19')
        DATABASE_LOCK_FILE = os.path.join(profile_dir, 'database_lock.txt')
        
        # Αν το Database_Addons33.py πρόλαβε και έφτιαξε το lock, περιμένουμε να το σβήσει
        while os.path.exists(DATABASE_LOCK_FILE):
            xbmc.log("[Master_Build] Το Database_Addons33.py επεξεργάζεται τη βάση (database_lock.txt ενεργό). Αναμονή 2 δευτερόλεπτα...", xbmc.LOGINFO)
            xbmc.sleep(2000)
            
        xbmc.log("[Master_Build] [ΚΑΘΑΡΟ ΠΕΔΙΟ] Η βάση δεδομένων ολοκληρώθηκε πλήρως!", xbmc.LOGINFO)
        xbmc.sleep(1000)
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
            BG.close() # 🟢 ΤΕΛΕΙΩΝΕΙ ΕΔΩ, ΟΠΩΣ ΠΑΛΙΑ!





# def xmlskin():
    # if not setting('xmlskinversion') == 'false':
        # if xmlskin_version > int(setting('xmlskinversion')):
            # xbmcvfs.delete('special://home/userdata/addon_data/skin.19MatrixWorld/settings.xml')
            # xbmc.sleep(500)
            # 🎯 Σωστό άνοιγμα του Progress Bar με τις δικές σου μεταβλητές
            # BG.create(Dialog_U12, Dialog_Xml_Skin)
            # BG.update(5, Dialog_U12, Dialog_Xml_Skin)
            # xbmc.sleep(500)
            # BG.update(15, Dialog_U12, Dialog_Xml_Skin)
            # xbmc.sleep(100)
            
            # 🚀 Εκκίνηση της λήψης του νέου βελτιστοποιημένου Zip
            # xbmc.log("[Master_Build] Έναρξη λήψης βελτιστοποιημένου XML Skin...", xbmc.LOGINFO)
            # xbmc.executebuiltin(XmlSkin_startup)
            
            # ⏳ ΤΟ ΕΞΥΠΝΟ ΧΡΟΝΟΜΕΤΡΗΜΕΝΟ ΦΡΕΝΟ (12 ΔΕΥΤΕΡΟΛΕΠΤΑ)
            # Κρατάμε σταθερά τις δικές σου μεταβλητές (Dialog_U12, Dialog_Xml_Skin) για να μην μπερδεύεται η οθόνη
            # for i in range(25, 81, 6):
                # BG.update(i, Dialog_U12, Dialog_Xml_Skin)
                # xbmc.sleep(1200) # 10 βήματα x 1.2 δευτερόλεπτα = 12 δευτερόλεπτα συνολική αναμονή
            
            # xbmc.log("[Master_Build] [OK] Ο χρόνος αναμονής ολοκληρώθηκε.", xbmc.LOGINFO)
            
            # 🎯 Κλείδωμα της έκδοσης στα settings
            # setting_set('xmlskinversion', str(xmlskin_version))
            # BG.update(100, Dialog_U12, 'Η μεταφορά μενού ολοκληρώθηκε.')
            # xbmc.sleep(5000)
            # BG.close()
            
            # xbmc.sleep(500)
            # user_choice = xbmcgui.Dialog().yesno(
                # '[B][COLOR cornflowerblue]Skin World[/COLOR][/B]', 
                # 'Οι αλλαγές στο [COLOR orange]HOME MENU[/COLOR] θα εμφανιστούν στην επόμενη εκκίνηση του build.[CR]Θέλετε να κλείσετε το Kodi τώρα;'
            # )
            
            # if user_choice:
                # xbmc.log("[Master_Build] Ο χρήστης επέλεξε άμεσο κλείσιμο. Ακαριαίο os._exit...", xbmc.LOGINFO)
                # os._exit(1)
                # return False 
            # else:
                # xbmc.log("[Master_Build] Ο χρήστης πάτησε ΟΧΙ. Επιστροφή True για συνέχεια ροής.", xbmc.LOGINFO)
                # xbmcgui.Dialog().notification('[B][COLOR orange]Skin World[/COLOR][/B]', 'Οι αλλαγές θα εφαρμοστούν στο επόμενο boot!', icon_Build, sound=False)
                # xbmc.sleep(2000)
                # return True # 👈 Πράσινο φως για να τρέξει το UpdateAddonRepos()
                
    # return True # Αν δεν υπήρχε update, επιστρέφει True για να γίνουν κανονικά τα υπόλοιπα updates προσθέτων


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




# ----------------------------------------------------------------------
# 🎯 ΕΝΙΑΙΟ DEF: ΟΛΟΙ ΟΙ ΚΑΘΑΡΙΣΜΟΙ ΚΑΙ ΤΑ FIXES ΣΕ ΣΕΙΡΑ (ΜΕ ΧΕΙΡΟΦΡΕΝΟ)
# ----------------------------------------------------------------------
def run_pre_update_fixes():
    xbmc.log("[Master_Build] Έναρξη run_pre_update_fixes...", xbmc.LOGINFO)

    # === [ΜΕΡΟΣ Α: ΟΙ ΚΑΘΑΡΙΣΜΟΙ (Πρώην clean_house)] ===
    try:
        # Διαγραφή cache του MyIPTV
        xbmcvfs.delete('special://home/userdata/addon_data/plugin.video.myiptv/cache.db')
        
        # Αφαίρεση service του vnmedia αν υπάρχει
        vn_service = xbmcvfs.translatePath('special://home/addons/plugin.video.vnmedia/service.py')
        if os.path.exists(vn_service):
            try: os.remove(vn_service)
            except: pass

        # Καθαρισμός Artist Slideshow που βαραίνει τη RAM
        base_path = xbmcvfs.translatePath('special://home/userdata/addon_data/script.artistslideshow')
        for folder_name in ["ArtistInformation", "ArtistSlideshow"]:
            target_path = os.path.join(base_path, folder_name)
            if os.path.exists(target_path) and os.path.isdir(target_path):
                try: shutil.rmtree(target_path)
                except: pass
                
        xbmc.log("[Master_Build] Οι αρχικοί καθαρισμοί ολοκληρώθηκαν επιτυχώς.", xbmc.LOGINFO)
        xbmc.sleep(500)
    except Exception as e:
        xbmc.log(f"[Master_Build] Σφάλμα στους αρχικούς καθαρισμούς: {str(e)}", xbmc.LOGERROR)


    # === [ΜΕΡΟΣ Β: ΤΑ FIXES ΣΟΥ (100% ΑΠΑΡΑΛΛΑΚΤΑ ΜΕ ΤΙΣ ΔΙΕΣΕΙΣ ΤΟΥΣ)] ===

    """ fix1. Απενεργοποίηση του Πρόσθετου --->   The Loop    """
    # try:
    #     xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix1.py")')
    # except: pass
    # xbmc.sleep(500)

    """ fix2. Απενεργοποίηση service --->   plugin.video.the-loop: "8.3"  &  plugin.video.madtitansports: "2.0.45"     """
    # try:
    #     xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix2.py")')
    # except: pass
    # xbmc.sleep(500)

    """ fix2_on. Ενεργοποίηση service --->   plugin.video.the-loop:   &  plugin.video.madtitansports:     """
    try:
        xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix2_on.py")')
    except: pass
    xbmc.sleep(500)

    """ fix3. Διαγραφή του Πρόσθετου --->   plugin.video.whiskeyblues     """ 
    # try:
    #     xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix3.py")')
    # except: pass
    # xbmc.sleep(2000)

    """ fix4. Διαγραφή του Πρόσθετου --->   plugin.video.AliveGR  έκδοση "2.99.99" (και κάτω)     """
    # try:
    #     xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix4.py")')
    # except: pass
    # xbmc.sleep(2000)

    """ fix5. Διαγραφή settings του Πρόσθετου --->   plugin.video.themoviedb.helper  ( <setting id="language">12</setting> )     """
    try:
        xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix5.py")')
    except: pass
    xbmc.sleep(500)

    """ fix6. Διαγραφή settings του Πρόσθετου --->   plugin.video.atlas     """
    try:
        xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix6.py")')
    except: pass
    xbmc.sleep(500)

    """ fix7. Διαγραφή/Ρυθμίσεις settings του Πρόσθετου --->   weather.gismeteo     """
    try:
        xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/Fixes/fix7.py")')
    except: pass
    xbmc.sleep(500)


    xbmc.log("[Master_Build] [OK] Και τα Pre-Update Fixes ολοκληρώθηκαν!", xbmc.LOGINFO)

    # 🛑 ΤΟ ΑΠΑΡΑΒΑΤΟ ΧΕΙΡΟΦΡΕΝΟ:
    # Παγώνει το thread και περιμένει να κάτσουν όλες οι αλλαγές των settings, 
    # οι διαγραφές και τα background tasks, ΠΡΙΝ προχωρήσει η ροή στα επόμενα βήματα!
    wait_for_kodi("Αρχικοί Καθαρισμοί & Ρυθμίσεις Fixes")


    # Αστραπιαίο τελικό σκούπισμα της cache του MyIPTV
    xbmcvfs.delete('special://home/userdata/addon_data/plugin.video.myiptv/cache.db')



# ----------------------------------------------------------------------
# ⚙️ Η ΚΕΝΤΡΙΚΗ ΣΥΝΑΡΤΗΣΗ ΕΝΗΜΕΡΩΣΕΩΝ (ΑΚΡΙΒΩΣ ΑΠΟ ΚΑΤΩ)
# ----------------------------------------------------------------------
def UpdateAddonRepos():
    xbmc.sleep(200)
    
    # 🛡️ 1. 🎯 ΔΙΚΛΕΙΔΑ ΑΣΦΑΛΕΙΑΣ: Εκτελείται ο καθαρισμός και τα fixes από το check.py 
    # πρώτη-πρώτη, και το thread παγώνει εκεί με το wait_for_kodi μέχρι να ολοκληρωθούν όλα!
    run_pre_update_fixes()

    # ⚙️ 2. Μόλις λυθεί το χειρόφρενο, γυρνάει ο διακόπτης του Kodi Core
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')

    xbmc.sleep(200)
    xbmcgui.Dialog().notification("Add-ons Updates...", "[COLOR green]Enable[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/auto5.png', sound=False)
    xbmc.sleep(2000)
    xbmcgui.Dialog().notification("Check...", "Ελεγχος για ενημερώσεις προσθέτων", icon='special://home/addons/plugin.program.downloader19/resources/media/auto3.png', sound=False)
    xbmc.sleep(2000)
    xbmc.log("[Master_Build] Έλεγχος background διεργασιών πριν το UpdateAddonRepos...", xbmc.LOGINFO)
    
    # 🎯 Τελικός έλεγχος για να σιγουρευτούμε ότι δεν ξέμεινε τίποτα
    wait_for_kodi("Τελικός Έλεγχος Updater")

    while xbmc.getCondVisibility('Window.IsActive(yesnodialog)') or xbmc.getCondVisibility('Window.IsActive(progressdialog)'):
        xbmc.sleep(1000)
        
    xbmc.log("[Master_Build] [RELEASE] Όλα καθαρά! Εκκίνηση του Updater.", xbmc.LOGINFO)
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/addonupdatesprog.py")')
    xbmc.sleep(20000)
    Backup_Skin_Set()
    Backup_Home_Set()



def turbo_enable_addons_zip2():
    import sqlite3
    xbmc.log("[Master_Build] Έναρξη turbo ενεργοποίησης προσθέτων για το Zip2...", xbmc.LOGINFO)
    
    addons_path = xbmcvfs.translatePath('special://home/addons')
    addons_db = xbmcvfs.translatePath('special://database/Addons33.db')
    
    addon_xmls = []
    for name in glob.glob(os.path.join(addons_path,'*/addon.xml')):
        addon_xmls.append(name)
    addon_xmls.sort()
    
    addon_ids = []
    for xml in addon_xmls:
        try:
            root = parse(xml) # ⚠️ Αν σου βγάλει error εδώ στο parse, άλλαξέ το σε: from xml.dom.minidom import parse
            tag = root.documentElement
            _id = tag.getAttribute('id')
            addon_ids.append(_id)
        except:
            pass
            
    disabled = []
    for x in addon_ids:
        try:
            xbmcaddon.Addon(id = x)
        except:
            disabled.append(x)
            
    if not disabled:
        return

    try:
        conn = sqlite3.connect(addons_db)
        c = conn.cursor()
        c.execute("PRAGMA synchronous = OFF")
        c.execute("PRAGMA journal_mode = MEMORY")
        
        # Παίρνουμε τη σημερινή ημερομηνία για το installDate
        from datetime import datetime
        installed_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        for y in disabled:
            try:
                c.execute("SELECT id FROM installed WHERE addonID = ?", (y,))
                if c.fetchone() is None:
                    c.execute('INSERT INTO installed (addonID, enabled, installDate) VALUES (?,?,?)', (y, '1', installed_date))
                else:
                    c.execute('UPDATE installed SET enabled = 1 WHERE addonID = ?', (y,))
            except:
                pass
                
        conn.commit()
        conn.close()
    except Exception as e:
        xbmc.log(f'[Master_Build] SQL Error στο Zip2: {str(e)}', xbmc.LOGERROR)


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

