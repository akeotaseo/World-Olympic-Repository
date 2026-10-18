import os, glob, shutil
from updatervar import *
delete_files = translatePath('special://home/userdata/addon_data/plugin.program.downloader19/delete_files.py')
#from delete_files import delete_files
exists = os.path.exists


def check_del_dir():
    for path_list in delete_files:
        if exists(addons_path + '%s' % path_list) or exists('%s' % path_list):
    #        path_list = path_list.replace(UpdaterMatrix, '').replace(addons_path, '')
            BG.update(33, '[B]Διαγραφή αχρείαστων αρχείων...[/B]', path_list)
            xbmc.sleep(1000)
            del_dir()

def del_dir():
    for ad in addons_data_path:
     for rr in delete_files:
       dir_list = glob.iglob(os.path.join(ad, rr))
       for path in dir_list:
           if os.path.isdir(path):
               shutil.rmtree(path)
           if os.path.isfile(path):
              os.remove(path)

