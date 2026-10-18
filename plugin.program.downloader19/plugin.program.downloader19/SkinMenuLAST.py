import xbmc, xbmcgui
xbmcgui.Dialog().notification("[B][COLOR blue]Skin World[/COLOR][/B]", "Ρυθμίσεις - HOME", icon='special://home/addons/skin.19MatrixWorld/resources/icon.png', sound=True)

from resources.lib.modules import check

from updatervar import *




if __name__ == '__main__':
	# if not setting('updaterversion') == 'false':
		# xbmcgui.Dialog().notification("[B][COLOR orange]Ελεγχος για ενημερώσεις[/COLOR][/B]", "...", icon='special://home/addons/plugin.program.downloader19/icon.gif', sound=False)
		# xbmc.sleep(5000)
		# check.notifyT()
		# check.autoenable()
		# check.var()
		# check.delete()
		# check.installation()
		# check.players()
		# check.zip1()
		# check.zip2()
		# check.zip3()
		# check.zip4()
		# check.zip5()
		# check.pvr()
		# check.setsetting()
		# check.database()
		check.xmlskin()
		# xbmc.sleep(5000)
		# check.UpdateAddonRepos()





