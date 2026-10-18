import os, sys, db, xbmc, sqlite3, glob, xbmcgui

# xbmc.executebuiltin('PlayMedia("plugin://plugin.program.G.K.N.Wizard/?mode=fixaddonupdate")')

# xbmcgui.Dialog().notification("Database", "Addons33", icon='special://home/addons/plugin.program.downloader19/resources/media/database.webp', sound=False)

from updatervar import *
from xbmcaddon import Addon
from xbmcvfs import translatePath
from xbmcgui import Dialog
from xbmc import log
from datetime import datetime
from xml.dom.minidom import parse

addon_xmls = []

BG = xbmcgui.DialogProgressBG()
addon_id        = 'plugin.program.downloader19'
addon           = xbmcaddon.Addon(addon_id)
addoninfo       = addon.getAddonInfo
ADDON_NAME      = addoninfo('name')
#ADDON_NAME = Addon().getAddonInfo('name')
DB_FOLDER = translatePath('special://database')
ADDONS_DB = os.path.join(DB_FOLDER, 'Addons33.db')
OK_DIALOG = Dialog().ok
YES_NO_DIALOG = Dialog().yesno

Database_Addons33 = [('repository.World', 'repository.World'),
                     ('repository.Worldolympic', 'repository.World'),
                     ('repository.Worldrepo', 'repository.World'),
                     ('repository.WorldNexus', 'repository.World'),
                     ('repository.WorldOmega', 'repository.World'),


                     ]


def enable_addons():
    for name in glob.glob(os.path.join(addons_path,'*/addon.xml')):
        addon_xmls.append(name)
    addon_xmls.sort()
    addon_ids =[]
    for xml in addon_xmls:
        try:
            root = parse(xml)
            tag = root.documentElement
            _id = tag.getAttribute('id')
            addon_ids.append(_id)
        except:
            pass
    enabled=[]
    disabled=[]
    for x in addon_ids:
        try:
            xbmcaddon.Addon(id = x)
            enabled.append(x)
        except:
            disabled.append(x)
    for y in disabled:
        try:
            enable_db(y)
        except:
            pass
    # xbmc.executebuiltin('UpdateLocalAddons')
    # xbmc.executebuiltin('UpdateAddonRepos')
    # xbmc.sleep(500)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.stalker","enabled":false}}')
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')

def enable_db(d_addon):
    """ create a database connection to a SQLite database """
    conn = None
    conn = sqlite3.connect(addons_db)
    c = conn.cursor()
    try:
        c.execute("SELECT id, addonID, enabled FROM installed WHERE addonID = ?", (d_addon,))
        found = c.fetchone()
        if found == None:
            # Insert a row of data
            c.execute('INSERT INTO installed (addonID , enabled, installDate) VALUES (?,?,?)', (d_addon, '1', installed_date))
        else:
            c.execute('UPDATE installed SET enabled = ? WHERE addonID = ? ', (1, d_addon,))
    except Exception as e:
        log('Failed to enable %s. Reason: %s' % (d_addon, e), xbmc.LOGINFO)
    conn.commit()
    conn.close()


def addon_database():
    db.addon_database(Database_Addons33, 1, True)
    try:
        con = sqlite3.connect(ADDONS_DB)
        cursor = con.cursor()
        # cursor.execute('DELETE FROM addonlinkrepo;',)
        # cursor.execute('DELETE FROM addons;',)
        cursor.execute('DELETE FROM package;',)
        # cursor.execute('DELETE FROM repo;',)
        cursor.execute('DELETE FROM update_rules;',)
        # cursor.execute('DELETE FROM version;',)
        con.commit()
    except sqlite3.Error as e:
        xbmc.log(f'{ADDON_NAME}: There was an error reading the database - {e}', xbmc.LOGINFO)
        return ''
    finally:
        try:
            if con:
                con.close()
        except UnboundLocalError as e:
            xbmc.log(f'{ADDON_NAME}: There was an error connecting to the database - {e}', xbmc.LOGINFO)
################################
    # BG.create('[B]\u0391\u03bd\u03b1\u03bc\u03bf\u03bd\u03ae \u03b3\u03b9\u03b1 \u03bf\u03bb\u03bf\u03ba\u03bb\u03ae\u03c1\u03c9\u03c3\u03b7 \u03b5\u03bd\u03b7\u03bc\u03ad\u03c1\u03c9\u03c3\u03b7\u03c2[/B]', '\u0394\u03b9\u03cc\u03c1\u03b8\u03c9\u03c3\u03b7 repository.redwizard \u03c3\u03c4\u03b7\u03bd Database - Addons33.db ...')
    # xbmc.sleep(5000)
    # BG.update(78, '[B]\u0391\u03bd\u03b1\u03bc\u03bf\u03bd\u03ae \u03b3\u03b9\u03b1 \u03bf\u03bb\u03bf\u03ba\u03bb\u03ae\u03c1\u03c9\u03c3\u03b7 \u03b5\u03bd\u03b7\u03bc\u03ad\u03c1\u03c9\u03c3\u03b7\u03c2[/B]', '\u0394\u03b9\u03cc\u03c1\u03b8\u03c9\u03c3\u03b7 repository.redwizard \u03c3\u03c4\u03b7\u03bd Database - Addons33.db ...')
    # xbmc.sleep(8000)
    # BG.close(
################################
    try:
        con = sqlite3.connect(ADDONS_DB)
        cursor = con.cursor()
        cursor.execute('VACUUM;',)
        con.commit()
    except sqlite3.Error as e:
        xbmc.log(f"Failed to vacuum data from the sqlite table: {e}", xbmc.LOGINFO)
    finally:
        try:
            if con:
                con.close()
        except sqlite3.Error:
            pass


addon_database()


# xbmc.sleep(1000)
# xbmcgui.Dialog().notification("Database", "[COLOR cornflowerblue]Addons33[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/database.webp', sound=False)
xbmc.sleep(1000)
# Official repositories only (default)
# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"addons.updatemode","value":0}}')
# Any repositories
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"addons.updatemode","value":1}')




# xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')
# xbmcgui.Dialog().notification("Add-ons Updates...", "[COLOR green]ON[/COLOR]", icon='special://home/addons/plugin.program.downloader19/resources/media/auto4.png', sound=False)
# xbmc.sleep(20000)
# xbmc.executebuiltin('UpdateLocalAddons()')
# xbmc.executebuiltin('UpdateAddonRepos()')
# xbmc.executebuiltin('ActivateWindow(AddonBrowser)')


# Tk
# xbmc.sleep(50000)
# enable_addons()
# xbmc.sleep(10000)
# xbmc.executebuiltin('PlayMedia("plugin://plugin.program.G.K.N.Wizard/?mode=forceupdate")')
# xbmc.sleep(20000)
# xbmc.executebuiltin('PlayMedia("plugin://plugin.program.G.K.N.Wizard/?mode=fixaddonupdate")')