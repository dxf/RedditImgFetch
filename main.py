import json
import urllib3
urllib3.disable_warnings()
url = 'https://old.reddit.com/r/test/random.json'
http = urllib3.PoolManager()
suffix = ['.jpg','.png','.gif','.bmp']
while True:
    response = http.request('GET',url)
    thedata = response.data
    parsedjson = json.loads(thedata)
    thefinalurl = parsedjson[0]['data']['children'][0]['data']['url']
    if thefinalurl.endswith('.png') or thefinalurl.endswith('.jpg') or thefinalurl.endswith('.gif'):
        # Do what you want with the variable here! :) e.g:
        print(thefinalurl)
        break
    else:
        print('Not an image')
