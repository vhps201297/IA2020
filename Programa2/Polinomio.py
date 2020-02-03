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
        # menos_uno = self.expr[:len(self.expr) - 2]
        # menos_uno = [term -1 for term in menos_uno]
        derivative_v = [term -1 for term in self.expr[:-2]]
        derivative_v.append(self.expr[-2])
        return derivative_v

# términos del polinomio
terminos = [35,6,2,1,9]
# se instancia polinomio
polinomio = polynomial()
polinomio.expression = terminos

print("\npolinomio: ", polinomio.expr)
print("grado del polinomio: ", polinomio.degree)
print("derivada: ", polinomio.derivative, "\n")