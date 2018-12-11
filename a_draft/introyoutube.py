import json
from urllib.request import urlopen
url = "https://infowars.com"
response = urlopen(url)


for video in data['feed']['entry']['0:6']:
    print(video['title']['$t'])
