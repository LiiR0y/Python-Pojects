#PRACTICA III PYTHON
#1- Hacer una función que potencie un número x a la y
def potencia(x, y):
    return x **y

print(potencia(5, 2))

#2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre
#por pantalla el número escrito en letras.

Numero = int(input("Ingrese un Numero del 1 al 10: "))

def Uno():
	print('Uno')

def Dos():
	print('Dos')

def Tres():
	print('Tres')

def  Cuatro():
	print('Cuatro')

def Cinco():
	print('Cinco')

def Seis():
	print('Seis')

def Siete():
	print('Siete')

def Ocho():
	print('Ocho')

def Nueve():
	print('Nueve')

def Diez():
	print('Diez')

def error():
	print('El numero debe estar comprendido entre 1 a 10')

Letras = {
	1: Uno,
	2: Dos,
	3: Tres,
	4: Cuatro,
	5: Cinco,
	6: Seis,
	7: Siete,
	8: Ocho,
	9: Nueve,
	10: Diez
}

Letras.get(Numero, error)

#3- Hacer una función que reciba un año como argumento y retorne
#verdadero si es bisiesto.

def año_bisiesto(año):
	print("Es bisiesto" if not año % 4 and (año % 100 or  not año % 400) else "No es bisiesto")

año_bisiesto(2028)


#4- Crear una función que evalúe dos números y retorne verdadero si ambos
#números son iguales.

def numeros_iguales(num1, num2):
    return num1 == num2

print(numeros_iguales(9, 2))

#7- Hacer una función que reciba como argumento una lista de elementos
#numéricos y retorno otra lista con cada elemento de la primera lista
#duplicados.

def duplicar_lista(a, b):

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = a[:]

print (duplicar_lista(b))


#8- Hacer una función que reciba un valor iniciar y uno final, y muestre en
#pantalla las tablas de multiplicar de los números múltiplos de 6 que hay
#entre el valor inicial y el valor final.

valor_inicial = int(input("Ingrese el valor incial: "))
valor_final = int(input("Ingrese el valor final: "))

def multiple(valor_inicial, valor_final):

    operacion = valor_inicial % valor_final
    if operacion == 0:
        return True
    
 
multiples_6=[]

 
for i in range(valor_inicial, valor_final):
 
    if multiple(i,6):
        multiples_6.append(i)
 
 
print ("Los multipl0s del 6 son:", multiples_6)