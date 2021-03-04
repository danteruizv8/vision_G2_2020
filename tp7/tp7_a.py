#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Transformación afín - Incrustando imágenes
import cv2
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)

pto1, pto2, pto3 = (-1,-1), (-1,-1), (-1,-1)
punto = 1

def seleccion(event, x, y, flags, param):
    global punto, pto1, pto2, pto3, img
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Se oprimió el botón")
        if punto == 1:
            pto1 = x, y
            cv2.circle(img, pto1, 3, (255, 0, 0), 2)
        elif punto == 2:
            pto2 = x, y
            cv2.circle(img, pto2, 3, (0, 255, 0), 2)
        elif punto == 3:
            pto3 = x, y
            cv2.circle(img, pto3, 3, (0, 0, 255), 2)
        punto += 1
        cv2.imshow("imagen", img)

def imgafin(imagen, r_altura, r_ancho):
    inicio = np.array([pto1, pto2, pto3], dtype=np.float32)
    destino = np.array([(0, r_altura), (0, 0), (r_ancho, 0)], dtype=np.float32)
    matriz = cv2.getAffineTransform(inicio, destino)
    result = cv2.warpAffine(imagen, matriz, (r_ancho, r_altura))
    return result
try:
    img = cv2.imread(path+"/rotulos.jpg", cv2.IMREAD_COLOR)
    original = img.copy()
    cv2.namedWindow("imagen")
    cv2.setMouseCallback("imagen", seleccion)
    print("Seleccione 3 puntos, presione 'a' cuando termine para mostrar las sandias.")
    print("Para volver a seleccionar los puntos presionar R")
    Size_xy = img.shape
    print("Size: ", Size_xy)
    while(True):
        cv2.imshow("imagen", img)
        tecla = cv2.waitKey(0) & 0xFF
        if tecla == ord("a"):
            rAl = int(input("Ingrese el alto de la imagen de salida que quiere generar\n"))
            rAn = int(input("Ingrese el ancho de la imagen de salida que quiere generar\n"))
            print("Guardando imagen resultado.png")
            result = imgafin(img, rAl, rAn)
            cv2.imwrite(path+"/resultado.png", result)
            cv2.namedWindow("resultado")
            cv2.imshow("resultado", result)
        elif tecla == ord("r"):
            print("Restaurando imagen:")
            img = original.copy()
            punto = 1
            p1, p2, p3 = (-1,-1), (-1,-1), (-1,-1)
            cv2.destroyWindow("resultado")
        elif tecla == ord("q"):
            print("Exit.-\n")
            break
    cv2.destroyAllWindows()
except Exception as e:
    print("Excepcion: %s", e)
    cv2.destroyAllWindows()