def load(imagen,angle=0,tx=0,ty=0,s=1):

    import cv2
    import numpy as np


    ##angle=10
    ##tx=0
    ##ty=0

    alto, ancho, canales = imagen.shape
    
    ampliada = np.zeros([s*alto,s*ancho,canales], dtype = int)

    escala = np.matrix([[s, 0, 0],
                        [0, s, 0],
                        [0, 0, 1]])
    
    escala_inv = np.linalg.inv(escala)
    
    alto2, ancho2, canales = ampliada.shape


    for i in range(alto2): #recorre la matriz y los colores
        for j in range(ancho2):
                dest = np.array([[i],[j],[1]])  # guarda las coordenads
                                                #originales del pixel
                origx,origy,uno = escala_inv.dot(dest)    #aplica la transf
                origx = int(origx)      #paso a int      
                origy = int(origy)
                
                if ((origy < ancho) and (origx < alto) and (origy > 0)and(origx > 0)):
                    for k in range(canales):
                                ampliada[i,j,k]=imagen[origx,origy,k]
    
    cv2.imwrite('imgampli.png',ampliada)
    
    angle = angle*2* np.pi /360

 #   imagen = cv2.imread("cuadro.jpg") ## imagen a editar
    copia = ampliada.copy()   ## hago una copia para restaurar

    copia = copia[:,:,0]

    # matriz de giro sobre (0,0) y translacion
    A = np.matrix ([[np.cos(angle) , np.sin(angle), tx],
                    [-np.sin(angle), np.cos(angle), ty],
                    [0 , 0, 1]])

    alto, ancho = copia.shape #obtiene las dimensiones de la imagen

    #las siguientes son matrices necesarias
    #para girar sobre el centro de la imagen
    T1 = np.matrix ([[1, 0, ancho/2],
                     [0, 1, alto/2],
                     [0, 0, 1]])

    T2 = np.matrix ([[1, 0, -ancho/2],
                     [0, 1, -alto/2],
                     [0, 0, 1]])

    ## x' = x * T1*A*T2
    ## x' = x * B

    B = T1.dot(A.dot(T2)) #crea la matriz de transf T1*A*T2
                  
    print('Matriz de transformación') #Imprime la matriz de transf
    print(B)


    destino = np.zeros_like(ampliada)
    #cv2.imshow('image',destino)         #crea un fondo sobre el que
    #cv2.imwrite('fondo.png',destino )  #imprimir la transformacion

    for i in range(alto2): #recorre la matriz y los colores
        for j in range(ancho2):
            
                orig = np.array([[i],[j],[1]])  # guarda las coordenads
                                                #originales del pixel
                destx,desty,uno = B.dot(orig)    #aplica la transf
                destx = int(destx)      #paso a int      
                desty = int(desty)
                
                if ((desty < ancho) and (destx < alto) and (desty > 0)and(destx > 0)):
                    for k in range(3):
                                destino[i,j,k]=ampliada[destx,desty,k]

    #cv2.imshow('transformada',destino)
    cv2.imwrite('imagen_transformada.png',destino )


    return 0


