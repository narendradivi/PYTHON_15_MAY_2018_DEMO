import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for c in countries:
    print ("%-50s %-20s  %d" %(c['name'][0:50], c['capital'], c['population']))


