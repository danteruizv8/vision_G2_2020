#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#ejecutar como $python framerate.py video.mp4
#
import sys
import cv2
if(len(sys.argv)>1):
    filename = sys.argv[1]
else:
    print('Ingrese un nombre de archivo') #si no se pasa parametro muestra este mensaje
    sys.exit(0)

cap = cv2.VideoCapture(filename)

fourcc =cv2.VideoWriter_fourcc('X','V','I','D')

framesize = (640,480) #tamagno de video forzado

out = cv2.VideoWriter('output.avi',fourcc,20.0,framesize) #archivo de salida

delay = 33 #delay para framerate

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow('image_gray', gray)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
