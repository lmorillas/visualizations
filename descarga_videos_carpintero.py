""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *

RUTA = 'docs/static/'
RUTAINDEX = 'docs/carpintero/index.html'

if __name__ == '__main__':
    description = "Vídeos youtube de Pablo Carpintero"
    title = "Vídeos Pablo Carpintero"
    schema = json.load(open('schema.json'))

    yt = connect_youtube()

    channelId = "UCm3XpXgNUStILc2R9m5XOag"
    username = 'PabloCarpintero1'

    videos = todos_los_videos_canal(yt, channelId)

    json.dump(videos, open('videos_carpintero_yt.json', 'w'))
    videose = crea_videos_exhibit('videos_carpintero_yt.json')
    crea_index(ruta = RUTAINDEX, schema = schema, data = {"items": videose},
        title = title, description = description)

