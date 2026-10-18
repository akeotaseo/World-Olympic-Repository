import xbmc, xbmcgui


def derbid_authorize():
    funcs = (action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8, action_9, action_10, action_11, action_12)
    selection = xbmcgui.Dialog().select('[B][COLOR=orange]Εξουσιοδότηση - Επαναφορά Derbid[/COLOR][/B]', 
['[B][COLOR=white][COLOR=lime]Authorize [COLOR=white]Real-Derbid[/COLOR][/B]',
 '[B][COLOR=white][COLOR=lime]Authorize [COLOR=white]AllDerbid[/COLOR][/B]',
 '[B][COLOR=white][COLOR=lime]Authorize [COLOR=white]Premiumize.me[/COLOR][/B]',
 '[B][COLOR=white][COLOR=lime]Authorize [COLOR=white]Debrid-Link.fr[/COLOR][/B]',
 '[B][COLOR=white][COLOR=lime]Authorize [COLOR=white]Link Snappy[/COLOR][/B]',
  '[B][COLOR=white][COLOR=lime]Authorize [COLOR=white]TorBox[/COLOR][/B]',
 '[B][COLOR=white][COLOR=orange]Reset [COLOR=white]Real-Debrid[/COLOR][/B]',
 '[B][COLOR=white][COLOR=orange]Reset [COLOR=white]AllDebrid[/COLOR][/B]',
 '[B][COLOR=white][COLOR=orange]Reset [COLOR=white]Premiumize.me[/COLOR][/B]',
 '[B][COLOR=white][COLOR=orange]Reset [COLOR=white]Debrid-Link.fr[/COLOR][/B]',
 '[B][COLOR=white][COLOR=orange]Reset [COLOR=white]Link Snappy[/COLOR][/B]',
 '[B][COLOR=white][COLOR=orange]Reset [COLOR=white]TorBox[/COLOR][/B]'])

    if selection:
        if selection < 0:
            return 
        func = funcs[selection-12]
        return func()
    else:
        func = funcs[selection]
        return func()
    return 

def action_1():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=auth_rd)')

def action_2():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=auth_ad)')

def action_3():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=auth_pm)')

def action_4():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=auth_dl)')

def action_5():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=auth_ls)')

def action_6():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=auth_tb)')

def action_7():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=reset_rd)')

def action_8():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=reset_ad)')

def action_9():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=reset_pm)')

def action_10():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=reset_dl)')

def action_11():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=reset_ls)')

def action_12():
    xbmc.executebuiltin('RunPlugin(plugin://script.module.resolveurl/?mode=reset_tb)')

derbid_authorize()
