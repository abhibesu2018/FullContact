import json
from urllib.request import urlopen
API_KEY = "API_KEY"
EMAIL_ID = "EMAIL_ID"
url = 'https://api.fullcontact.com/v2/person.json?apiKey='+API_KEY+'&email='+EMAIL_ID
urlData = urlopen(url).read().decode('utf-8')
loadedJson = json.loads(urlData)
print(json.dumps(loadedJson, indent=3))
