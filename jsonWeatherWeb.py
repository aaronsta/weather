import json
from urllib.request import urlopen
url = "https://api.weather.gov/alerts/active?area=MI"
response = urlopen(url)
data = json.loads(response.read())
#print(data)
#f = open('weatherAll.json')
#f = open('weather04142023.json')  
# returns JSON object as 
# a dictionary
#data = json.load(f)

data_lower = data["features"]
alerts = []
for item in data_lower:
    onset = item["properties"]["onset"]
    geoc = item["properties"]["geocode"]["SAME"]
    headline = item["properties"]["headline"]
    desc = item["properties"]["description"]
    areadesc = item["properties"]["areaDesc"]
    #print(headline)
    #print(onset)
    if (("026163" in geoc) or ("026161" in geoc)):
        myDict = {"onset" : onset, "headline" : headline, "desc":desc, "areadesc":areadesc}
        alerts.append(myDict)

for alert in alerts:
    print(alert["onset"])
    print(alert["areadesc"])
    print(alert["headline"])
    print(alert["desc"])

with open('alerts.json', 'a') as outfile:
    json.dump(alerts, outfile)
    
# Closing file
#f.close() 
