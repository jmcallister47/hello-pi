#! /usr/bin/env python
import numpy as np
import cv2
import subprocess

def main():
    iteration = 1
    while(True):
        print "starting picture 1"
        takePicture()
        print "took picture " + str(iteration)
        if(localFaceDetection('tmp/image.jpg')):
            print "detected face"
            command = "~/hello-pi/api-trainer/identify.py ~/hello-pi/face-detection/tmp/image.jpg"
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            print output
        else: 
            print "detected no faces"

def takePicture():
    command = "sudo raspistill -o tmp/image.jpg"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

'''Detect if image contains faces'''
def localFaceDetection(imageLocation):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(imageLocation)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 0:
        return True
    return False

if __name__ == "__main__":
    main()
