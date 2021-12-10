#Simula el tiro de una moneda para 1, 10,100,1000 y 10000intentos.Mostrar el porcentaje de ocurrencia de cara y seca.
import random

moneda = ["cara","seca"]
cont_cara= 0
cont_seca = 0

for i in range(1):
     eleccion = random.choice(moneda)
     if eleccion == "seca":
         cont_seca+=1
     else:
         cont_cara+=1

print(cont_seca)
print(cont_cara)


for i in range(10):
     eleccion = random.choice(moneda)
     if eleccion == "seca":
         cont_seca+=1
     else:
         cont_cara+=1
print(cont_seca)
print(cont_cara)

for i in range(100):
     eleccion = random.choice(moneda)
     if eleccion == "seca":
         cont_seca+=1
     else:
         cont_cara+=1
print(cont_seca)
print(cont_cara)

for i in range(1000):
     eleccion = random.choice(moneda)
     if eleccion == "seca":
         cont_seca+=1
     else:
         cont_cara+=1

print(cont_cara)