# -*- coding: utf8 -*-
#!/usr/bin/env python
import urllib.request
stream_url = 'http://pub1.di.fm/di_classictrance'
request = urllib.request.Request(stream_url)
try:
    request.add_header('Icy-MetaData', 1)
    response = urllib.request.urlopen(request)
    icy_metaint_header = response.headers.get('icy-metaint')
    if icy_metaint_header is not None:
        metaint = int(icy_metaint_header)
        read_buffer = metaint+255
        content = response.read(read_buffer)
        title = content[metaint:].split("'")[1]
    print (title)
except:
        print ('Error')
