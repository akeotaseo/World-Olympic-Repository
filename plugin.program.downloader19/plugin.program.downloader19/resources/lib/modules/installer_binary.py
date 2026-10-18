import os, xbmc, xbmcgui
from updatervar import *

addon_path = translatePath('special://home/addons')

if xbmc.getCondVisibility('System.HasAddon({})'.format('vfs.sftp')):
    SFTP = '[B][COLOR=white]SFTP support [COLOR=lime](Εγκατεστημένο)[/COLOR][/B]'
else:
    SFTP = '[B][COLOR=white]SFTP support[/COLOR][/B]'

if xbmc.getCondVisibility('System.HasAddon({})'.format('vfs.rar')):
    RAR = '[B][COLOR=white]Rar archive support [COLOR=lime](Εγκατεστημένο)[/COLOR][/B]'
else:
    RAR = '[B][COLOR=white]Rar archive support[/COLOR][/B]'

if xbmc.getCondVisibility('System.HasAddon({})'.format('vfs.libarchive')):
    Archive = '[B][COLOR=white]Archive support [COLOR=lime](Εγκατεστημένο)[/COLOR][/B]'
else:
    Archive = '[B][COLOR=white]Archive support[/COLOR][/B]'

if xbmc.getCondVisibility('System.HasAddon({})'.format('inputstream.adaptive')):
    Inputstream = '[B][COLOR=white]Inputstream Adaptive [COLOR=lime](Εγκατεστημένο)[/COLOR][/B]'
else:
    Inputstream = '[B][COLOR=white]Inputstream Adaptive[/COLOR][/B]'

if xbmc.getCondVisibility('System.HasAddon({})'.format('inputstream.rtmp')):
    RTMP = '[B][COLOR=white]RTMP Input [COLOR=lime](Εγκατεστημένο)[/COLOR][/B]'
else:
    RTMP = '[B][COLOR=white]RTMP Input[/COLOR][/B]'

if xbmc.getCondVisibility('System.HasAddon({})'.format('inputstream.ffmpegdirect')):
    FFmpeg = '[B][COLOR=white]Inputstream FFmpeg Direct [COLOR=lime](Εγκατεστημένο)[/COLOR][/B]'
else:
    FFmpeg = '[B][COLOR=white]Inputstream FFmpeg Direct[/COLOR][/B]'

if xbmc.getCondVisibility('System.HasAddon({})'.format('visualization.spectrum')):
    Spectrum = '[B][COLOR=white]Spectrum [COLOR=lime](Εγκατεστημένο)[/COLOR][/B]'
else:
    Spectrum = '[B][COLOR=white]Spectrum[/COLOR][/B]'


def Installer_Binary_Addons():
    funcs = (action_1, action_2, action_3, action_4, action_5, action_6, action_7)
    selection = xbmcgui.Dialog().select('[B][COLOR=orange]Εγκατάσταση Binary Addons:[/COLOR][/B]', 
    [SFTP, RAR, Archive, Inputstream, RTMP, FFmpeg, Spectrum])

    if selection:
        if selection < 0:
            return 
        func = funcs[selection-7]
        return func()
    else:
        func = funcs[selection]
        return func()
    return 

def action_1():
    xbmc.executebuiltin('InstallAddon(vfs.sftp)')
    xbmc.sleep(100)
    xbmc.executebuiltin('SendClick(11)')
    dir_list = glob.iglob(os.path.join(addon_path, "vfs.sftp"))
    for path in dir_list:
        if os.path.exists(addon_path): xbmcgui.Dialog().notification("[B][COLOR orange]TechNEWSology Build[/COLOR][/B]", "[COLOR white]Το πρόσθετο είναι εγκατεστημένο![/COLOR]", icon_Build)

def action_2():
    xbmc.executebuiltin('InstallAddon(vfs.rar)')
    xbmc.sleep(100)
    xbmc.executebuiltin('SendClick(11)')
    dir_list = glob.iglob(os.path.join(addon_path, "vfs.rar"))
    for path in dir_list:
        if os.path.exists(addon_path): xbmcgui.Dialog().notification("[B][COLOR orange]TechNEWSology Build[/COLOR][/B]", "[COLOR white]Το πρόσθετο είναι εγκατεστημένο![/COLOR]", icon_Build)

def action_3():
    xbmc.executebuiltin('InstallAddon(vfs.libarchive)')
    xbmc.sleep(100)
    xbmc.executebuiltin('SendClick(11)')
    dir_list = glob.iglob(os.path.join(addon_path, "vfs.libarchive"))
    for path in dir_list:
        if os.path.exists(addon_path): xbmcgui.Dialog().notification("[B][COLOR orange]TechNEWSology Build[/COLOR][/B]", "[COLOR white]Το πρόσθετο είναι εγκατεστημένο![/COLOR]", icon_Build)

def action_4():
    xbmc.executebuiltin('InstallAddon(inputstream.adaptive)')
    xbmc.sleep(100)
    xbmc.executebuiltin('SendClick(11)')
    dir_list = glob.iglob(os.path.join(addon_path, "inputstream.adaptive"))
    for path in dir_list:
        if os.path.exists(addon_path): xbmcgui.Dialog().notification("[B][COLOR orange]TechNEWSology Build[/COLOR][/B]", "[COLOR white]Το πρόσθετο είναι εγκατεστημένο![/COLOR]", icon_Build)

def action_5():
    xbmc.executebuiltin('InstallAddon(inputstream.rtmp)')
    xbmc.sleep(100)
    xbmc.executebuiltin('SendClick(11)')
    dir_list = glob.iglob(os.path.join(addon_path, "inputstream.rtmp"))
    for path in dir_list:
        if os.path.exists(addon_path): xbmcgui.Dialog().notification("[B][COLOR orange]TechNEWSology Build[/COLOR][/B]", "[COLOR white]Το πρόσθετο είναι εγκατεστημένο![/COLOR]", icon_Build)

def action_6():
    xbmc.executebuiltin('InstallAddon(inputstream.ffmpegdirect)')
    xbmc.sleep(100)
    xbmc.executebuiltin('SendClick(11)')
    dir_list = glob.iglob(os.path.join(addon_path, "inputstream.ffmpegdirect"))
    for path in dir_list:
        if os.path.exists(addon_path): xbmcgui.Dialog().notification("[B][COLOR orange]TechNEWSology Build[/COLOR][/B]", "[COLOR white]Το πρόσθετο είναι εγκατεστημένο![/COLOR]", icon_Build)

def action_7():
    xbmc.executebuiltin('InstallAddon(visualization.spectrum)')
    xbmc.sleep(100)
    xbmc.executebuiltin('SendClick(11)')
    dir_list = glob.iglob(os.path.join(addon_path, "visualization.spectrum"))
    for path in dir_list:
        if os.path.exists(addon_path): xbmcgui.Dialog().notification("[B][COLOR orange]TechNEWSology Build[/COLOR][/B]", "[COLOR white]Το πρόσθετο είναι εγκατεστημένο![/COLOR]", icon_Build)

Installer_Binary_Addons()

