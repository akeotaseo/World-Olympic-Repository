import os, xbmc, xbmcgui, xbmcvfs
from updatervar import *

def skin_menu():
    funcs = (action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8, action_9)
    selection = xbmcgui.Dialog().select('[B][COLOR=orange]                                     Ρυθμίσεις Κελύφους[/COLOR][/B]', 
['[B][COLOR=white]Αλλαγή Ταπετσαρίας[/COLOR][/B]',
 '[B][COLOR=white]Απενεργοποίηση Widgets[/COLOR][/B]',
 '[B][COLOR=white]Επαναφορά Widgets[/COLOR][/B]',
 '[B][COLOR=white]Επαναφορά αρχικού μενού[/COLOR][/B]',
 '[B][COLOR=white]Επαναφορά προεπιλεγμένων ρυθμίσεων του Κελύφους[/COLOR][/B]',
 '[B][COLOR=white]Διάταξη Λίστας (Λεπτή-Κανονική)[/COLOR][/B]',
 '[B][COLOR=white]Κινούμενη Ταπετσαρία[/COLOR][/B]',
 '[B][COLOR=white]Submenu (Απόκρυψη-Εμφάνιση)[/COLOR][/B]',
 '[B][COLOR=white]Διαμόρφωση του Κεντρικού Μενού[/COLOR][/B]'])

    if selection:
        if selection < 0:
            return 
        func = funcs[selection-9]
        return func()
    else:
        func = funcs[selection]
        return func()
    return 

def action_1():
    xbmc.executebuiltin("Action(Close)")
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    xbmc.executebuiltin(Background_path)

def action_2():
    choice = xbmcgui.Dialog().yesno('[B][COLOR red]TechNEWSology[/COLOR][/B]', '[COLOR white]Με αυτή την επιλογή θα αφαιρεθούν τα widgets όλων των κατηγοριών. Αυτό θα έχει ως αποτέλεσμα μείωση κατανάλωσης της μνήμης στη συσκευή σας με όφελος γρηγορότερη εναλλαγή κατηγοριών και έναρξης του Build. [CR][CR][COLOR lime]Η διαφορά στην ταχύτητα θα είναι αισθητή !!![/COLOR][CR](Όταν το μενού αναβαθμίζεται, θα επιστρέφουν τα widgets και θα χρειάζεται να επαναλαμβάνετε την διαδικασία.)',
                                    nolabel='[COLOR red]Άκυρο[/COLOR]',yeslabel='[COLOR lime]Αφαίρεση Widgets[/COLOR]')

    if choice == 1: [xbmc.executebuiltin("Action(Close)"),xbmc.sleep(1000),xbmc.executebuiltin("Action(Close)"), xbmcvfs.delete('special://profile/addon_data/script.skinshortcuts/skin.TechNEWSology.properties'), xbmcvfs.delete('special://profile/addon_data/script.skinshortcuts/skin.TechNEWSology.hash'),
                     xbmc.sleep(1000), xbmc.executebuiltin(Backgrounds_Without_Widgets), xbmc.sleep(10000), xbmc.executebuiltin("ReloadSkin"), xbmc.sleep(5000),
                     xbmcgui.Dialog().ok("[COLOR lime]Αφαιρέθηκαν τα widgets με Επιτυχία ![/COLOR]", "[COLOR white]Αν επιθυμείτε την επαναφορά των widgets αλλά και την επιλογή Background, θα μεταβείτε στο επάνω μέρος Ρυθμίσεις Κελύφους με σύμβολο το πινέλο.[COLOR white][/COLOR]")]

def action_3():
    xbmc.executebuiltin("Action(Close)"),
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    xbmc.executebuiltin(Backgrounds_With_Widgets)
    xbmc.sleep(5000)
    xbmc.executebuiltin(skinshortcuts_menu)
    xbmc.sleep(10000)
    xbmc.executebuiltin("ReloadSkin()")

def action_4():
    xbmc.executebuiltin("Action(Close)"),
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    xbmc.executebuiltin(Backgrounds_With_Widgets)
    xbmc.sleep(5000)
    xbmc.executebuiltin(skinshortcuts_menu)
    xbmcgui.Dialog().notification("[B][COLOR orange]Επαναφόρτωση του προφίλ...[/COLOR][/B]",'[COLOR white]Πάγωμα εικόνας - Αναμονή προς ολοκλήρωση.[/COLOR]' , icon_Build)
    xbmc.sleep(10000)
    xbmc.executebuiltin("LoadProfile(Master user)")

def action_5():
    xbmcgui.Dialog().ok("[B][COLOR red]TechNEWSology[/COLOR][/B]", "[COLOR white]Πατώντας εντάξει στο παράθυρο που ακολουθεί, επιλέγουμε [COLOR lime]Εφαρμογή Fix[COLOR white][CR]για να πραγματοποιηθεί επαναφορά προεπιλεγμένων ρυθμίσεων του κελύφους.[/COLOR]")
    xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=install&name=TechNEWSology+-Matrix-&url=gui)')

def action_6():
    xbmc.executebuiltin("Action(Close)")
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    xbmc.executebuiltin('Skin.ToggleSetting(Enable.SlimList)')
    xbmcgui.Dialog().notification("[B][COLOR red]Πραγματοποιήθηκε[/COLOR][/B]",'[COLOR white]αλλαγή στην διάταξη της λίστας.[/COLOR]' , icon_Build)

def action_7():
    xbmc.executebuiltin("Action(Close)")
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    xbmc.executebuiltin('Skin.ToggleSetting(Enable.AnimatedBackgrounds)')
    xbmc.executebuiltin("ReloadSkin()")

def action_8():
    xbmc.executebuiltin("Action(Close)")
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    xbmc.executebuiltin('Skin.ToggleSetting(Enable.VisibleSubmenu)')
    xbmc.executebuiltin("ReloadSkin()")

def action_9():
    xbmc.executebuiltin('ActivateWindow(SkinSettings)')
    xbmcgui.Dialog().notification("[B][COLOR red]ΠΡΟΣΟΧΗ ![/COLOR][/B]",'[COLOR white] Μετά από κάθε αναβάθμιση στο μενού του skinshortcuts του Build, θα χάνεται οποιαδήποτε αλλαγή πραγματοποιείτε.[/COLOR]' , icon_Build)

skin_menu()
