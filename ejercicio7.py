#mostrar los primeros 5 números perfectos.
numero = int(input("Ingresa un nro:\n"))
perfecto = 0
nros_suma = [perfecto]

for i in range(1,numero):
    
    busqueda_perfecto = numero % i 
        
    if busqueda_perfecto == 0:
        perfecto += i
        nros_suma.append(i)
      
if perfecto == numero:
    print("es perfecto")
    print("Los nros son:")
    for i in range(1,len(nros_suma)):
        if i <= 5:
         print(f"{nros_suma[i]}")
