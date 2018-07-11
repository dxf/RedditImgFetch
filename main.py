import json
import urllib3
import webbrowser
urllib3.disable_warnings()
url = 'https://old.reddit.com/r/pics/random.json'
http = urllib3.PoolManager()
response = http.request('GET',url)
thedata = response.data
parsedjson = json.loads(thedata)
thefinalurl = parsedjson[0]['data']['children'][0]['data']['url']
webbrowser.open(thefinalurl)
