# -*- coding: utf-8 -*- 
#!/usr/bin/env python
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
    

