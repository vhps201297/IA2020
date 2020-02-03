from fractions import Fraction

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

    @property
    def integral(self):
        integral_v = []
        vector_rev= self.expression[::-1]
        for term in range(len(vector_rev)):
            integral_v.append(str(Fraction(str(vector_rev[term]) + "/" + str(term + 1))))
        integral_v.insert(0, '0')
        return integral_v[::-1]

    @property
    def integral_pp(self):
        vector_rev = self.integral[::-1]
        pretty_printing = ''
        for term in range(len(vector_rev)-1, -1, -1):
            pretty_printing += "(" + str(vector_rev[term]) + ")" +"x^" + str(term) + " + "
        return pretty_printing[:-3]

# términos del polinomio
terms = [3,3,2,5]
polinomio = polynomial()
polinomio.expression = terms

print("\npolinomio: ", polinomio.expression)
print("grado del polinomio: ", polinomio.degree)
print("derivada: ", polinomio.derivative)
print("integral (vector): ", polinomio.integral)
print("integral (polinomio): ", polinomio.integral_pp, "\n")