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
    
# términos del polinomio
terminos = [3,2,1,9]
# se instancia polynomial
polinomio = polynomial()
polinomio.expression = terminos
#print(polinomio.expr)
print(polinomio.degree)