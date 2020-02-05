import Polinomio

class Calculadora:
    def __init__(self):

        self.polinomio1=[]
        self.polinomio2=[]
        self.mayor=[]
        self.menor=[]
        self.resultado=[]

    def setDatos(self):
        #Datos de los polinomios, grado y valor
        grado=int(input("Grado del primer polinomio: "))
        for i in range(0,grado + 1):
            print("Grado : ",i)
            valor = int(input("\t Valor: "))
            self.polinomio1.append(valor)
        print("\n El primer polinomio es: " )
        for i in range (0,len(self.polinomio1)):
            print("+ (",self.polinomio1[i],"x^",i,") \t",end="")
        grado_sp=int(input("\n\n Grado del segundo polinomio: "))
        for i in range(0,grado_sp+1):
            print("Grado : ",i)
            valor_sp = int(input("\t Valor: "))
            self.polinomio2.append(valor_sp)
        print("\n El segundo polinomio es: " )
        for i in range (0,len(self.polinomio2)):
            print("+ (",self.polinomio2[i],"x^",i,") \t",end="")

    def comparaDatos(self):
       #Comparamos ambos polinomios con el fin de obtener el de mayor grado
        if len(self.polinomio1)>len(self.polinomio2):
            self.mayor = self.polinomio1
            self.menor = self.polinomio2
        else:
            self.mayor = self.polinomio2
            self.menor = self.polinomio1 

    def menu(self):
        print("\n\t\t---------- Operaciones con polinomios ----------")
        menu ={
            1:"Suma",
            2:"Resta",
            3:"Multiplicacion",
            4:"Derivada",
            5:"Integral",
            6:"Salir"
            }
        for a,b in menu.items():
            print(a,b)
        opcion=int(input("Introduzca la opcion deseada: "))
        if opcion==1:
            self.setDatos()
            self.comparaDatos()
            self.suma()
        elif opcion==2:
            self.setDatos()
            self.comparaDatos()
            self.resta()
        elif opcion==3:
            self.setDatos()
            self.comparaDatos()
            self.multiplicacion()
        elif opcion==4:
            self.derivada()
        elif opcion==5:
            self.integral()
        elif opcion==6:
            print("Saliendo de la calculadora")
            exit()
        else:
            input (" Opción inválida, inténtelo de nuevo.\n Presione una tecla para continuar... ")
            calculadora.menu()
        calculadora.menu()
    
    def suma(self):
        print("\n\n------SUMA------")
        for i, _ in enumerate(self.mayor):
            if i + 1 > len(self.menor):
                self.resultado.append(self.mayor[i])
            else:
                self.resultado.append(self.mayor[i] + self.menor[i])
        print("\n\n El resultado de la suma de polinomios es : ")        
        for i in range (0,len(self.resultado)):
            print("+ (",self.resultado[i],"x^",i,") \t",end="")
        
    def resta(self):
        print("\n\n------RESTA------")
        for i, _ in enumerate(self.mayor):
            if i + 1 > len(self.menor):
                self.resultado.append(self.mayor[i])
            else:
                self.resultado.append(-self.mayor[i] + self.menor[i])
        print("\n\n El resultado de la resta de polinomios es : ")        
        for i in range (0,len(self.resultado)):
            print("+ (",self.resultado[i],"x^",i,") \t",end="")
         
        
    def multiplicacion(self):
        print("\n\n------MULTIPLICACION------")
        for i, _ in enumerate(self.mayor):
            if i + 1 > len(self.menor):
                self.resultado.append(self.mayor[i])
            else:
                self.resultado.append(self.mayor[i] * self.menor[i])
        print("\n\n El resultado de la multiplicacion de polinomios es : ")        
        for i in range (0,len(self.resultado)):
            print("+ (",self.resultado[i],"x^",i,") \t",end="")
    
    def derivada(self):
        print("\n\n------DERIVADA------")
        terms = []
        grado = int(input("Grado del polinomio: "))
        for term in range(grado + 1):
            print("Grado : ",grado - term)
            terms.append(int(input()))
        polinomio_o = Polinomio.polynomial()
        polinomio_o.expression = terms
        derivative = polinomio_o.derivative
        print("\nPolinomio: ", polinomio_o.pretty_printing(polinomio_o.expression), "\n")
        print("Derivada (polinomio): ", polinomio_o.pretty_printing(derivative), "\n")

    def integral(self):
        print("\n\n------INTEGRAL------")
        terms = []
        grado = int(input("Grado del polinomio: "))
        for term in range(grado + 1):
            print("Grado : ",grado - term)
            terms.append(int(input()))
        polinomio_o = Polinomio.polynomial()
        polinomio_o.expression = terms
        integral = polinomio_o.integral
        print("\nPolinomio: ", polinomio_o.pretty_printing(polinomio_o.expression), "\n")
        print("Integral (polinomio): ", polinomio_o.pretty_printing(integral), "+ c\n")

    def caratula(self):
        unam = "Universidad Nacional Autónoma de México"
        fi = "Facultad de ingeniería"
        ia = "Inteligencia artificial"
        pg = "Programa 2"
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


calculadora=Calculadora()
calculadora.caratula()
calculadora.menu()