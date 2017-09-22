# This is a cleaner version of picture_comparsion3.py
#import cv2
import requests
import pprint
import numpy as np
import time
import os
import picamera

def getFilenamesAndClasses(dataset_dir_raw):
    """ Returns list of image file paths relative to the provided raw dataset directory
        dataset_dir_raw: directory containing subdirectories of JPEGS to use for training
        ex: hand -> rock, paper, scissors
        subdirectories represnt class names
    """
    root_dir = dataset_dir_raw
    directories = []
    classNames = []
    for filename in os.listdir(root_dir):
        path = os.path.join(root_dir, filename);
        if os.path.isdir(path):
            directories.append(path)
            classNames.append(filename)

    photoFilenames = []
    for directory in directories:
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            photoFilenames.append(path)
    return photoFilenames

block = True

while block == True:
    print "            Welcome to Face Detection System"
#    print "To enter, your face must be registered in the database. After the camera shows up, press 'q' to see if you can enter."


    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(0)
        camera.capture('./capture.jpg')
        camera.stop_preview()
#    cap = cv2.VideoCapture(0)
#
#    while(True):
#        ret, frame = cap.read()
#        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
#        cv2.imshow('frame', rgb)
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            out = cv2.imwrite('capture.jpg', frame)
#            break
#    cap.release()
#    cv2.destroyAllWindows()

    def compare(face1, face2):
        """
        compare face 1 to face 2 - is face 1 = face2?
        """
        payload = {'api_key': 'xT_4ChJTosLQPrxmIPq444uaBp4I8dzM', 'api_secret': 'FKSgyp50IMSCm8d7PdRXQmWDUW0mO4PO'}
        picture_payload1 = {'image_file1': open(face1, 'rb'), 'image_file2': open(face2, 'rb')}
        r = requests.post('https://api-us.faceplusplus.com/facepp/v3/compare', params=payload, files=picture_payload1)
#        pp = pprint.PrettyPrinter(indent=4)
#        pp.pprint(r.json())
        data = r.json()
        face1=data["faces1"]
        if (len(face1)==0):
            return -1
        else:
            confidence = data["confidence"]
            if confidence >= 60:
                return 1
            else:
                return 0

    access = False

    path = os.getcwd()
    picture = path + "/capture.jpg"

    pictures_faces_path = path + "/test/pictures_faces"
    pictures_faces = os.listdir(pictures_faces_path)

    for face in pictures_faces:
        isPerson = compare(picture, path + "/test/pictures_faces/{0}".format(face))
        if (isPerson ==1):
            access = 1
	    break
        elif (isPerson ==-1):
            access =-1
            break


    if access == 1:
        print "You are {0}.".format(face)
        block = False
    elif access ==0:
        print "Your face isn't in the database right now. Would you like to add it?"

        decision1 = raw_input("> ")

        if decision1 == "yes" or decision1 == "Yes":
            print "Please enter the Lab password:"

            decision2 = raw_input("> ")

            if decision2 == "homework":
                print "Okay, what is your name?\v"

                person_name = raw_input("> ")

                print "Face the camera. Your picture will be taken in 5."

#                camera_port = 0
#                camera = cv2.VideoCapture(camera_port)
#                time.sleep(5.0)
#                return_value, image = camera.read()

                path = path + '/test/pictures_faces/'

                with picamera.PiCamera() as camera:
                    camera.start_preview()
                    time.sleep(0)
                    camera.capture(str(path) + "{0}.png".format(person_name))
                    camera.stop_preview()

#                path = path + '/test/pictures_faces/'
#                cv2.imwrite(str(path) + "{0}.png".format(person_name), image)
#                del(camera)

                print "\vYour face is saved to the database."
                block = False
            else:
                print "Access denied"
                block = False
        else:
            print "Access denied"
            block = False
    else:
        print "no face detected -"
        block = False
