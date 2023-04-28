#Sistemas de Numeracion
#111
print(0b111) #-> binario
print(0o111) #-> octal
print(111)#-> decimal
print(0x111) #-> hex


print("---------------")
#Convertir de decimal a otro sistema de numeracion
print(oct(44))
print(hex(273))
print(bin(273))
print(hex(786))
print(oct(234))
print(hex(99))
print("---------------------------------------------")
#Representando numeros decimales, punto flotantes, de punto flotantes
print(.4)
print(-2.5+2)
print(0.4)
#Notaciones cientificas 

print(5e3)
print(5.5e3)
print(5e-3)
print(-5e3)
print(8e10)
print(-8e7)
#Se pone "E" por exponentes elevados


#Cadenas de texto 
print("hola")
print("Hola a todos")
print("Hola")
#Strings
print("Leo", "La pulga", "Messi")
print("Hola amigos")

#George Boole
#True False 
#Valores Booleanos

print(10>5)
print(10>100)
print(1<0)
print("------------")

print("hola"== "hola") 
print("Hola"== "Hola")
print("---------")
print("Auto"!= "Bus")

#Operaciones aritmeticas
print(5+5)
print(5-5)
print(10*5)
print(5/5)

#Exponentes 
print(3**2)
print(2**3**2) #2^3^2
print((2**3)**2) #2^(3)^2


print("-------------")


#Divisiones Enteras
print(6//3)
print(6.0//3)
print(6//-4)
print(6 / -4)


print("----------------------")

#Operador de residuo
#% residuo
print(18 % 2)
print(19 % 2)

#Se utliza para saber si un numero es par o impar
#Tambien para conversion de unidades

#kilometros a metros

#1km -> 1000m
#Cuantos km equivalen 2500 mts
print("equivalen a", 2500/1000, "kms")


#Cuantos dias hay en 1500 minutos
print(1500%1440, "minutos extra")
print(1500 // 1440)
print("1500 minutos equivalen a:", (1500 // 1440), "dia y ", end="")
print(1500 % 1440,"minutos")