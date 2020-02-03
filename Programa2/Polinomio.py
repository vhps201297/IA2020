class polynomial():
    
    def __init__(self):
        pass

    @property
    def expression(self):
        return self.expr

    @expression.setter
    def expression(self, terms):
        self.expr = terms

    @property
    def degree(self):
        return len(self.expr) - 1

    @property
    def derivative(self):
        der = []
        vector_rev = self.expression[::-1]
        for term in range(1, len(vector_rev)):
            der.append(vector_rev[term] * term)
        return der[::-1]

# términos del polinomio
terms = [7,9,2,1,9]
# se instancia polinomio
polinomio = polynomial()
polinomio.expression = terms

print("\npolinomio: ", polinomio.expression)
print("grado del polinomio: ", polinomio.degree)
print("derivada: ", polinomio.derivative, "\n")