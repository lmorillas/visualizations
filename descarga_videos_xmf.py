""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *
from muxicas import *

RUTA = 'docs/static/'

if __name__ == '__main__':
    schema = json.load(open('schema.json'))

    yt = connect_youtube()

    videos = todos_los_videos_canal(yt, channelId)

    json.dump(videos, open('videos_yt.json', 'w'))
    videose = crea_videos_exhibit('videos_yt.json')
    crea_index(ruta = RUTAINDEX, schema = schema, data = {"items": videose},
        title = title, description = description)


        