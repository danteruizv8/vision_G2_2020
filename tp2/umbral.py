#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

figura =cv2.imread('hoja.png',0) #archivo a modificar

#imread cre una matriz 3D: row (height) x column (width) x color[BGR] (3)
#con el argumento "0" lee en escala de grises.Entonces queda una matriz 2D:
#row (height) x column (width) x  Black (1)

cv2.imwrite('resultado_lectura.png',figura ) #imagen leida

umbral=200 #Nivel de colores

alto, ancho = figura.shape #obtiene las dimensiones de la imagen

for i in range(alto): #recorre la matriz y binariza los colores
    for j in range(ancho):
        if(figura[i,j] < umbral):
            figura[i,j] = 0
        else:
            figura[i,j] = 255


cv2.imwrite('resultado.png',figura ) #imagen transformada
