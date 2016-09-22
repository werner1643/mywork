# -*- coding: utf-8 -*- 
#!/usr/bin/env python
#ICY 200 OK icy-notice1:
#This stream requires Winamp
#icy-notice2:SHOUTcast Distributed Network Audio Server/Linux v1.9.8
#icy-name:Buddha
#icy-genre:
#icy-url:http://www.buddharadio.com
#content-type:audio/aac
#icy-pub:0
#icy-metaint:32768
#icy-br:32
#import urllib.request 

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
    
    
    opener = urllib.request.build_opener()
    data=opener.open(request)
    headers=True
    while headers:
        line = data.readline()
        if line[0:11]=="icy-metaint":
            interval = int(line[13:])

            if line=="\r\n":
                headers=False

                data.read(interval)
                len=ord(data.read(1))*16
                print "Meta data is",len
                print data.read(len)
