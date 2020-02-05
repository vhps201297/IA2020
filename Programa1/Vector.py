import os
import math

class Vector:

    def __init__(self):
        self.content = []

    # retorna el contenfido del vector
    def get_content(self):
        return self.content

    # establece la lista del vector
    def setContent(self,datos):
        self.content = datos

    # Regresa la suma del vector instanciado mas 
    # el vector que se ingresa en el parámetro.
    def suma_vector(self, vector):
        vector2 = vector
        vectorSuma = []
        for i in range(0,len(self.content)):
            val = self.content[i] + vector2[i]
            vectorSuma.append(val)
        return vectorSuma

    # Regresa la resta del vector instanciado menos 
    # el vector que se ingresa dentro del parámetro.
    def resta_vector(self, vector):
        vector2 = vector
        vectorRes = []
        for i in range(0,len(self.content)):
            val = self.content[i] - vector2[i]
            vectorRes.append(val)
        return vectorRes

    # Regresa el vector instanciado pero con los valores multiplicados 
    # por el valor escalar.
    def productor_por_escalar(self, escalar):
        for i in range(0, len(self.content)):
            self.content[i] *= escalar
        return self.content 

    # Para el producto punto de dos vectores se crea un vector con el producto
    # de los valores en cada índice del vector instanciado y el segundo vector,
    # por último se suma los valores del nuevo vector y se manda como resultado.
    def producto_punto(self, vector):
        suma = 0
        lista_tmp = [vector[i]*self.content[i] for i in range(len(vector))]
        for j in range(len(lista_tmp)):
            suma += lista_tmp[j]
        return suma

    # Para la norma o longitud del vector, se determinó con la siguiente formula:
    # sqrt((x^2)+(y^2)+...+(n^2)) 
    def norma(self):
        suma = 0
        for i in range(len(self.content)):
            suma += self.content[i]**2
        return math.sqrt(suma)

    # Para poder cálcular el angulo entre vectores se ocupó la siguiente fórmula:
    # theta = angCos((A·B)/(|A||B|)) sin embargo el resultado lo obtenemos en radianes,
    # para obtenerlo en grados se ocupó el método "degrees()".
    def angulo_vector(self, vector):
        norma1 = self.norma()
        norma2 = vector.norma()
        prod_punto = self.producto_punto(vector.get_content())
        angcos = math.acos(prod_punto/(norma1 * norma2))
        return math.degrees(angcos)

def suma():

    v1 = " Llenado del primer vector "
    v2 = " Llenado del segundo vector "
    tit = " Suma de vectores "
    #Instancia del vector, se inicia un vector vacío
    vector = Vector()
    #Pedir datos de los vectores al usuario
    os.system("clear")
    #os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    datos_suma = int ( input ("\n Ingrese el tamaño que tienen ambos vectores: ") )

    #llenado del primer vector
    print ("\n",v1.center(80,"="),"\n")
    lista1 = llenar_lista(datos_suma)
    
    #llenado del segundo vector
    print ("\n",v2.center(80,"="),"\n")
    lista2 = llenar_lista(datos_suma)

    #Se establece el vector inicial
    vector.setContent(lista1)
    vector_suma = vector.suma_vector(lista2)
    
    print ("\n El primer vector es: ",lista1)
    print (" El segundo vector es: ",lista2)
    print ("\n ----- El vector suma es: ",vector_suma, "-----")
    print ("\n ¿Qué desea hacer?\n 1. Ir al menú principal\n 2. Salir")
    eleccion() 

def resta():
    v1 = " Llenado del primer vector "
    v2 = " Llenado del segundo vector "
    tit = " Resta de vectores "
    #Instancia del vector, se inicia como vacío
    vector = Vector()
    #Pedir datos de los vectores al usuario
    os.system("clear")
    #os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    datos_resta = int ( input (" Ingrese el tamaño que tienen ambos vectores: ") )
    #llenado del primer vector
    print ("\n",v1.center(80,"="),"\n")
    lista1 = llenar_lista(datos_resta)
    #llenado del segundo vector
    print ("\n",v2.center(80,"="),"\n")
    lista2 = llenar_lista(datos_resta)
    #Se establece el vector inicial
    vector.setContent(lista1)
    vector_resta = vector.resta_vector(lista2)

    print ("\n El primer vector es: ",lista1)
    print (" El segundo vector es: ",lista2)
    print("\n ----- El vector resta es: ",vector_resta,"-----")
    print ("\n 1. Ir al menú principal\n 2. Salir")
    eleccion()

def norma():
    v1 = " Llenado del vector "
    tit = " Norma de un vector "
    os.system("clear")
    #os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    tam = int ( input (" Ingrese el tamaño del vector: ") )
    
    #llenado del vector
    print ("\n ",v1.center(80,"="),"\n")
    lista1 = llenar_lista(tam)
    
    print(" El vector ingresado es: ",lista1)
    #Elevando al cuadrado cada uno de los elementos del vector
    vector = Vector()
    vector.setContent(lista1)
    print("\n ----- La norma del vector es: ", vector.norma(),"-----")
    print ("\n 1. Ir al menú principal\n 2. Salir")
    eleccion()

def multiplicacion():
    v1 = " Llenado del vector "
    tit = " Multiplicación por un escalar "
    vector = Vector()
    os.system("clear")
    #os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    datos_suma = int ( input (" Ingrese el tamaño del vector: ") )

    #llenado del vector
    print ("\n",v1.center(80,"="),"\n")
    lista1 = llenar_lista(datos_suma)
    print ("\n El vector ingresado es: ",lista1)
    escalar = int ( input("\n Ingrese el escalar por el que se va a multiplicar el vector: ") )
    vector.setContent(lista1)
    vector_productor_escalar = vector.productor_por_escalar(escalar)

    print("\n ----- El vector resultante es: ", vector_productor_escalar,"-----")
    print ("\n 1. Ir al menú principal\n 2. Salir")
    eleccion()

def angulo():
    v1 = " Llenado del primer vector "
    v2 = " Llenado del segundo vector "
    tit = " Ángulo entre dos vectores "
    vector = Vector()
    vector2 = Vector()
    lista1 = []
    lista2 = []
    os.system("clear")
    #os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    tam = int ( input (" Ingrese el tamaño del vector: ") )
    
    #llenado del primer vector
    print ("\n ",v1.center(80,"="),"\n")
    for i in range (tam):
        elemento1 = int ( input (" Ingrese elemento: ") )
        lista1.append(elemento1)
    #Hacemos una copia de la lista 1
    
    vector.setContent(lista1)
    #llenado del segundo vector
    print ("\n ",v2.center(80,"="),"\n")
    for i in range (tam):
        elemento2 = int ( input (" Ingrese elemento: ") )
        lista2.append(elemento2)
    #Hacemos una copia de la lista 2
    vector2.setContent(lista2)
    print("\n El primer vector es: ", lista1)
    print(" El segundo vector es: ", lista2)
    
    print("\n ----- El ángulo entre los dos vectores es: ", vector.angulo_vector(vector2),"-----")
    print ("\n 1. Ir al menú principal\n 2. Salir")
    eleccion()

def caratula():
    unam = "Universidad Nacional Autónoma de México"
    fi = "Facultad de ingeniería"
    ia = "Inteligencia artificial"
    pg = "Programa 1"
    alum = "Integrantes:"
    fumo = "Fuentes Mora Oscar Fernando"
    gagn = "Granados Gómez Nanci Noelia"
    gle = "Guerrero López Enrique"
    psvh = "Pólito Seba Víctor Hugo"
    sem = "Semestre 2020-2"
    prof = "Profesor: Eduardo Espinosa Ávila"
    print ( "\n",unam.center(100, " "), "\n",fi.center(100," "), "\n\n",ia.center(100, " "), "\n",pg.center(100, " ") )
    print ("\n",alum.center(100," "), "\n",fumo.center(100, " "), "\n", gagn.center(100, " "), "\n",gle.center(100, " "))
    print (psvh.center(102," "),"\n\n",sem.center(100, " "), "\n\n",prof.center(100, " "))
    input("\n\n\nPresione una tecla para continuar...")

def main():
    os.system("clear")
    #os.system("cls")
    print ("\n\t\t---------- Operaciones con vectores ----------")
    print (" 1. Suma \n 2. Resta \n 3. Norma")
    print (" 4. Multiplicación por un escalar")
    print (" 5. Ángulo entre dos vectores")
    print (" 6. Salir")
    while True:
        try:
            opcion = int (input ("\n Elija una opción: "))
            if (opcion == 1):
                suma()
            elif(opcion == 2):
                resta()
            elif(opcion == 3):
                norma()
            elif(opcion == 4):
                multiplicacion()
            elif(opcion == 5):
                angulo()
            elif(opcion == 6):
                return input("Saliendo...")
                break
            else:
                input (" Opción inválida, inténtelo de nuevo.\n Presione una tecla para continuar... ")
                main()
            break
        except ValueError:
            input (" Caracter inválido.\n Presione una tecla para continuar... ")
            main()

def eleccion():
     while True:
        try:
            elecc = int(input ("\n Elija una opción: "))
            if (elecc == 1):
                main()
            elif(elecc == 2):
                return input("Saliendo...")
                break
            else:
                print (" Opción incorrecta")
                eleccion()
            break
        except ValueError:
            input (" Caracter inválido. \nPresione una tecla para continuar...")
            #os.system("clear")
            #os.system("cls")
            print ("\n 1. Ir al menú principal\n 2. Salir")

def llenar_lista(tam):
    lista_tmp = []
    for i in range (tam):
        elemento2 = int ( input (" Ingrese elemento: ") )
        lista_tmp.append(elemento2)
    return lista_tmp

caratula()
main()