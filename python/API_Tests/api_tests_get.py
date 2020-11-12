import requests
import json

url = 'http://httpbin.org/get'
args = {'curso':'Python_API','nome':'Hildebrando'}

response = requests.get(url, params=args)

if response.status_code == 200:
    # response_json = response.json()
    # origin = response_json['origin']
    # print(origin)

    # Using json library:
    response_json = json.loads(response.text)
    origin = response_json['origin']
    print(origin)
    
    





# file = open('google.html', 'wb')
# file.write(content)
# file.close()
