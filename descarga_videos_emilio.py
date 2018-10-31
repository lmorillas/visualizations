""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *
from emiliovillalba import *

RUTA = 'docs/static/'
        
if __name__ == '__main__':

    yt = connect_youtube()
    schema = json.load(open('schema.json'))
    
    if playlist:
        playlists = get_playlists(yt, channelId)
        json.dump(playlists, open('playlists_yt.json', 'w'))
        
    videos  = todos_los_videos_playlist(yt, playlists)
    ids = [x['snippet']['resourceId']['videoId'] for x in videos]
    videosCanal = todos_los_videos_canal(yt, channelId)
    videosCanal  = [v   for v in videosCanal if v['id']['kind'] == 'youtube#video' ]
    noestan = [v for v in videosCanal if v['id']['videoId'] not in ids]
    videos.extend(noestan)

    json.dump(videos, open('videos_yt.json', 'w'))
    videos = crea_videos_exhibit('videos_yt.json' )

    if playlist:
        playlists = crea_playlist_exhibit('playlists_yt.json', separador='|')
    else:
        playlists = []
    
    crea_index(ruta = RUTAINDEX, schema = schema, data = {"items": videos + playlists},
        title = title, description = description, playlist=playlist)
