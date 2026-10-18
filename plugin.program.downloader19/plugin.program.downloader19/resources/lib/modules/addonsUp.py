import os, xbmc, xbmcvfs, xbmcgui, xbmcaddon, shutil, glob

def addonsUp():        
        choice = xbmcgui.Dialog().yesno('[COLOR orange]Addons Up[/COLOR]', '[CR][B]Ελεγχος για ενημέρωση πρόσθετων.[/B][CR][CR]Για να συνεχίσετε πατήστε [B][COLOR green]Addons Up[/COLOR][/B] και περιμένετε...',
                                        nolabel='[B][COLOR white]Όχι τώρα...[/COLOR][/B]',yeslabel='[B][COLOR green]Addons Up[/COLOR][/B]')
                                        
        if choice == 1: [#xbmc.executebuiltin('installAddon()'),
                         #xbmc.sleep(1000),
                         #xbmc.executebuiltin('addonsEnable.enable_addons()'),

                         xbmc.executebuiltin('ActivateWindow(AddonBrowser,return)'),
                         #xbmc.sleep(2000),
                         #xbmc.executebuiltin('RunAddon()'),
                         xbmc.sleep(5000),
                         xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=fixaddonupdate)'),
                         xbmc.sleep(8000),
                         xbmc.executebuiltin('RunPlugin(plugin://plugin.program.G.K.N.Wizard/?mode=forceupdate)'),
                         xbmc.sleep(10000),
                         xbmc.executebuiltin('UpdateAddonRepos'),]
addonsUp()

