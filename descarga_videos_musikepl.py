""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *

RUTA = 'docs/static/'
        
if __name__ == '__main__':

    yt = connect_youtube()

    channelId = "UC0DgZM3kQfc_xuZyjcqSQVg"
    username = 'Pablomousike1'

    
    playlists = get_playlists(yt, channelId)

    #videos = fetch_all_youtube_videos(yt, "PLybE0q7GFyrbQSrWNgci8QJ60gQjQKLlH")
    videos  = todos_los_videos_playlist(yt, playlists)
    ids = [x['snippet']['resourceId']['videoId'] for x in videos]
    
    videosCanal = todos_los_videos_canal(yt, channelId)
    videosCanal  = [v   for v in videosCanal if v['id']['kind'] == 'youtube#video' ]
    noestan = [v for v in videosCanal if v['id']['videoId'] not in ids]
    videos.extend(noestan)
    #videos2 = todos_los_videos_2(yt, channelId)

    json.dump(playlists, open('playlists_mousike_yt.json', 'w'))
    json.dump(videos, open('videos_mousike_yt.json', 'w'))
    crea_videos_exhibit('videos_mousike_yt.json', RUTA + 'videos_mousike.json')
    crea_playlist_exhibit('playlists_mousike_yt.json', RUTA + 'playlists_mousike.json',
        separador='|'  )
        