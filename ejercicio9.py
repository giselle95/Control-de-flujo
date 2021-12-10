#Ingresar 10 valores por telado. Indicar cual fue el mayor y en que posicion entro.
numero = int(input("Ingrese el nro:\n"))
mayor = numero
posicion = 0
for i in range(0 , 10):
 
    if numero > mayor:
        mayor = numero
        posicion = i
    numero = int(input("Ingrese el nro:\n"))

    print(f"El mayor es {mayor} y entro en la posicion {posicion+1}")