# Se ingresaran números positivos enteros. Determinar cuántos de estos son paras. El ingreso finalizará con un número negativo.

numero = int( input("Ingrese un nro positivo:\n"))

while numero > 0:
    par = numero % 2
    
    if par == 0:
        print( " Es par")
    numero = int( input("Ingrese un nro positivo:\n"))