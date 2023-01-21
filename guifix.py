import xbmc, xbmcgui


def guifix():
    funcs = (click_1, click_2)
    call = xbmcgui.Dialog().select('[B][COLOR=orange]Gui fix0[/COLOR][/B]', 
['[COLOR=white]Gui fix [COLOR=green](Matrix)[/COLOR]',
 '[COLOR=white]Gui fix [COLOR=purple](Nexus)[/COLOR]'])



    if call:
        if call < 0:
            return
        func = funcs[call-2]
        return func()
    else:
        func = funcs[call]
        return func()
    return 0



def click_1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.program.G.K.N.Wizard/?mode=install&name=World+-Matrix-&url=gui")')

def click_2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.program.G.K.N.Wizard/?mode=install&name=World+-Nexus-&url=gui")')

guifix()
