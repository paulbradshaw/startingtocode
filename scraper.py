import urllib, json

url = "https://data.police.uk/api/stops-force?force=west-midlands"
response = urllib.urlopen(url)
data = json.loads(response.read())
#print data
for i in data:
    print i
