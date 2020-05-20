#def transforma(figura,angle, tx, ty)

import cv2
import numpy as np


angle=10
tx=0
ty=0

angle = angle*2* np.pi /360

imagen = cv2.imread("cuadro.jpg") ## imagen a editar
copia = imagen.copy()   ## hago una copia para restaurar

copia = copia[:,:,0]



A = np.matrix ([[np.cos(angle), np.sin(angle), tx],
           [-np.sin(angle), np.cos(angle), ty],
            [0,0,1]])

alto, ancho = copia.shape #obtiene las dimensiones de la imagen


T1 = np.matrix ([[1, 0, ancho/2],
               [0, 1,alto/2],
               [0, 0, 1]])

T2 = np.matrix ([[1, 0, -ancho/2],
               [0, 1,-alto/2],
               [0, 0, 1]])

## x' = x * T1*A*T2
## x' = x * B

B = T1.dot(A.dot(T2))
              



tam = np.array([[alto],[ancho],[1]])


print('Matriz de transformación')
print(B)


destino = np.zeros_like(imagen)
cv2.imshow('image',destino)
cv2.imwrite('fondo.png',destino )

for i in range(alto): #recorre la matriz y binariza los colores
    for j in range(ancho):
        for k in range(3):
            orig = np.array([[i],[j],[1]])
            #print(orig)
            #print('//-------')
            destx,desty,uno = B.dot(orig)
            destx = int(destx)
            desty = int(desty)
            uno = int(uno)
            if ((desty < ancho) and (destx < alto) and (desty > 0)and(destx > 0)):

                            destino[destx,desty,k]=imagen[i,j,k]

cv2.imshow('image',destino)
cv2.imwrite('fondo.png',destino )


#return 
