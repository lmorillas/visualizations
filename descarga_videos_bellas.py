""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *

RUTA = 'docs/static/'
        
if __name__ == '__main__':

    yt = connect_youtube()

    channelId = "UC5ulFfNeWSJuzeKJFY-hUvQ"

    playlists = get_playlists(yt, channelId)

    #videos = fetch_all_youtube_videos(yt, "PLybE0q7GFyrbQSrWNgci8QJ60gQjQKLlH")
    videos  = todos_los_videos_playlist(yt, playlists)
    #videos2 = todos_los_videos_2(yt, channelId)

    json.dump(playlists, open('playlists_bellas_yt.json', 'w'))
    json.dump(videos, open('videos_bellas_yt.json', 'w'))
    crea_videos_exhibit('videos_bellas_yt.json', RUTA + 'videos_bellas.json')
    crea_playlist_exhibit('playlists_bellas_yt.json', RUTA + 'playlists_bellas.json')


    



        