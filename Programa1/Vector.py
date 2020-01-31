class Vector:
	#content = []

	def __init__(self):
		self.content = []

	def setContent(self,datos):
		self.content = datos

	def size(self):
		return len(self.content)

	def suma_vector(self, vector):
		vector2 = vector
		vectorRes = []
		for i in range(0,len(self.content)):
			val = self.content[i] + vector2[i]
			vectorRes.append(val)
		return vectorRes

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

	def raiz(numero):
		#numero=float(input("Ingrese numero: "))
		numero=numero * 1.0
		if numero>=0:
			p=numero
			i=0
			while i!=p:
				i=p
				p=(numero/p+p) / 2
			return p
		else :
			return -1


# Instancia del vector, se inicia un vector vacío
vector = Vector()

lista1 = [1,2,3]
lista2 = [2,3,4]
# Establece el vector inicial
vector.setContent(lista1)
# suma el vector inicial con otro vector
vector_suma = vector.suma_vector(lista2)
# resta el vector que se ingresa como parámetro
vector_resta = vector.resta_vector(lista2)
# realiza el producto escalar hacia el vector
vector_productor_escalar = vector.productor_por_escalar(5)

print("Tamaño: ",vector.size())
print("vector_suma", vector_suma)
print("vector_resta", vector_resta)
print("vector base por un escalar:", vector_productor_escalar)



