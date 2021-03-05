import cv2
import numpy as np
import math

## Variables
l = 80      # lado del cuacrado en mm
esc = 2    # factor de escala pixels/mm
c = l*esc   # lado en pixels
osx =  50 #offset_x
osy =  50 #offset_y

p,x1,y1,x2,y2,i,medida=0,0,0,0,0,0,0
menu = "MENU: (m) medir  (g) guardar  (q) salir"

# Puntos de referencia obtenidos con tp8 sobre la imagen
puntos = np.float32([[ 27 , 465 ],[ 66 , 266 ],[ 268 , 267 ],[ 270 , 463 ]]);

xd = puntos[0,0]+osx    # corrimiento para evitar perdida de margenes
yd = puntos[0,1]+osy

# puntos de destino del mapeo
destino = np.float32([[ xd , yd ],[ xd , yd-c ],[ xd+c , yd-c ],[ xd+c , yd]]);

## Funciones 
 
# corrige proyeccion
def homografia(image,puntos,destino):
     (h, w) = image.shape[:2]
     M=cv2.getPerspectiveTransform(puntos,destino)
     rect=cv2.warpPerspective(image,M,(h+osy,w+osx))
     return rect
  
# marca puntos de medicion
def selec_p(event,x,y,flag,params):
	global p,x1,y1,x2,y2,long
	if event==cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img_transf,(x,y),3,(255,0,0),-1)
		cv2.imshow('Transformada',img_transf)
	if event==cv2.EVENT_LBUTTONUP:
		if p==0:
			(x1,y1)=(x,y)
		if p==1:
			(x2,y2)=(x,y)
			long=np.float32(math.sqrt((x2-x1)**2 + (y2-y1)**2)/esc)
			print("La longitud es ",long)
			print()
		p += 1

# auxiliar - suspende eventos del mouse
def dummy(event,x,y,flag,params):
   event==cv2.EVENT_LBUTTONDOWN
   event==cv2.EVENT_LBUTTONUP
   
# imprime texto en imagen a diferente altura
def texto(image,text,posy):
   fuente = cv2.FONT_HERSHEY_SIMPLEX
   linea = cv2.LINE_AA
   colort = (0, 250, 250)
   colorb = (10, 10, 10)
   pt1 = (10,4+posy)
   pt2 = ((10+11*len(text)),25+posy)
   image = cv2.rectangle(image, pt1, pt2, colorb, -1)
   image = cv2.rectangle(image, pt1, pt2, colort, 1)
   image = cv2.putText(image , text, (10,20+posy), fuente, 0.6, colort, 1 , linea)
   return image


img1 = cv2.imread('medir_1.jpg', 1)    # Carga imagen original
img_transf = homografia(img1, puntos, destino) #corrige
(h, w) = img1.shape[:2]
img_copy = img_transf.copy()     # Crea copia limpia

img1 = texto(img1, "Imagen Original",0)
cv2.imshow('Original', img1)
cv2.waitKey(2000)

cv2.namedWindow('Transformada')
img_transf = texto(img_transf, menu,h-10)
cv2.imshow('Transformada', img_transf)
print (menu)

while(1):

    k = cv2.waitKey(100) & 0xFF #verifica teclas precionadas
    
    if k == ord('m'):      # mide distancia entre dos puntos seleccionados
        
        img_transf = img_copy.copy()
        img_transf = texto(img_transf, "Elija dos puntos",0)
        cv2.imshow('Transformada',img_transf)
        cv2.setMouseCallback('Transformada',selec_p)
        p = 0
        while (1):
              
              k = cv2.waitKey(1) & 0xFF
              if p == 2:
                 img_transf = cv2.line(img_transf, (x1,y1), (x2,y2), (0,255,0), 2)
                 cv2.setMouseCallback('Transformada',dummy)
                 # Imprime valor medido
                 img_transf = texto(img_transf, "Longitud: "+str(long)+" mm",0)
                 img_transf = texto(img_transf, menu,h-10)
                 cv2.imshow('Transformada',img_transf) 
                 print (menu)
                 break

              
    elif k == ord('g'):  # Guarda imagen con la medicion
       cv2.imwrite('medida.png',img_transf)
       img_guardado = texto(img_transf, "Guardado...",h-100)
       cv2.imshow('Transformada',img_guardado) 
       
       
    elif k == ord('q'): # sale del programa
        break

cv2.destroyAllWindows()
