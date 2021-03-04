#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))
print(path)

p1, p2, p3 = (-1,-1), (-1,-1), (-1,-1)
punto = 1

def seleccion(event, x, y, flags, param):
    global punto, p1, p2, p3, img1
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Se oprimió el botón")
        if punto == 1:
            p1 = x, y
            cv2.circle(img1, p1, 3, (255, 0, 0), 2)
        elif punto == 2:
            p2 = x, y
            cv2.circle(img1, p2, 3, (0, 255, 0), 2)
        elif punto == 3:
            p3 = x, y
            cv2.circle(img1, p3, 3, (0, 0, 255), 2)
        punto += 1
        cv2.imshow("imagen1", img1)

def imagenafin(imagen, s1h, s1w):
    source = np.array([(0, imagen.shape[0]), (0, 0), (imagen.shape[1], 0)], dtype=np.float32)
    destination = np.array([p1, p2, p3], dtype=np.float32)
    matrix = cv2.getAffineTransform(source, destination)
    mask = np.zeros((s1h, s1w, 3), np.uint8)
    mask[:] = (255, 255, 255)
    res = mask * cv2.warpAffine(imagen, matrix, (s1w, s1h))
    return res

try:
    img1 = cv2.imread(path+"/LEO MESSI COLOR.jpg", cv2.IMREAD_COLOR)
    original = img1.copy()
    cv2.namedWindow("imagen1")
    cv2.setMouseCallback("imagen1", seleccion)
    img2 = cv2.imread(path+"/sandía-quebrada.jpg", cv2.IMREAD_COLOR)
    # cv2.namedWindow("imagen2")
    print("Seleccione 3 puntos, presione 'a' cuando termine para mostrar las sandias.")
    print("Para volver a seleccionar los puntos presionar R")
    xySize = img1.shape
    print("Size: ", xySize)
    while(True):
        cv2.imshow("imagen1", img1)
        #cv2.imshow("imagen2", img2)
        tecla = cv2.waitKey(0) & 0xFF
        if tecla == ord("a"):
            print("Guardando la imagen de salida.png")
            resultado = imagenafin(img2, img1.shape[0], img1.shape[1])
            # salida = cv2.addWeighted(img1, 0.5, resultado, 0.5, 0)
            resultGray = cv2.cvtColor(resultado, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(resultGray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            fondo = cv2.bitwise_and(img1, img1, mask=mask_inv)
            salida = cv2.add(fondo, resultado)
            cv2.imwrite(path+"/img/salida.png", salida)
            cv2.namedWindow("salida")
            cv2.imshow("salida", salida)
        elif tecla == ord("r"):
            print("Restaurar imagen")
            img1 = original.copy()
            punto = 1
            p1, p2, p3 = (-1,-1), (-1,-1), (-1,-1)
            cv2.destroyWindow("salida")
        elif tecla == ord("q"):
            print("Exit.-\n")
            break
    cv2.destroyAllWindows()
except Exception as e:
    print("Excepcion: %s", e)
    cv2.destroyAllWindows()
