#!/usr/bin/env python
import httplib, urllib, base64
import sys, json

file = open('api-key.txt')
key = file.read().strip()
file.close()
name = str(sys.argv[1])
jsonData = json.loads(urllib.urlopen('people.json').read())
personId = str(jsonData["recognized"][name])
imageLocation = str(sys.argv[2])

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key':str(key),
}

params = urllib.urlencode({
    # Request parameters
    'personGroupId':'recognized',
    'personId':str(personId),
})

body = ""
#load image
f = open(imageLocation, "rb")
body = f.read()
f.close()

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
