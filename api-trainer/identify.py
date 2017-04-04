#!/usr/bin/env python
import httplib, urllib, base64
import sys, json

file = open('~/hello-pi/api-trainer/api-key.txt')
key = file.read().strip()

def main():
    faceIds = detect()
    personIds = []
    for faceId in faceIds:
        data = identify(faceId['faceId']) 
        if(len(data[0]['candidates']) > 0): #at least one recognized
            personIds.append(data[0]['candidates'][0]['personId'])
    peopleJsonData = json.loads(urllib.urlopen('people.json').read())
    peopleNames = []
    for personId in personIds:
        for key, value in peopleJsonData['recognized'].items():
            if(value == personId):
                peopleNames.append(key)
    print peopleNames    

def detect():
    headers = {
        'Content-type':'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key,
    }
    params = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'true',
    })
    body = ""
    imageLocation = str(sys.argv[1])
    image = open(imageLocation, "rb")
    body = image.read()
    image.close()
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse("")
    data = response.read()
    conn.close()
    jsonData = json.loads(str(data))
    faceIds = []
    for faceId in jsonData:
        faceIds.append(faceId)
    return faceIds

def identify(faceId):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }
    params = urllib.urlencode({
    }) 
    body = { 
        'personGroupId':'recognized',
        'faceIds':[
            str(faceId)
        ],
    }
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/identify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    jsonData = json.loads(str(data))
    return jsonData

if __name__ == "__main__":
    main()
