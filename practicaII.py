#PRACTICA II PYTHON:
#Loriel Ramirez Sanchez

#1 – Realizar un programa que solicite al usuario un número indeterminado de números 
# (mientras se tecleen números que no sean cero). Al salir el programa debe dar en 
# pantalla el total de números dados y la suma de ellos.
total  =0
numero = int(input("Ingrese un número: "))

while numero != 0:
    total += numero
    numero = int(input("Ingrese un número: "))
print(total)


#2- Realizar un programa que presente un menú con las siguientes opciones
    #1- Convertir grados a Celsius a Fahrenheit
    #2- Convertir dólar a pesos
    #3- Convertir metros a pies
    #4- Salir
#Cada vez que finalice una de estas acciones debe regresar al menú. 
#El programa solo finalizará cuando el usuario elija la opción salir.

Opcion = ""
while Opcion != "4":
    print("MENU DE CONVERSIONES \n 1-Convetir Grados Celsius a Farenheit \n 2-Convertir Dollar a Pesos \n 3-Convertir Metros a pies \n 4-Salir")
    Opcion = input("Ingrese la Operacion a realizar:")

    if Opcion == "1":
        print("Converion de Grado Celsius a Farenheit")
        gradoC = int(input("Ingrese la Temperatura en Grados Celsius:"))
        resultado = gradoC * 9/5 + 32
        print(f"El Resultado en grado Fahrenheit es: {resultado} °F")
        
    elif Opcion == "2":
        print("Conversion de Dollar a Pesos")
        cantDollar = int(input("Ingrese la cantidad en dollares:"))
        cantPesos = 57.72
        resultado = cantDollar * cantPesos
        print(f"El resultado en pesos Dominicanos es: {resultado}")

    elif Opcion == "3":
        metro = int(input("Ingrese la Longitud en metro:"))
        pies = 3.28
        resultado = metro * pies
        print(f"El resultado en pies es: {resultado}")
    else:
        print(f"Gracias por Usar el sistema de conversiones")



#3- Hacer un programa que genere las tablas de multiplicar de los números múltiplos de 5 que hay entre 1 y 1000
tabla = 5
valor = 1
while valor <= 1000:
    print(tabla, "X", valor, "=", tabla * valor)
    valor = valor + 1


#4- Realizar un programa que reciba por teclado el sueldo de un empleado y 
# le aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

sueldo = int(input("Ingrese el sueldo del empleado:"))

#Calculo del AFP
ars = 0.0304
descars = sueldo * ars

#Calculo del AFP
afp = 0.0287
descafp = sueldo * afp

print (f"El descuento mensual de ARS es {descars}")
print (f"El descuento mensual de AFP es {descafp}")

#5-Cree una aplicación de cajero automático para el banco ABC. 
# El cajero tendrá un límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
cantidad1000 = 9
saldo = 1000 * cantidad1000
cantidad500 = 19
saldo = saldo + cantidad500 * 500
cantidad100 = 99
saldo = saldo + cantidad100 * 100



if saldo > 0:
    banco = input("Ingrese su Banco:")
    if banco == "ABC" or banco == "abc":
        print("Puede retirar hasta $10,000 y en multiplos de $50 pesos")
    else:
        print("El limite de retiro para su banco es $2,000")

    while True:
        monto = int(input("Ingrese el monto que desea Retirar"))
        if (monto % 50) !=0:
         print("#ERROR, La cantidad no esta disponible") 
        if monto > 10000:
            print("La cantidad ingresada supera el limite")
        elif monto > saldo:
            print("No hay saldo suficiente")
        if (monto <= 10000) and (monto <= saldo) and (monto % 50 == 0): 
            break

    if monto >= 1000:
        billete1000 = int(monto / 1000 )
        if billete1000 > cantidad1000:
            monto = monto - (cantidad1000 * 1000)
            billete1000 = cantidad1000
        else:
            monto = monto - (billete1000 * 1000)

    if monto >= 500:
        billete500 = int(monto / 500 )
        if billete500 > cantidad500:
            monto = monto - (cantidad500 * 500)
            billete500 = cantidad500
        else:
            monto = monto - (billete500 * 500)

    if monto >= 100:
        billete100 = int(monto / 100 )
        if billete100 > cantidad100:
            monto = monto - (cantidad100 * 100)
            billete100 = cantidad100
        else:
            monto = monto - (billete100 * 100)

    print ("La cantidad proporcionada es:")
    print (billete1000,"Billetes de $1,000")
    print (billete500, "Billetes de $500")
    print (billete100,"Billetes de $100")      
    



