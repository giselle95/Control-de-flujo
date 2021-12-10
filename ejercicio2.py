#Se ingresaran 100 numeros enteros. Sumar los de orden impar por un lado y los de orden par por otro. Determinar cuales proporcionan la mayor suma. 



cont_par = 0
cont_impar = 0
numero = int(input("Ingrese los numeros:\n"))

for i in range(10) :
      
    par = numero % 2
    
    if par == 0:
        cont_par += numero
    else:
        cont_impar += numero
    numero = int(input("Ingrese los numeros:\n"))
        

print(f"La suma de los numeros pares es : {cont_par} y de los numeros impares es {cont_impar}")
