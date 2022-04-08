#PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON
#Loriel Ramirez Sanchez

#PRACTICA I: VARIABLES, TIPOS DE DATOS,EXPRESIONES Y CONDICIONALES.

#Escriba un programa que:

#1- Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2

menorque = 4 < 2
print(type(menorque))

#2- Almacene en una variable el nombre de una persona 
# y al final muestre en la consola el mensaje: “Bienvenido [nombrePersona]”

nombrePersona = input("Ingrese un Nombre:")

print(f"Bienvenido {nombrePersona})

#3- Evalúe si un número es par o impar y muestre en la consola el mensaje. 

numero = int(input("Ingrese un Numero:"))

if numero % 2 == 0:
    print(f"El numero {numero} es Par")
else:
    print(f"El numero {numero} es Impar")


#4- Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse en la consola.
numero1 = int(input("Ingrese el Primer Numero:"))
numero2 = int(input("Ingrese el Segundo Numero:"))

if numero1 > numero2:
    print(f"el primer numero es mayor")
elif numero1 == numero2:
    print(f"Ambos numeros son iguales")
    
else:
    print(f"El Segundo numero es mayor")

#5- Convierta dólares a pesos.
cantDollar = int(input("Ingrese la cantidad en dollares:"))
cantPesos = 57.72
resultado = cantDollar * cantPesos

print(f"El resultado en pesos Dominicanos es: {resultado}")

#6- Convierta grados celsius a Fahrenheit
gradoC = int(input("Ingrese la Temperatura en Grados Celsius:"))
resultado = gradoC * 9/5 + 32
print(f"El Resultado en grado Fahrenheit es: {resultado} °F")

#7- Almacene cuatro notas 90,95,77,92 y las promedie. Al final debe decir su calificación en letras A,B,C,D,E ó F.
cal1 = int(input("Ingrese la Primera Calificacion:"))
cal2 = int(input("Ingrese la Primera Calificacion:"))
cal3 = int(input("Ingrese la Primera Calificacion:"))
cal4 = int(input("Ingrese la Primera Calificacion:"))
promedio = (cal1 + cal2 + cal3 + cal4)/4
print("Rango de calificacion Final:\n A = 90 - 100 \n B = 80 - 89\n C = 70 - 79\n D = 60 - 69\n F = 50 - 59")

if promedio >= 90:
    print(f"La calificacion final es: A ({promedio})")
elif promedio >= 80 and promedio < 89:
    print(f"La calificacion final es: B ({promedio})")
elif promedio >= 70 and promedio < 79:
    print(f"La calificacion final es: C ({promedio})")
elif promedio >= 60 and promedio < 69:
    print(f"La calificacion final es: D ({promedio})")
elif promedio >= 50 and promedio < 59:
    print(f"La calificacion final es: F ({promedio})")

#8- Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo 
# y calcule la cuota mensual. (Amortizar mediante el sistema francés)
 
monto = int(input("Ingrese el Monto:"))
cc = int(input("Ingrese la cantidad de Cuotas:"))
porcentaje = float(input("Ingrese el Porcentaje de interes anual de del prestamo:"))
porcent = porcentaje / 100

cuota = monto * ((porcent * ((1 + porcent) ** cc)) / (((1 + porcent) ** cc) - 1))
print(f"La cuota mensual es:{cuota}")
