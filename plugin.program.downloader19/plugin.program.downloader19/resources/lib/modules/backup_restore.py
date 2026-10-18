import os, xbmc, xbmcgui, shutil
from zipfile import ZipFile
from pathlib import Path
from updatervar import *
from resources.lib.modules.utils import addDir

p = Path(home)
backup_path = Path(translatePath(setting('backupfolder')))
backups = p / 'backups'
addons = p / 'addons'
media = p / 'media'
userdata = p / 'userdata'
wizard_path = Path(addon_path)
data_path = Path(addon_profile)

def log(_text, _var):
	xbmc.log(f'{_text} = {str(_var)}', xbmc.LOGINFO)

excludes = [p / 'addons/packages', p / 'addons/temp', p / 'userdata/Thumbnails', p / 'userdata/Database/Textures13.db', p / wizard_path]

def from_keyboard():
	kb = xbmc.Keyboard('', 'Ονομασία Backup αρχείου', False)
	kb.doModal()
	if (kb.isConfirmed()):
		return kb.getText()
	else:
		return False

def backup_build():
	backup_path.mkdir(parents=True, exist_ok=True)
	k = from_keyboard()
	if k is False:
		return xbmcgui.Dialog().ok('[B]Backup[/B]', '[CR]                                       [B]Ακυρώθηκε![/B]')
	else:
		backup_name = backup_path / f'{k}.zip'
	BG.create('Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')
	addons_dirs, addons_files = ([x for x in addons.iterdir() if x.is_dir() and x not in excludes]), ([x for x in addons.iterdir() if x.is_file() and x not in excludes])
	BG.update(25, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')

	media_dirs, media_files = ([x for x in media.iterdir() if x.is_dir() and x not in excludes]), ([x for x in media.iterdir() if x.is_file() and x not in excludes])
	BG.update(35, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')

	userdata_dirs, userdata_files = ([x for x in userdata.iterdir() if x.is_dir() and x not in excludes]), ([x for x in userdata.iterdir() if x.is_file() and x not in excludes])

	zip_file = ZipFile(backup_name, 'w')
	BG.update(45, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')

	for x in sorted(addons_dirs):
		for z in sorted([y for y in x.rglob('*') if y not in excludes]):
			if '__pycache__' not in str(z):
				zip_file.write(z, str(z.relative_to(p)))
				BG.update(67, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')

	for x in sorted(addons_files):
		zip_file.write(x, str(x.relative_to(p)))
		BG.update(75, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')

	for x in sorted(media_dirs):
		for z in sorted([y for y in x.rglob('*') if y not in excludes]):
			zip_file.write(z, str(z.relative_to(p)))
			BG.update(88, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')

	for x in sorted(media_files):
		zip_file.write(x, str(x.relative_to(p)))
		BG.update(90, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')

	for x in sorted(userdata_dirs):
		for z in sorted([y for y in x.rglob('*') if y not in excludes]):
			zip_file.write(z, str(z.relative_to(p)))
			BG.update(100, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')
	for x in sorted(userdata_files):
		zip_file.write(x, str(x.relative_to(p)))
		BG.update(100, 'Αντίγραφο ασφαλείας', 'Αποθήκευση αρχείων...')
	BG.close()
	zip_file.close()

	xbmcgui.Dialog().ok('[B]Backup[/B]', '[CR]                        [COLOR lime]Ολοκληρώθηκε με επιτυχία![/COLOR]')

excludes_freshstart = [addon_id, 'backups',  'Addons33.db', 'kodi.log']

def fresh_start_restore():
	for root, dirs, files in os.walk(xbmcPath, topdown=True):
		dirs[:] = [d for d in dirs if d not in excludes_freshstart]
		for name in files:
			if name not in excludes_freshstart:
				try:
					os.unlink(os.path.join(root, name))
				except:
					log('Error Deleting', name)
					
	for root, dirs, files in os.walk(xbmcPath,topdown=True):
		dirs[:] = [d for d in dirs if d not in excludes_freshstart]
		for name in dirs:
			if name not in ['addons', 'userdata', 'Database', 'addon_data', 'backups', 'temp']:
				try:
					shutil.rmtree(os.path.join(root,name),ignore_errors=True, onerror=None)
				except:
					log('Error Deleting', name)

def get_backup_folder():
    dialog = xbmcgui.Dialog()
    fn = dialog.browseSingle(0, 'Kodi', 'local', '', False, False)
    setting_set('backupfolder', fn)

def reset_backup_folder():
    setting_set('backupfolder', 'special://home/backups')
    xbmcgui.Dialog().ok('Backup Folder', 'Θέση φακέλου Backup\Προεπιλεγμένος ορισμός')

def restore_menu():
    build_backups = ([x for x in backup_path.iterdir() if x.is_file() and str(x).endswith('.zip')])
    for build in build_backups:
        addDir(str(build.stem), str(build), 20, icon_Build, addon_fanart, str(build.name), isFolder=False)


def restore_build(zippath):
    restore = xbmcgui.Dialog().yesno('Επαναφορά', 'Είστε βέβαιοι ότι θέλετε να πραγματοποιηθεί διαγραφή στα τρέχοντα δεδομένα και να κάνετε επαναφορά από αντίγραφο ασφαλείας?')
    if restore is True:
        fresh_start_restore()
        if os.path.exists(zippath):
            BG.create('Επαναφορά', 'Εξαγωγή αρχείου...')
            counter = 1
            with ZipFile(zippath, 'r') as z:
                files = z.infolist()
                for file in files:
                    filename = file.filename
                    filename_path = os.path.join(home, filename)
                    progress_percentage = int(counter/len(files)*100)
                    try:
                        if not os.path.exists(filename_path) or 'Addons33.db' in filename:
                            z.extract(file, home)
                    except Exception as e:
                        xbmc.log(f'Error extracting {filename} - {e}', xbmc.LOGINFO)
                    BG.update(progress_percentage, f'{local_string(30034)}...\n{progress_percentage}%\n{filename}')
                    counter += 1
                BG.update(100, 'Ολοκληρώθηκε με επιτυχία!')
                xbmcgui.Dialog().ok('Επαναφορά', '[CR]                        [COLOR lime]Ολοκληρώθηκε με επιτυχία![/COLOR]')
                setting_set('firstrun', 'true')
                os._exit(1)
            BG.close()
        else:
            xbmcgui.Dialog().ok('Επαναφορά', 'Δεν βρέθηκε αρχείο Backup')
    else:
        return False