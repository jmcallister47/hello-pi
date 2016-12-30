#!/usr/bin/env python 
import httplib, urllib, base64
import sys

file = open('../api-key.txt','r')
key = file.read().strip()
file.close()
personGroupId = str(sys.argv[1])

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
}

params = urllib.urlencode({
    'personGroupId':str(personGroupId)
})

body = {
    'name':str(personGroupId)
}

conn = httplib.HTTPSConnection('api.projectoxford.ai')
conn.request("PUT", "/face/v1.0/persongroups/{personGroupId}?%s" % params, str(body), headers)
response = conn.getresponse()
data = response.read()
dataFile = open('../person-group-id.txt','w')
dataFile.write(str(personGroupId))
dataFile.close()
print(data)
conn.close()
