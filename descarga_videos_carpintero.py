""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *

RUTA = 'docs/static/'
        
if __name__ == '__main__':

    yt = connect_youtube()

    channelId = "UCm3XpXgNUStILc2R9m5XOag"
    username = 'PabloCarpintero1'

    videos = todos_los_videos_canal(yt, channelId)

    json.dump(videos, open('videos_carpintero_yt.json', 'w'))
    crea_videos_exhibit('videos_carpintero_yt.json', RUTA + 'videos_carpintero.json')
    

    


    
    uploads = "UUm3XpXgNUStILc2R9m5XOag"

    channelList = {
        "kind": "youtube#channel",
        "etag": "\"DuHzAJ-eQIiCIp7p4ldoVcVAOeY/VkPR2DYaapvBi9prtm7pSapAGiw\"",
        "id": "UCm3XpXgNUStILc2R9m5XOag",
        "contentDetails": {
            "relatedPlaylists": {
                "uploads": "UUm3XpXgNUStILc2R9m5XOag",
                "watchHistory": "HL",
                "watchLater": "WL"
            }
        }
    }
