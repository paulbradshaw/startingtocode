#import libraries
import urllib, json, scraperwiki

#Change this URL to another - as long as it's an API that supplies JSON
url = "https://data.police.uk/api/stops-force?force=west-midlands"
#Grab the page at the URL, store in a variable
response = urllib.urlopen(url)
#Use that variable, and load the JSON in it, store in another variable
data = json.loads(response.read())

#Create an empty dictionary - to store data below
record = {}
#Create a counter, set at zero for now
index = 0
#Begin a for loop to go through data (which is a list of JSON)
for i in data:
    #Increase the counter by zero
    index = index+1
    #Store in that dictionary variable under the key 'index'
    record['index'] = index
    #Print just to test we're getting things right
    print i['age_range']
    #Store the age_range branch of that JSON in the dictionary variable under the key 'age'
    record['age'] = i['age_range']
    #Repeat for datetime branch
    record['datetime'] = i['datetime']
    #Save the whole dictionary in a sqlite database; use the index key as the primary key
    scraperwiki.sqlite.save(['index'], record)
