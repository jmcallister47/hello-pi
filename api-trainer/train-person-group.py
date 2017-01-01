#!/usr/bin/env python
import httplib, urllib, base64

file = open('api-key.txt','r')
key = str(file.read()).strip()
file.close()

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': key,
}

params = urllib.urlencode({
    'personGroupId':'recognized' 
})

conn = httplib.HTTPSConnection('api.projectoxford.ai')
conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/train?%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()
