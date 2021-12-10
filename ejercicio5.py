#Repetir el ejercicio anterior permitiendo solo 3 intentos. Luego del tercer intento fallido colocar una advertencia. 

clave = input("Ingrese la clave : \n")
bloqueo = False
cont = 1
while bloqueo == False:
    
    if clave == 23645:
        bloqueo = True
    else:
        cont+=1
        clave = int(input("Ingrese la clave : \n"))
    if cont == 3:
        print("Ya marcaste 3 veces mal la clave")
        bloqueo = True