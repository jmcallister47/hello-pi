#!/usr/bin/env python 
import httplib, urllib, base64
import sys

file = open('../api-key.txt')
key = file.read().strip()

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
}

params = urllib.urlencode({
})

body = {
    "name":str(sys.argv[1]),
}

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/persongroups/recognized/persons?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    dataFile = open('../people.txt',a)
    dataFile.write("Name: " + str(sys.argv[1]))
    print(type(data))
    print(data)
    dataFile.write(data)
    dataFile.close()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
