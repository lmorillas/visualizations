""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *

RUTA = 'videos_bellas/docs/static/'
        
if __name__ == '__main__':

    yt = connect_youtube()

    channelId = "UC5NVNZjoW0G40JJnygtGHAA"

    videos = todos_los_videos_canal(yt, channelId)
    #videos2 = todos_los_videos_2(yt, channelId)

    
    json.dump(videos, open('videos_xmf_yt.json', 'w'))
    crea_videos_exhibit('videos_xmf_yt.json', RUTA + 'videos_muxicas.json')
    

    



        