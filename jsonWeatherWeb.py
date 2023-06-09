import json
from urllib.request import urlopen
url = "https://api.weather.gov/alerts/active?area=MI"
response = urlopen(url)
data = json.loads(response.read())
print("got data")


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

file_loc = '/Users/aaronstark/Documents/dev/job/alerts.json'
with open(file_loc, 'a') as outfile:
    json.dump(alerts, outfile)

