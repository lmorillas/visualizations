""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from .secret import DEVELOPER_KEY


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def connect_youtube():
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    return youtube

def fetch_youtube_videos_playlist(youtube, playlistId):
    """
    Fetches a playlist of videos from youtube
    We splice the results together in no particular order

    Parameters:
        parm1 - (string) playlistId
    Returns:
        playListItem Dict
    """
    part="snippet,status,contentDetails"

    res = youtube.playlistItems().list(
    part=part,
    playlistId=playlistId,
    maxResults="50"
    ).execute()

    nextPageToken = res.get('nextPageToken')
    while ('nextPageToken' in res):
        nextPage = youtube.playlistItems().list(
        part=part,
        playlistId=playlistId,
        maxResults="50",
        pageToken=nextPageToken
        ).execute()
        res['items'] = res['items'] + nextPage['items']

        if 'nextPageToken' not in nextPage:
            res.pop('nextPageToken', None)
        else:
            nextPageToken = nextPage['nextPageToken']

    return res


def get_playlists(youtube, channelId):
    part="snippet,status,contentDetails"
    res = youtube.playlists().list(
        part=part, 
        channelId=channelId, 
        maxResults="50", 
        ).execute()
    nextPageToken = res.get('nextPageToken')
    
    while (nextPageToken):
        nextPage = youtube.playlists().list(
        part=part, 
        channelId=channelId, 
        maxResults="50", 
        pageToken=nextPageToken
        ).execute()
        res['items'] = res['items'] + nextPage['items']

        nextPageToken = nextPage.get('nextPageToken')
        
    return res

def todos_los_videos_playlist(yt, playlists):
    videos = []
    for p in playlists['items']:
        res = fetch_youtube_videos_playlist(yt, p.get('id'))
        videos = videos + res['items']
    '''
    videos2 = []

    for p in playlists['items']:
        res = fetch_all_youtube_videos_status(yt, p.get('id'))
        videos2 = videos2 + res['items']
    '''
    return videos

def todos_los_videos_canal(yt, canal):
    part="id, snippet"
    res = yt.search().list(
        part=part, 
        channelId=canal, 
        maxResults="50", 
        ).execute()

    nextPageToken = res.get('nextPageToken')
    
    while (nextPageToken):
        nextPage = yt.search().list(
        part=part, 
        channelId=canal, 
        maxResults="50", 
        pageToken=nextPageToken
        ).execute()
        res['items'] = res['items'] + nextPage['items']

        nextPageToken = nextPage.get('nextPageToken')
        
    return res['items']
        
if __name__ == '__main__':
    
    # comedy central playlist, has 332 video
    # https://www.youtube.com/watch?v=tJDLdxYKh3k&list=PLD7nPL1U-R5rDpeH95XsK0qwJHLTS3tNT
    

    ejercicios = 'PLybE0q7GFyrYHdWcrcb74l6ZXi1jbGXU4'
    
    channelId = "UC5ulFfNeWSJuzeKJFY-hUvQ"
    username = "davidbellasgarcia"

    channelList = {
   "kind": "youtube#channel",
   "etag": "\"DuHzAJ-eQIiCIp7p4ldoVcVAOeY/Wfv9vP_GKiAbHv_NHQi4-A6DgdE\"",
   "id": "UC5ulFfNeWSJuzeKJFY-hUvQ",
   "contentDetails": {
    "relatedPlaylists": {
     "favorites": "FL5ulFfNeWSJuzeKJFY-hUvQ",
     "uploads": "UU5ulFfNeWSJuzeKJFY-hUvQ",
     "watchHistory": "HL",
     "watchLater": "WL"
    }
   }
   }


    yt = connect_youtube()
    playlists = get_playlists(yt, channelId)
    #videos = fetch_all_youtube_videos(yt, "PLybE0q7GFyrbQSrWNgci8QJ60gQjQKLlH")
    videos  = todos_los_videos(yt, playlists)
    videos2 = todos_los_videos_2(yt, channelId)

    json.dump(playlists, open('playlists_bellas_yt.json', 'w'))
    json.dump(videos, open('videos_bellas_yt.json', 'w'))
    

    x = 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=davidbellasgarcia&key=AIzaSyCg2O20tAx14Awx4jat1N09lKxLtvckUf4'
    y = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId=UC5ulFfNeWSJuzeKJFY-hUvQ&key=AIzaSyCg2O20tAx14Awx4jat1N09lKxLtvckUf4'
    z = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId=UC5ulFfNeWSJuzeKJFY-hUvQ&key=AIzaSyCg2O20tAx14Awx4jat1N09lKxLtvckUf4&pageToken=CAUQAA'




        