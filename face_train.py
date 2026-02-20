import os
import cv2 as cv
import numpy as np

people = ['Michael scott']

p = []

DIR = r'C:\Users\Firulais\Documents\Repositorios\GitHub\Image_Recognition\Resources\Photos\Faces'

haar_cascade = cv.CascadeClassifier('./haar_face.xml')


features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        labels = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(labels)
                
                #cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
                #cv.putText(frame, f'Face {i+1}',(x+w, y+h), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), thickness=2)

#for i in os.listdir(r'C:\Users\Firulais\Documents\Repositorios\GitHub\Image_Recognition\Resources\Photos\MichaelScott'):
#    p.append(i)

create_train()
print('Training done ---------------------')

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
print('Before training ------------------------')
face_recognizer.train(features, labels)

print('End program ------------------------')
print (p)