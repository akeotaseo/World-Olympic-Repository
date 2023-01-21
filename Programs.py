import xbmc, xbmcgui


def programs():
    funcs = (click1, click2, click3, click4, click5, click6, click7, click8, click9, click10, click11, click12, click13, click14, click15, click16, click17)
    call = xbmcgui.Dialog().select('[B][COLOR=orange]  ~ Tools ~[/COLOR][/B]', 
    
['[B][COLOR=white][B][COLOR dodgerblue]GR[COLOR white]eco[COLOR dodgerblue]TM [COLOR white]Builds Wizard[/COLOR][/B]',
 '[B][COLOR=white][B][COLOR orange]World Updater - Tools[/COLOR][/B]',


 '[B][COLOR=white]Home Widget [B][COLOR=green]ON[/COLOR][/B] / [B][COLOR=red]OFF[/COLOR][/B]',
 '[B][COLOR=white]Txt / Graph [B][COLOR red] Skin[/COLOR][/B]',


 '[B][COLOR=white]Αυτόματη ενημέρωση του build [B][COLOR=green]ON[/COLOR][/B] / [B][COLOR=red]OFF[/COLOR][/B]',

 '[B][COLOR=white]Intro [B][COLOR=green]Enable[/COLOR][/B] / [B][COLOR=red]Disable[/COLOR][/B]',

 '[B][COLOR=white][B]Επαν-εκκίνηση [B][COLOR orange]World Updater - Tools[/COLOR][/B]',
 '[B][COLOR=white][B][COLOR grey]Fix build update [/COLOR][/B]',
 '[COLOR blue][B]Gui Fix [/B][/COLOR]',


 '[COLOR lightslategray][B]Resolveurl[/COLOR][/B]',

 '[COLOR white][B]SearchSubs [/B][/COLOR]',

 '[B]Delete All[COLOR pink] XXX[/COLOR] Addons[/B]',
 '[B]Install[COLOR purple] TheCrew[/COLOR] Peropsitory[/B]',
 
 
 '[COLOR yellow][B]Nemesisaio / EntertainMe [/COLOR][B]Fix [/B]',


 '[B][COLOR=white]Delete[/COLOR][/B]   temp',

 '[COLOR orange][B]Select Matrix[/B][/COLOR] - [COLOR red]Test[/COLOR]'
  #'[COLOR lightskyblue][B]Select Tools[/COLOR][/B]',
 ])


    if call:
        if call < 0:
            return
        func = funcs[call-17]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def click1():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.G.K.N.Wizard/)')

def click2():
    xbmc.executebuiltin('ActivateWindow(10001,plugin://plugin.program.downloader19/)')
    
def click3():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build//PY/Tools/HomeWidgetONOFF/HomeWidgetONOFF.py")')

def click4():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build//PY/skin/DialogTextGraph.py")')

def click5():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Tools/downloaderstartupOnOff/DialogEnableDisabledownloaderstartup.py")')

def click6():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/skin/Introonoff.py")')

def click7():
    xbmc.executebuiltin('RunScript("special://home/addons/plugin.program.downloader19/service.py")')

def click8():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/FixBuild.py")')

def click9():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Tools/guifix.py")')
    
def click10():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Tools/Resolveurl/SelectResolveurl.py")')

def click11():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Tools/SearchSubs.py")')

def click12():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/AddonsDelete/DialogDeleteAllXXXAddons.py")')

def click13():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Wolf/InstalTheCrewRepository.py")')

def click14():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Tools/StreamArmy.py")')

def click15():
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Tools/TempDelete/DialogeTemp_Delete.py")')

def click16():

    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build//PY/SelectMatrix/DialogSelectMatrix.py")')

def click17():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.autowidget/?group=28tools-28&mode=group&refresh&reload")')

programs()
