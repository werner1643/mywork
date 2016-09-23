# -*- coding: utf-8 -*- 
#!/usr/bin/env python
#http://www.getinfo.ru/article545.html
#icy-name – название станции
#icy-genre – музыкальный жанр станции
#icy-pub - указывает допускает ли сервер публикацию себя в публичной директории (1 – да, 0 -нет)
#icy-br – битрейт потока
#icy-url - homepage потока
#icy-irc, icy-icq, icy-aim – контактная информация для публикации в публичной директории 

import urllib.request 

stream_url = 'http://185.50.24.141:8000/main_mp3_128'
request = urllib.request.Request(stream_url)

request.add_header('Icy-MetaData', 1)
response = urllib.request.urlopen(request)
icy_metaint_header = response.headers.get('icy-metaint')
if icy_metaint_header is not None:
    metaint = int(icy_metaint_header)
    read_buffer = metaint+255
    content = response.read(read_buffer)
    title = content[metaint:]
    print (title.decode('utf8', 'ignore').split("'")[1])
    print (title.decode('utf8', 'ignore').split("'"))
