
import os, glob, xbmc, xbmcgui, xbmcvfs, xbmcaddon, shutil
from updatervar import *
#from resources.lib.modules.delete_addons import del_dir
from resources.lib.GUIcontrol import txt_updater
from resources.lib.modules import db, addonsEnable
from resources.lib.modules.addonsEnable import enable_addons
#from resources.lib.modules.installer_addons import installAddon
from resources.lib.GUIcontrol.txt_updater import get_skinshortcutsversion

skinshortcuts_version = get_skinshortcutsversion()

Database_Addons33 = [('plugin.video.fmoviesto', 'repository.gkobu'),
                     ('plugin.video.cartoonsgr', 'repository.bugatsinho'),
                     ('plugin.video.shadow', 'repository.gkobu'),
                     ('plugin.video.microjen', 'repository.gkobu'),
                     ('script.gkobu.pairwith', 'repository.gkobu'),
                     ('script.module.grs', 'repository.gkobu'),
                     ('plugin.program.downloader', 'repository.gkobu'),
                     ('script.module.resolveurl', 'repository.gkobu'),
                     ('script.module.oathscrapers', 'repository.gkobu'),
                     ('plugin.video.duffyou', 'repository.gkobu'),
                     ('script.module.blackscrapers', 'repository.gkobu'),
                     ('resource.images.blacklodge.artwork', 'repository.gkobu'),
                     ('plugin.video.blacklodge', 'repository.gkobu'),
                     ('script.module.streamlink', 'repository.gkobu'),
                     ('service.subtitles.localsubtitle', 'repository.gkobu'),
                     
                     
                     ('repository.gknwiz', 'repository.gknwiz'),
                     ('plugin.program.G.K.N.Wizard', 'repository.gknwiz'),
                     
                     ('script.theoath.artwork', 'repository.gkobu'),
                     ('plugin.video.winner', 'repository.gkobu'),
                     ('plugin.video.theoath', 'repository.gkobu'),
                     ('script.extendedinfo', 'repository.Worldolympic'),
                     
                     ('repository.mbebe', 'repository.mbebe'),
                     
                     
                     
                     ('repository.Worldolympic', 'repository.World'),
                     ('repository.World', 'repository.World'),
                     ('repository.Worldrepo', 'repository.World'),
                     
                     ('plugin.video.sportliveevents', 'repository.World'),
                     ('plugin.video.klubsports', 'repository.World'),
                     ('plugin.video.daddylive', 'repository.World'),
                     
                     
                     ('plugin.video.playlistloader', 'repository.World'),
                     
                     ('skin.19MatrixWorld', 'repository.Worldolympic'),
                     ('plugin.video.mlbtv2', 'repository.World'),
                     ('plugin.program.mypreferences', 'repository.Worldolympic'),
                     ('context.video.favourites', 'repository.Worldolympic'),
                     ('plugin.video.favourites', 'repository.Worldolympic'),
                     ('plugin.program.super.favourites', 'repository.World'),
                     ('service.World.Build', 'repository.Worldolympic'),
                     ('plugin.program.downloader19', 'repository.Worldolympic'),
                     ('plugin.program.autowidget', 'repository.Worldolympic'),
                     ('plugin.video.uiiumovies', 'repository.World'),
                     ('plugin.image.World', 'repository.Worldolympic'),
                     ('plugin.video.tvone', 'repository.World'),
                     ('plugin.video.tvone11', 'repository.World'),
                     ('plugin.video.tvone111', 'repository.World'),
                     ('plugin.video.tvone1111', 'repository.World'),
                     ('plugin.video.videodevil', 'repository.World'),  
                     ('plugin.video.theanonymous.matrix', 'repository.World'),
                     ('script.sites', 'repository.World'),
                     ('plugin.video.hdtrailers_net.reloaded', 'repository.World'),
                     ('plugin.video.tvseriesvideo', 'repository.World'),
                     ('plugin.video.playlistloader', 'repository.World'),
                     
                     
                     ('repository.encryptic', 'repository.encryptic'),
                     ('plugin.video.nlm', 'repository.encryptic'),
                     
                     ('plugin.video.vidembed', 'repository.World'),
                     ('script.module.parrot', 'repository.World'),
                     ('plugin.video.parrot', 'repository.World'),
                     
                     ('repository.parrot', 'repository.parrot'),
                     
                     
                     
                     ('plugin.video.cristalazul', 'repository.World'),
                     
                     ('repository.arrownegra', 'repository.arrownegra'),
                     
                     
                     ('plugin.video.netflix', 'repository.castagnait'),
                     
                     
                     ('plugin.video.themoviedb.helper', 'repository.jurialmunkey'),
                     ('repository.jurialmunkey', 'repository.jurialmunkey'),
                     
                     
                     ('plugin.video.atlas', 'repository.atlas'),
                     ('repository.atlas', 'repository.atlas'),
                     
                     ('plugin.video.vavooto', 'repository.michaz'),
                     
                     ('plugin.video.amazon-test', 'repository.sandmann79-py3.plugins'),
                     ('plugin.video.jetproxy', 'repository.Magnetic'),
                     ('script.module.slproxy', 'repository.gujal'),
                     
                     ('service.subtitles.opensubtitles_by_opensubtitles_dualsub', 'repository.peno64'),
                     
                     
                     ('repository.Rising.Tides', 'repository.Rising.Tides'),
                     ('plugin.video.viacom.mtv', 'repository.kodinerds'),
                     
                     ('repository.butter', 'repository.butter'),
                     ('repository.Rockcrusher', 'repository.Rockcrusher'),
                     
                     
                     ('repository.skinbase.19', 'repository.skinbase.19'),
                     ('chamchenko-dev', 'chamchenko-dev'),
                     
                     ('script.module.jetextractors', 'repository.loop'),
                     
                     ('repository.tvchopo', 'repository.tvchopo'),
                     ('vkkodi.repo', 'vkkodi.repo')]


                         ### Προσθέτεις εντός της αγκύλης τα πρόσθετα που επιθυμείς [  ] ###

addon_list = ['plugin.video.live.test', 'plugin.video.testt']


         ### Προσθέτεις εντός της αγκύλης τα πρόσθετα ή τα αρχεία που επιθυμείς να αφαιρέσεις [  ] ###

delete_addons = ['repository.test', 'repository.encryptic', 'repository.testt']



def Updater_Matrix():
    BG.create(Dialog_U1, Dialog_U2)
    
    xbmc.sleep(5000)
    BG.update(25, Dialog_U1, Dialog_U6)



    xbmc.sleep(5000)
    db.addon_database(Database_Addons33, 1, True)
    #xbmc.sleep(5000)
    #BG.update(40, Dialog_U1, 'Εισαγωγή αποθετηρίων στο Database/Addons33...')
    xbmc.sleep(5000)
    BG.update(40, Dialog_U1, 'Παρακαλώ περιμένετε...')




    xbmc.sleep(3000)
    #BG.update(30, Dialog_U1, 'Delete UpdaterMatrix...')
    del_dir()
    xbmc.sleep(3000)

                               ### delete addons ands files ###

                                 #Εγκατάσταση νέων repository'
    if os.path.exists(UpdaterMatrix_path2): xbmcvfs.delete(UpdaterMatrix_path2), xbmc.sleep(1000)

                                 #Εγκατάσταση addon_data
    if os.path.exists(UpdaterMatrix_path3): xbmcvfs.delete(UpdaterMatrix_path3), xbmc.sleep(1000)

                                        #KODI-Intro-Video.mp4
    if os.path.exists(UpdaterMatrix_path4): xbmcvfs.delete(UpdaterMatrix_path4), xbmc.sleep(1000)

                          #Εισαγωγή νέων διακομιστών του PvrStalker
    if os.path.exists(UpdaterMatrix_path5): xbmcvfs.delete(UpdaterMatrix_path5), xbmc.sleep(1000)

                                  #TheMovieDb Helper players
    if os.path.exists(UpdaterMatrix_path6): xbmcvfs.delete(UpdaterMatrix_path6), xbmc.sleep(1000)

                                           #Διάφορα Fix
    if os.path.exists(UpdaterMatrix_path7): xbmcvfs.delete(UpdaterMatrix_path7), xbmc.sleep(1000)

                                       #Fix skin.19MatrixWorld
    if os.path.exists(UpdaterMatrix_path8): xbmcvfs.delete(UpdaterMatrix_path8), xbmc.sleep(1000)

                                             #Addons33
    if os.path.exists(UpdaterMatrix_path9): xbmcvfs.delete(UpdaterMatrix_path9), xbmc.sleep(1000)

                                                 #plugin.program.downloader19
    if os.path.exists(UpdaterMatrix_path21): xbmcvfs.delete(UpdaterMatrix_path21), xbmc.sleep(1000)

                                             #test
    if os.path.exists(UpdaterMatrix_path22): xbmcvfs.delete(UpdaterMatrix_path22), xbmc.sleep(1000)

                                              #service.autoexec
    if os.path.exists(UpdaterMatrix_path23): xbmcvfs.delete(UpdaterMatrix_path23), xbmc.sleep(1000)

                                    #script.module.resolveurl
    if os.path.exists(UpdaterMatrix_path29): xbmcvfs.delete(UpdaterMatrix_path29), xbmc.sleep(1000)

                                        #DeleteFiles
    xbmc.sleep(3000)
    xbmcvfs.delete('special://home/userdata/addon_data/plugin.video.themoviedb.helper/players/atla_oipeirates.json')


### Το ενεργοποιείς όταν θέλεις να περάσεις πρόσθετα ###
    #xbmc.sleep(10000)
    #BG.update(42, Dialog_U1, 'Εγκατάσταση πρόσθετων...')
    xbmc.sleep(5000)
    installAddon()





    # tc [DeleteArrow]
    #xbmc.sleep(2000)
    #BG.update(32, Dialog_U1, 'RunScript DeleteAddonsNow')
    #xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/AddonsDelete/DeleteAddonsNow.py")')
    #xbmc.sleep(2000)
    #BG.update(33, Dialog_U1, Dialog_U6)




    #xbmc.sleep(5000)
    #BG.update(35, Dialog_U1, 'RunScript Delete temp')
    #xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/Tools/TempDelete/temp_Delete.py")')

    #xbmc.sleep(2000)
    #BG.update(36, Dialog_U1, Dialog_U6)


    #xbmc.sleep(5000)
    #BG.update(37, Dialog_U1, 'RunScript Delete repository.arrownegra')
    #xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/AddonsDelete/DeleteArrow.py")')

    #xbmc.sleep(5000)
    #BG.update(38, Dialog_U1, Dialog_U6)    

    #xbmc.sleep(5000)
    #BG.update(50, Dialog_U1, 'Περιμένετε...')


    #xbmc.sleep(5000)
    #BG.update(40, Dialog_U1, 'Delete Themoviedbhelper')
    #xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/AddonsDelete/DeleteThemoviedbhelper.py")')
    #xbmc.sleep(5000)




    xbmc.sleep(5000)
    BG.update(60, Dialog_U1, Dialog_U6)


###########################################################################


         #UP plugin.program.downloader19
    if not os.path.exists(UpdaterMatrix_path21):
        xbmc.sleep(5000)
        xbmc.executebuiltin(UpdaterMatrix_21)
        #BG.update(50, Dialog_U1, Dialog_U6)
        BG.update(70, Dialog_U1, 'Παρακαλώ περιμένετε...')




    #if not os.path.exists(UpdaterMatrix_path2):
        #xbmc.sleep(5000)
        #BG.update(44, Dialog_U1, 'Εγκατάσταση νέων repository')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_2)
        #xbmc.sleep(7000)
        #BG.update(46, Dialog_U1, Dialog_U6)



    #if not os.path.exists(UpdaterMatrix_path3):
        #xbmc.sleep(5000)
        #BG.update(48, Dialog_U1, 'Εγκατάσταση addon_data')
        #xbmc.sleep(7000)
        #xbmc.executebuiltin(UpdaterMatrix_3)
        #xbmc.sleep(7000)
        #BG.update(50, Dialog_U1, Dialog_U6)



    #if not os.path.exists(UpdaterMatrix_path4):
        #xbmc.sleep(5000)
        #BG.update(52, Dialog_U1, 'KODI-Intro-Video.mp4') 
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_4)
        #xbmc.sleep(7000)
        #BG.update(54, Dialog_U1, Dialog_U6)



    #if not os.path.exists(UpdaterMatrix_path5):
        #xbmc.sleep(5000)
        #BG.update(56, Dialog_U1, 'Εισαγωγή νέων διακομιστών του PvrStalker...')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_5)
        #xbmc.sleep(7000)
        #BG.update(58, Dialog_U1, Dialog_U6)



    #if not os.path.exists(UpdaterMatrix_path6):
        #xbmc.sleep(5000)
        #BG.update(62, Dialog_U1, 'TheMovieDb Helper players')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_6)
        #xbmc.sleep(7000)
        #BG.update(64, Dialog_U1, Dialog_U6)



    #if not os.path.exists(UpdaterMatrix_path7):
        #xbmc.sleep(5000)
        #BG.update(66, Dialog_U1, 'Διάφορα Fix')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_7)
        #xbmc.sleep(7000)
        #BG.update(68, Dialog_U1, Dialog_U6)


    xbmc.sleep(5000)
    BG.update(75, Dialog_U1, Dialog_U6)



    #if not os.path.exists(UpdaterMatrix_path8):
        #xbmc.sleep(5000)
        #BG.update(70 , Dialog_U1, 'Up skin...')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_8)
        #BG.update(72, Dialog_U1, 'skinshortcuts_menu')
        #xbmc.sleep(7000)



    #if not os.path.exists(UpdaterMatrix_path9):
        #xbmc.sleep(5000)
        #BG.update(74 , Dialog_U1, 'Addons33')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_9)
        #xbmc.sleep(7000)
        #BG.update(76, Dialog_U1, Dialog_U6)



    #if not os.path.exists(UpdaterMatrix_path22):
        #xbmc.sleep(5000)
        #BG.update(78 , Dialog_U1, 'test')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_22)
        #BG.update(80, Dialog_U1, Dialog_U6)  
        #xbmc.sleep(7000)



    #if not os.path.exists(UpdaterMatrix_path23):
        #xbmc.sleep(5000)
        #BG.update(78 , Dialog_U1, 'autoexec.py')
        #xbmc.sleep(5000)
        #xbmc.executebuiltin(UpdaterMatrix_23)
        #BG.update(80, Dialog_U1, Dialog_U6)  
        #xbmc.sleep(7000)



    #if not os.path.exists(UpdaterMatrix_path29):
        #xbmc.sleep(5000)
        #BG.update(81, Dialog_U1, 'reset settings resolveurl')
        #xbmc.sleep(7000)
        #xbmc.executebuiltin(UpdaterMatrix_29)
        #BG.update(80, Dialog_U1, Dialog_U6)  
        #xbmc.sleep(7000)


    xbmc.sleep(5000)
    #BG.update(80, Dialog_U1, Dialog_U6)
    #xbmc.sleep(1000)
    #xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/DeleteFiles.py")')
    #xbmc.sleep(1000)
    xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/PY/DeleteFoldersNow.py")')
    xbmc.sleep(5000)
    BG.update(85, Dialog_U1, 'Παρακαλώ [COLOR green]περιμένετε[/COLOR] χωρίς να πατήσετε κάτι.')

    #xbmc.executebuiltin('RunScript("special://home/addons/service.World.Build/service.downloaderstartup/In_TheMovieDb Helper.py")')

    #xbmc.sleep(5000)
    #BG.update(83, Dialog_U1, 'Ενεργοποίηση πρόσθετων...')
    #addonsEnable.enable_addons()
    
    #xbmc.sleep(5000)
    #BG.update(82, Dialog_U1, 'Install all updates')
    #RunAddon()

    #xbmc.sleep(7000)
    #BG.update(90, Dialog_U1, Dialog_U6)
###########################################################################




    xbmc.sleep(5000)
    BG.update(92, Dialog_U1, 'Ελεγχος για ενημέρωση στο μενού του skin...')


    if skinshortcuts_version > int(setting('skinshortcutsversion')):
        xbmc.executebuiltin(skinshortcuts_menu)
        xbmc.sleep(5000)
        BG.update(96, Dialog_U1, 'Ενημέρωση μενού skin.')
        setting_set('skinshortcutsversion', str(skinshortcuts_version))
        xbmc.sleep(5000)
        BG.update(100, Dialog_U4, 'Θα ακολουθήσει... επαναφόρτωση του προφίλ')
        xbmc.sleep(5000)
        BG.update(100, Dialog_U4, 'Θα ακολουθήσει... και πάγωμα της εικόνας')
        xbmc.sleep(5000)
        BG.update(100, Dialog_U4, Dialog_U5)
        xbmc.executebuiltin("LoadProfile(Master user)")
    xbmc.sleep(5000)
    BG.update(100, Dialog_U4, Dialog_U5)
    xbmc.sleep(5000)
    BG.update(100, Dialog_U4, Dialog_U5)

    xbmc.sleep(5000)
    addonsEnable.enable_addons()

    BG.close()
    xbmcvfs.delete(downloader_startup_delete)


def installAddon():
    for addon_id in addon_list:
      xbmc.executebuiltin('InstallAddon(%s)' % (addon_id))
      xbmc.sleep(100)
      xbmc.executebuiltin('SendClick(11)')
      xbmc.sleep(100)


def del_dir():
    for ad in addons_data_path:
     for rr in delete_addons:
       dir_list = glob.iglob(os.path.join(ad, rr))
       for path in dir_list:
           if os.path.isdir(path):
               shutil.rmtree(path)
           if os.path.isfile(path):
              os.remove(path)


def enable_addons():
	conn =db_lib.connect(os.path.join(xbmc.translatePath('special://profile/Database'),'Addons33.db'))
	conn.text_factory = str
	conn.executemany('update installed set enabled=1 where addonID = (?)',((val,) for val in os.listdir(xbmc.translatePath(os.path.join('special://home','addons')))))
	conn.commit()
	xbmc.executebuiltin('UpdateLocalAddons')
	xbmc.executebuiltin('UpdateAddonRepos')


     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"videoplayer.stretch43","value":0}}')
     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"addons.updatemode","value":1}}')
     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"GUI.SetFullscreen","id":1,"params":{"fullscreen":"toggle"}}')
     #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ExecuteAction","id":1,"params":{"action":"togglefullscreen"}}')




#        choice = xbmcgui.Dialog().yesno('[B][COLOR orange]TechNEWSology[/COLOR][/B]', '[COLOR white]      Επιθυμείτε την απενεργοποίηση των ενημερώσεων [CR]                        του TechNEWSology Updater ?[/COLOR]',
#                                        nolabel='[COLOR lime]Ενεργοποίηση[/COLOR]',yeslabel='[COLOR orange]Απενεργοποίηση[/COLOR]')
#        if choice == 1: [xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "plugin.program.downloader19","enabled":false}}'), xbmcgui.Dialog().ok("[COLOR lime]TechNEWSology Updater-Tools[/COLOR]", "[COLOR orange]Απενεργοποήθηκαν οι αυτόματες ενημερώσεις         του TechNEWSology Updater.[/COLOR]")]
#        else:
#            xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "plugin.program.downloader19","enabled":true}}')

Updater_Matrix()
