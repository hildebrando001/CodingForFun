import requests

url = 'http://httpbin.org/post'
payload = {'curso':'Python_API','nome':'Hildebrando'}
headers = {'Content-Type': 'application/json', 'access-token': '12345'} # Tells to the server u're sending in a json format
# response = requests.post(url, data=payload) # all values will be into form attribute "form" :{}
# response = requests.post(url, data=json.dumps(payload)) # It goes to data attribute
response = requests.post(url, json=payload, headers=headers) #convert toa json object

print(response.url)

if response.status_code == 200:
    # print(response.content)
    headers_response = response.headers #Dic
    # print(headers_response)
    print(headers_response['Server'])