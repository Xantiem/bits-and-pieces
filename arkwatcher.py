import urllib.request
import json
import datetime
import ctypes

a = urllib.request.urlopen('http://wiredcat.hopto.org/WiredcatGenesis2/ASV_Players.json')
b = json.loads(a.read())

max_c = len(b)
c = 0

while c < max_c:
    if b[c]['playerid'] == 659814353:
        p_line = c
    c += 1

t = b[p_line]["active"][:10].split('-')


date = datetime.datetime(int(t[0]), int(t[1]), int(t[2]))

new_date = date + datetime.timedelta(days=48)

print(new_date.strftime("%Y/%m/%d"))

    
