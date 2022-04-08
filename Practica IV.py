#Practica IV: Python
#Loriel Ramirez

#1- Modele tres entidades del mundo real, colocar por lo menos 3
#características distintivas.
class Smartphone():
    def __init__(self, marca, color, modelo, precio):
     self.marca = marca
     self.color = color 
     self.modelo = modelo
     self.precio = precio

movil1 = Smartphone("Apple", "Negro", "IPhone 12","$1.099.00")
movil2 = Smartphone("Samsung", "Phanton Violet", "Galaxy S21 5G","799.00")
movil3 = Smartphone("Xiaomi", "Azul", "Xiaomi Mi 11","$720.00")

#2- Crear una clase llamada Estudiante con un campo llamado promedio, el cual
#solo podrá ser accedido mediante un metodo. El valor del promedio no puede
#estar por encima de 100 que es la nota máxima.
class Estudiante():
    def __init__(self, promedio):
        self.promedio = promedio
        
    def motrar_prom(self):
        if self.promedio <= 100:
         print(f"El promedio del estudiante es: {self.promedio}")
        else:
             print("El promedio debe se menor a 100")

est = Estudiante(190)
est.motrar_prom()


#3-Hacer una clase llamada Aritmética, que contenga métodos para cada una de
#las operaciones aritméticas básicas.

class Aritmetica():
    num1= 0
    num2= 0

    def __init__(self,num1,num2):
        self.num1= int(num1)
        self.num2= int(num2)

    def sumar(self):
        suma = self.num1+self.num2
        print(suma)
    
    def restar(self):
        resta = self.num1-self.num2
        print( resta)

    def multiplicar(self):
        multiplicacion = self.num1*self.num2
        print(multiplicacion)

    def dividir(self):
        division = self.num1/self.num2
        print(division)


num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")

Aritmetica = Aritmetica(num1,num2)

#4-Cree una clase llamada Personaje con los métodos de instancia MoverArriba,
#MoverAbajo, MoverDerecha y MoverIzquierda. Cree una clase llamada Mario y
#otra clase llamada Koopa que herede las funcionalidades de la clase Personaje.
class Personaje():
    def __init__(self):
        self.MoverArriba = MoverArriba
        self.MoverAbajo = MoverAbajo
        self.MoverDerecha = MoverDerecha
        self.MoverIzquierda = MoverIzquierda


class Mario(Personaje):
    pass

class Koopa(Personaje):
    pass

