#Permitir el ingreso de una clave numerica entera. Finalizar el ingreso  solamente cuando la clave ingresada sea 23645.

#esta es una prueba
clave = input("Ingrese la clave : \n")
bloqueo = False

while bloqueo == False:
    
    if clave == 23645:
        bloqueo = True
    else:
        clave = int(input("Ingrese la clave : \n"))

    
    