#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#ejecutar como $python framerate.py video.mp4
#
import sys
import cv2
##if(len(sys.argv)>1):
##    filename = sys.argv[1]
##else:
##    print('Ingrese un nombre de archivo') #si no se pasa parametro muestra este mensaje
##    sys.exit(0)

filename = "video.mp4"

cap = cv2.VideoCapture(filename)

fourcc =cv2.VideoWriter_fourcc(*'X264')

framesize = (int(cap.get(3)),int(cap.get(4))) #obtiene el ancho y alto del video


print("Dimensiones:",framesize[0],"x",framesize[1])

framerate = (int(cap.get(5)))
print(framerate, "fps")

out = cv2.VideoWriter('output.mp4',fourcc,framerate,framesize) #archivo de salida

delay = int(1000/framerate) #delay para framerate obtenido

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
