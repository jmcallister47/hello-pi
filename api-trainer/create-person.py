#!/usr/bin/env python 
'''Name as argument. Ex. ./create-person.py "John Doe"'''
import httplib, urllib, base64
import sys, json, ast

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

conn = httplib.HTTPSConnection('api.projectoxford.ai')
conn.request("POST", "/face/v1.0/persongroups/recognized/persons?%s" % params, str(body), headers)
response = conn.getresponse()
data = response.read()
data = ast.literal_eval(data)
print(data)
jsonData = json.loads(urllib.urlopen('../people.json').read())
jsonData['list'].append({sys.argv[1]:data["personId"]}) #name:id
jsonFile = open('../people.json','w')
jsonFile.write(json.dumps(jsonData))
conn.close()
