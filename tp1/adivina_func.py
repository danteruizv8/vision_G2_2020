def adivina(max_intentos):   #recibe parametro cantidad de intentos permitidos
    import random
    numero = random.randint(0, 100)      #genera nro aleatorio entre 0 y 100
    #print(numero) #espiar numero

    running =True
    #max_intentos = 5 #para pruebas

    for i in range(0, max_intentos):    #repite hasta completar los inetntos
        respuesta = int(input('Ingrese un entero entre 0 y 100: '))
        if respuesta == numero:      #verifica el resultado
            print('Felicitaciones, adivinaste.')
            break
        else:
            if respuesta < numero:  #da pistas
                print('No, es un poco mayor')
            else:
                print('No, es un poco menor')
    else:
        print('Se alcanzaron los intentos permitidos.') #sale
    print('Fin del juego')

#adivina(5)
