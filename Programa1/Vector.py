import os
import math

class Vector:

	def __init__(self):
		self.content = []

	def setContent(self,datos):
		self.content = datos

	def size(self):
		return len(self.content)

	def suma_vector(self, vector):
		vector2 = vector
		vectorSuma = []
		for i in range(0,len(self.content)):
			val = self.content[i] + vector2[i]
			vectorSuma.append(val)
		return vectorSuma

	def resta_vector(self, vector):
		vector2 = vector
		vectorRes = []
		for i in range(0,len(self.content)):
			val = self.content[i] - vector2[i]
			vectorRes.append(val)
		return vectorRes

	def productor_por_escalar(self, escalar):
		for i in range(0, len(self.content)):
			self.content[i] *= escalar
		return self.content 

def suma():

    v1 = " Llenado del primer vector "
    v2 = " Llenado del segundo vector "
    tit = " Suma de vectores "
    #Instancia del vector, se inicia un vector vacío
    vector = Vector()
	#Pedir datos de los vectores al usuario
    lista1 = []
    lista2 = []
    #os.system("clear")
	#os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    datos_suma = int ( input ("\n Ingrese el tamaño que tienen ambos vectores: ") )

	#llenado del primer vector
    print ("\n",v1.center(80,"="),"\n")
    for i in range (datos_suma):
	    elemento1 = int ( input (" Ingrese elemento: ") )
	    lista1.append(elemento1)
	
    #llenado del segundo vector
    print ("\n",v2.center(80,"="),"\n")
    for i in range (datos_suma):
	    elemento2 = int ( input (" Ingrese elemento: ") )
	    lista2.append(elemento2)

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
    lista1 = []
    lista2 = []
    #os.system("clear")
	#os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    datos_resta = int ( input (" Ingrese el tamaño que tienen ambos vectores: ") )
	
	#llenado del primer vector
    print ("\n ",v1.center(80,"="),"\n")
    for i in range (datos_resta):
    	elemento1 = int ( input (" Ingrese elemento: ") )
    	lista1.append(elemento1)
    
	#llenado del segundo vector
    print ("\n ",v2.center(80,"="),"\n")
    for i in range (datos_resta):
    	elemento2 = int ( input (" Ingrese elemento: ") )
    	lista2.append(elemento2)
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
    lista1 = []
    lista1_temp = []
    #os.system("clear")
	#os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    tam = int ( input (" Ingrese el tamaño del vector: ") )
	
	#llenado del vector
    print ("\n ",v1.center(80,"="),"\n")
    for i in range (tam):
	    elemento1 = int ( input (" Ingrese elemento: ") )
	    lista1.append(elemento1)
    lista1_temp = lista1[:]
    print(" El vector ingresado es: ",lista1_temp)
    #Elevando al cuadrado cada uno de los elementos del vector
    lista1_lista1 = [lista1[i]*lista1[i] for i in range(len(lista1))]
    #sumando todos los elementos del vector
    suma = 0
    for i in range(0,len(lista1)):
        suma = suma + lista1_lista1[i]
    #Sacar la raiz cuadrada de la suma anterior, para obtener la norma
    norm = math.sqrt(suma)
    print("\n ----- La norma del vector es: ", norm,"-----")
    print ("\n 1. Ir al menú principal\n 2. Salir")
    eleccion()

def multiplicacion():
    v1 = " Llenado del vector "
    tit = " Multiplicación por un escalar "
    lista1 = []
    vector = Vector()
    #os.system("clear")
	#os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    datos_suma = int ( input (" Ingrese el tamaño del vector: ") )

	#llenado del vector
    print ("\n",v1.center(80,"="),"\n")
    for i in range (datos_suma):
	    elemento1 = int ( input (" Ingrese elemento: ") )
	    lista1.append(elemento1)
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
    lista1 = []
    lista2 = []
    lista1_temp = []
    lista2_temp = []
    vector = Vector()
    #os.system("clear")
	#os.system("cls")
    print("\n",tit.center(80,"="),"\n")
    tam = int ( input (" Ingrese el tamaño del vector: ") )
	
	#llenado del primer vector
    print ("\n ",v1.center(80,"="),"\n")
    for i in range (tam):
	    elemento1 = int ( input (" Ingrese elemento: ") )
	    lista1.append(elemento1)
    #Hacemos una copia de la lista 1
    lista1_temp = lista1[:]
    
    #llenado del segundo vector
    print ("\n ",v2.center(80,"="),"\n")
    for i in range (tam):
	    elemento2 = int ( input (" Ingrese elemento: ") )
	    lista2.append(elemento2)
    #Hacemos una copia de la lista 2
    lista2_temp = lista2[:]

    print("\n El primer vector es: ", lista1)
    print(" El segundo vector es: ", lista2)

    #multiplicar elemento a elemento los vectores (producto punto)
    lista1_lista2 = [lista1[i]*lista2[i] for i in range(len(lista1))]

    #sumar los elementos
    prod_punto = 0
    for i in range(0,tam):
        prod_punto = prod_punto + lista1_lista2[i]

    #Sacar la norma de cada vector
    #Vector 1
    norma_lista1 = [lista1[i]*lista1[i] for i in range(len(lista1))]
    suma = 0
    for i in range(0,tam):
        suma = suma + norma_lista1[i]
    norma1 = math.sqrt(suma)

    #Vector 2
    norma_lista2 = [lista2[i]*lista2[i] for i in range(len(lista2))]
    suma2 = 0
    for i in range(0,tam):
        suma2 = suma2 + norma_lista2[i]
    norma2 = math.sqrt(suma2)

    ang = math.acos((prod_punto)/(norma1*norma2))
    print("\n ----- El ángulo entre los dos vectores es: ", math.degrees(ang),"-----")
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
    #os.system("clear")
    #os.system("cls")
    print ("\n\t\t---------- Operaciones con vectores ----------")
    print (" 1. Suma \n 2. Resta \n 3. Norma")
    print (" 4. Multiplicación por un escalar")
    print (" 5. Ángulo entre dos vectores")
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
            elif (opcion == 5):
                angulo()
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
                return input("Gracias por usar")
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

caratula()
main()