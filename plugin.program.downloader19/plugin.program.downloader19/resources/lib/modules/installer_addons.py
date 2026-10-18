import xbmc

def installAddon():
    for addon_id in addon_list:
      xbmc.executebuiltin('InstallAddon(%s)' % (addon_id))
      xbmc.sleep(100)
      xbmc.executebuiltin('SendClick(11)')
      xbmc.sleep(100)

addon_list = ['plugin.video.crackle', 'plugin.video.skylinecctv', 'plugin.program.autowidget',
              'plugin.video.live.streamspro', 'plugin.program.downloader19', 'context.subtitles.gr',
              'service.subtitles.opensubtitles_by_opensubtitles', 'service.subtitles.localsubtitle',
              'service.subtitles.greeksubs', 'plugin.video.playlistloader', 'context.themoviedb.helper',
              'plugin.video.tvone1112', 'repository.vstream', 'repository.thecrew', 'context.trailer.mod',
              'plugin.video.themoviedb.helper', 'plugin.video.tvone111', 'plugin.video.sporthdme',
              'repository.NarcacistWizard', 'repository.Rising.Tides', 'plugin.video.subsmovies',
              'plugin.video.cartoonsgr']
