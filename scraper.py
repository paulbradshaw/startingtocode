import urllib, json, scraperwiki

url = "https://data.police.uk/api/stops-force?force=west-midlands"
response = urllib.urlopen(url)
data = json.loads(response.read())

record = {}
#print data
index = 0
for i in data:
    index = index+1
    record['index'] = index
    print i['age_range']
    record['age'] = i['age_range']
    record['datetime'] = i['datetime']
    scraperwiki.sqlite.save(['index'], record)
