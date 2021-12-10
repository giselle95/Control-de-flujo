#Se ingresaran numeros enteros hasta que se ingrese el 235. Indicar cuantas veces ocurrio el ingreso del numero 23. 

numero = int(input("Ingrese un numero:\n"))
cont = 0
while numero != 235:
    if numero == 23:
        cont+=1
    numero = int(input("Ingrese un numero:\n"))
print(f"Las veces que se puso 23 son:{cont}")