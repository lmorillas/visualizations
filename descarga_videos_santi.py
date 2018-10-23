""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *


        
if __name__ == '__main__':

    yt = connect_youtube()

    channelId = "UC0H23AN4HK_iKoMR9dr-kmA"
    username = 'SantiGaitero'

    playlists = get_playlists(yt, channelId)
    videos  = todos_los_videos_playlist(yt, playlists)


    #videos = todos_los_videos_canal(yt, channelId)

    json.dump(playlists, open('playlists_santi_yt.json', 'w'))
    crea_playlist_exhibit('playlists_santi_yt.json', 'playlists_santi.json')

    json.dump(videos, open('videos_santi_yt.json', 'w'))
    crea_videos_exhibit('videos_santi_yt.json', 'videos_santi.json')
    

    
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
