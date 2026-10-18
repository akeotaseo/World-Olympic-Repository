import os, xbmc
from xbmc import log
from urllib.request import urlopen
from urllib.request import Request
from zipfile import ZipFile
from updatervar import *
from resources.lib.modules.save_data import save_restore

exists = os.path.exists

def downloader(NAME, NAME2, VERSION, URL):
	zippath = tempfile_1
	if exists(tempfile_1): zippath  = tempfile_2
	if exists(tempfile_2): zippath  = tempfile_3
	if exists(tempfile_3): zippath  = tempfile_4
	if exists(tempfile_4): zippath  = tempfile_5
	if exists(tempfile_5): zippath  = tempfile_6
	if exists(tempfile_6): zippath  = tempfile_7
	if exists(tempfile_7): zippath  = tempfile_8
	if exists(tempfile_8): zippath  = tempfile_9
	if exists(tempfile_9): zippath  = tempfile_10
	if exists(tempfile_10): zippath = tempfile_11
	if exists(tempfile_11): zippath = tempfile_12
	if exists(tempfile_12): zippath = tempfile_13
	if exists(tempfile_13): zippath = tempfile_14
	if exists(tempfile_14): zippath = tempfile_15
	if exists(zippath):
		os.unlink(zippath)
	tempzip = open(zippath, 'wb')
	response = Request(URL, headers = headers)
	zipresp = urlopen(response)
	length = zipresp.getheader('content-length')
#	if length:
#		length2 = int(int(length)/1000000)
#	else:
#		length2 = 'Unknown Size'
#	dp.create(NAME + ' - ' + str(length2) + ' MB', 'Λήψη αρχείου zip...')
#	dp.update(0, 'Λήψη αρχείου zip...')

#	if length:
#		blocksize = max(int(length)/512, 1000000)
#		size = 0
#		while True:
#			buf = zipresp.read(blocksize)
#			if not buf:
#				break
#			size += len(buf)
#			size2 = int(size/1000000)
#			tempzip.write(buf)
#			dp.update(size2, 'Λήψη αρχείου zip...' + str(size2) + '/' + str(length2) + 'MB')

#	else:
#		dp.update(50, 'Λήψη αρχείου zip...')
#		tempzip.write(zipresp.read())
	tempzip.write(zipresp.read())

#	if length:
#		dp.update(100, 'Λήψη αρχείου zip...' + str(size2) + '/' + str(length2) + 'MB...Έγινε!')
#	else:
#		dp.update(100, 'Λήψη αρχείου zip...Έγινε!')
	xbmc.sleep(1000)
	tempzip.close()
#	dp.update(66, 'Εξαγωγή αρχείου zip...')
	xbmc.sleep(1000)
	zf = ZipFile(zippath)
	zf.extractall(path = home)
#	dp.update(100, 'Ολοκληρώθηκε με επιτυχία!')
	xbmc.sleep(2000)
	zf.close()
	os.unlink(zippath)


def downloader_b(NAME, NAME2, VERSION, URL):
	zippath = os.path.join(packages + "bfile.zip")
	if os.path.exists(zippath):
		os.unlink(zippath)
	tempzip = open(zippath, 'wb')
	response = Request(URL, headers = headers)
	zipresp = urlopen(response)
	length = zipresp.getheader('content-length')
	if length:
		length2 = int(int(length)/1000000)
	else:
		length2 = 'Unknown Size'
	dp.create(NAME + ' - ' + str(length2) + ' MB', 'Λήψη αρχείου zip...')
	dp.update(0, 'Λήψη αρχείου zip...')

	if length:
		blocksize = max(int(length)/512, 1000000)
		size = 0
		while True:
			buf = zipresp.read(blocksize)
			if not buf:
				break
			size += len(buf)
			size2 = int(size/1000000)
			tempzip.write(buf)
			dp.update(size2, 'Λήψη αρχείου zip...' + str(size2) + '/' + str(length2) + 'MB')

	else:
		dp.update(50, 'Λήψη αρχείου zip...')
		tempzip.write(zipresp.read())
	if length:
		dp.update(100, 'Λήψη αρχείου zip...' + str(size2) + '/' + str(length2) + 'MB...Έγινε!')
	else:
		dp.update(100, 'Λήψη αρχείου zip...Έγινε!')
	xbmc.sleep(1000)
	tempzip.close()
	dp.update(66, 'Εξαγωγή αρχείου zip...')
	xbmc.sleep(1000)
	zf = ZipFile(zippath)
	zf.extractall(path = home)
	dp.update(100, 'Ολοκληρώθηκε με επιτυχία!')
	xbmc.sleep(2000)
	zf.close()
	os.unlink(zippath)
	save_restore()