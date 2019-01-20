import csv
import re
from urllib.parse import urlparse
import urllib
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import parse_qs

'''
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters
'''

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQj-2s2x-1_d9Z2z2jvr9VnMo8aiM8vr5lV3U25LXMkwCWYpd3YhyzizrQC-F-LsQ9JZXjuEPNgZk0z/pub'

resp = requests.get(url)

doc = BeautifulSoup(resp.text, 'lxml')


datos = []
for nid, r in enumerate(doc.find_all('tr')):
    lista = []
    lista.append(nid)
    for d in r.find_all('td'):
        a = d.find_all('a')
        if a:
            a = a[0]
            link = a.attrs['href'].replace('https://www.google.com/url?q=', '')
            texto = a.text
            lista.append({'texto':texto, 'link': link})
        else:
            lista.append(d.text)
    datos.append(lista)


output = []
l = [''] * 11
regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
for fila in datos:
    res = l[:]
    for n, d in enumerate(fila):
        if isinstance(d, dict):
            res[n] = d.get('texto')
            link = d.get('link')
            link = urllib.parse.unquote(link)
            if n == 2:
                match = regex.match(link)
                if match:
                    link = match.group('id')
                    res[-4] = link
                else:
                    p = urlparse(link)
                    if p.query:
                        q = parse_qs(p.query)
                        if q.get('video_id'):
                            res[-4] = q.get('video_id')                
            elif n == 3:
                res[-3] = link.split('&')[0]
                # res[n] = urlparse(res[n]).path.split('/')[-1]
                
            else:
                link = link.split('&')[0]
                #print(link)
                res[-2] = link
        else:
            
            if n == 1 and 'Tutorial:' in d:
                res[n] = 'Tutorial'
                res[10] = d.replace('Tutorial:', '').strip()
            else:
                res[n] = d
    output.append(res)

w = csv.writer(open('improvisor.csv', 'w'))
h = ['id',
 'Category',
 'label',
 'Leadsheet',
 'Date',
 'Poster',
 'Comments',
 'title_url',
 'ls_url',
 'poster_url',
 'grade_tutorial']
w.writerow(h)
w.writerows(output[2:])

lista_dicts = [dict(zip(h, l)) for l in output[2:]]
datos = [{k: v for k, v in d.items() if v } for d in lista_dicts]    

ruta = 'docs/improVisor/index.html'
data = json.dumps({'items': datos})
schema = json.load(open('schema.json'))
schema = json.dumps(schema)
template = open('index_improvisor.html').read()
open(ruta, 'w').write(template.format(data=data, schema=schema))
