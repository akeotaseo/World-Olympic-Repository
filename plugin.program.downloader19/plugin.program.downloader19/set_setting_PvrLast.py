import xbmc, xbmcgui

xbmcgui.Dialog().ok('[B][COLOR blue]PVR[/COLOR][/B]', 'Με αυτή την επιλογή τα Settings[CR]των [COLOR=blue]PVR Stalker[/COLOR] & [COLOR=cornflowerblue]IPTV Simple Client[/COLOR][CR]θα επενέλθουν στην τελευταία ενημέρωση.')
def PVR_LAST():
    choice = xbmcgui.Dialog().yesno('[B][COLOR blue]PVR[/COLOR][/B]', '[COLOR white]Θέλετε σίγουρα να επαναφέρετε τα Settings[CR]των [COLOR=blue]PVR Stalker[/COLOR] & [COLOR=cornflowerblue]IPTV Simple Client[/COLOR][CR]στην τελευταία ενημέρωση?[/COLOR]',
                                            nolabel='[COLOR white]Όχι[/COLOR]',yeslabel='[COLOR white]Ναι[/COLOR]')
    if choice == 1: service_Pvr_Last()



    # if choice == 0: xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloaderstartup/PY/skin/SkinMenuTools.py")')
xbmcgui.Dialog().notification("[B][COLOR blue]PVR[/COLOR][/B]", "Τελευταία Ενημέρωση...", icon='special://home/addons/plugin.program.downloader19/resources/media/FixBuild.png', sound=False)

from resources.lib.modules import check

from updatervar import *
def service_Pvr_Last():

    ##  plugin.program.downloader19   ###


    addon_downloader19       = xbmcaddon.Addon('plugin.program.downloader19')
    setting_downloader19     = addon_downloader19.getSetting
    setting_set_downloader19 = addon_downloader19.setSetting
    if not setting_downloader19('pvrversion')=='0':
        xbmc.executebuiltin('ActivateWindow(10000)')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')
        xbmc.sleep(1000)
        setting_set_downloader19('pvrversion', '0')
        xbmc.sleep(2000)
        xbmcgui.Dialog().notification("[B][COLOR orange]pvrversion[/COLOR][/B]", "[COLOR white]Παρακαλώ περιμένετε...[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/FixBuild.png', sound=False)
        xbmc.sleep(2000)




        xbmcgui.Dialog().notification("[B][COLOR orange]Ok...[/COLOR][/B]", "[COLOR white]Παρακαλώ περιμένετε...[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/FixBuild2.png')
        xbmc.sleep(2000)

    # xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/service Skin Up.py")')


    if __name__ == '__main__':
        if not setting('updaterversion') == 'false':
           # xbmcgui.Dialog().notification("[B][COLOR orange]Ελεγχος για ενημερώσεις[/COLOR][/B]", "...", icon='special://home/addons/plugin.program.downloader19/icon.gif', sound=False)

            check.pvr()

PVR_LAST()
