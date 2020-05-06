import cv2
import numpy as np

drawing = False # true if mouse is pressed

ix,iy = -1,-1

imagen = cv2.imread("cuadro.jpg") ## imagen a editar
copia = imagen.copy()   ## hago una copia para restaurar

# funcion que llama el mouse
def seleccionar(event,x,y,flags,param):
  global ix,iy,drawing,mode,sub_img

  if event == cv2.EVENT_LBUTTONDOWN: ## marco el inicio de la seleccion
      drawing = True
      ix,iy = x,y

  elif event == cv2.EVENT_MOUSEMOVE: ##cuando selecciono/arrastro el mouse
    if drawing == True:
            if iy < y :  # a, b, c y d ordenan las coord. de menor a mayor
                a = iy   # independientemente del sentido que se mueva el mouse
                b = y
            else:
                a = y
                b = iy
            if ix < x :
                c = ix
                d = x
            else:
                c = x
                d = ix
            sub_img = copia[a:b, c:d] ## traigo del respaldo una copia de la seleccion

                ## creo otro rectangulo para fusionar y dar efecto opaco a la seleccion
            white_rect = np.ones(sub_img.shape, dtype=np.uint8) * 255
            
            res = cv2.addWeighted(sub_img, 1.0, white_rect, 0.25,1)     # 25% de opacidad

            cv2.rectangle(imagen,(ix,iy),(x,y),(0,255,0),2)     #va dibujando el rectangulo verde

            imagen[a:b, c:d] = res      #relleno rect con seleccion opaca


  elif event == cv2.EVENT_LBUTTONUP:
    drawing = False # finaliza la seleccion
    cv2.rectangle(imagen,(ix,iy),(x,y),(0,255,0),2) # dibuja el rect. seleccionado


cv2.namedWindow('image')  ## creo ventana para imagen
cv2.setMouseCallback('image',seleccionar) #llamo a los eventos del mouse en la ventana

while(1):
 cv2.imshow('image',imagen) #muestro imagen en la ventana
 k = cv2.waitKey(1) & 0xFF
 if   k == ord("g"):
        cv2.imwrite('seleccion.png',sub_img ) #guarda imagen seleccionada
 elif k == ord("r"):
        imagen = copia.copy()   ## restaura de la copia original
 elif k == ord("q"):            ## finaliza con q
    break


cv2.destroyAllWindows()   # elimino ventana
