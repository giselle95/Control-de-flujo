#determinar si un nro entero positivo ingresado  por teclado es o no un nro merfecto. Los numeros perfectos son aquellos 
# cuyos valor es igual a la suma de todos sus divisores exactos con excepción del mismo numero, por ejemplo 6 = 1 + 2 + 3 


numero = int(input("Ingresa un nro:\n"))
perfecto = 0
for i in range(1,numero):
    
    busqueda_perfecto = numero % i 
        
    if busqueda_perfecto == 0:
        perfecto += i
      
if perfecto == numero:
    print("es perfecto") 