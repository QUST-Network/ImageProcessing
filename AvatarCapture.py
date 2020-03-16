import cv2
import sys
import os.path
from glob import glob

def detect(filename, cascade_file="lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(48, 48))
    for i, (x, y, w, h) in enumerate(faces):
        face = image[y: y + h, x:x + w, :]
        #face = cv2.resize(face, (96, 96))
        face = cv2.resize(face, (960, 960))
        save_filename = '%s-%d.jpg' % (os.path.basename(filename).split('.')[0], i)
        cv2.imwrite("Data/" + save_filename, face)

if __name__ == '__main__':
    if os.path.exists('Data') is False:
        os.makedirs('Data')
    file_list = glob('IMG/*.jpg')
    for filename in file_list:
        detect(filename)