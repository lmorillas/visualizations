import json

def crea_videos_exhibit(entrada, salida=None):
    items = []
    itemsd = {}

    videos = json.load(open(entrada))
    for v in videos:
        try:
            if v.get('status') and v['status']['privacyStatus'] != 'public' or \
                v['snippet']['title'] == 'Deleted video':
                continue
            d = v.get('snippet')
            k = {}
            k['url'] = d['resourceId']['videoId']
            if k['url'] in itemsd:
                itemsd[k['url']]['playlistId'].append(d.get('playlistId'))
            else:
                k['label'] = d.get('title')
                try:
                    k['imagen'] = d['thumbnails']['medium']['url']
                except:
                    try:
                        k['imagen'] = d['thumbnails']['default']['url']
                    except:
                        print(k, 'no imagen')
                        pass
                k['playlistId'] = [d.get('playlistId')]
                k['position'] = d.get('position')
                k['url'] = d['resourceId']['videoId']
                k['type'] = 'video'
                k['id'] = v.get('id')
                k['publishedAt'] = d.get('publishedAt')[:10]
                k['description'] = d.get('description')
                itemsd[k['url']] = k
        except  Exception as e:
            print ('Exception --> ', e)
            if v.get('id') and v['id'].get('kind') != 'youtube#video':    
                continue
            d = v.get('snippet')
            k = {}
            k['url'] = v['id']['videoId']
            k['label'] = d.get('title')
            k['type'] = 'video'
            k['id'] = v['id']['videoId']
            k['publishedAt'] = d.get('publishedAt')[:10]
            k['description'] = d.get('description')
            try:
                k['imagen'] = d['thumbnails']['medium']['url']
            except:
                try:
                    k['imagen'] = d['thumbnails']['default']['url']
                except:
                    print(k, 'no imagen')
                    pass
            itemsd[k['url']] = k
    if salida:
        json.dump({'items': list(itemsd.values())}, open(salida, 'w'))
    else:
        return list(itemsd.values())

def crea_playlist_exhibit(entrada, salida=None, remove = None, separador=None):
    playlists = json.load(open(entrada))
    items = []
    for p in playlists.get('items'):
        if p['status']['privacyStatus'] == 'public':
            k = {}
            k['id'] = p.get('id')
            k['label'] = p['snippet']['title']
            if remove:
                k['label'] = k['label'].replace('remove', '').strip()
            if separador:
                k['label'] = k['label'].split(separador)[0].strip()
            k['type'] = 'playlist'
            items.append(k)
    if salida:
        json.dump({'items': items}, open(salida, 'w'))
    else:
        return items
