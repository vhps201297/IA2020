from fractions import Fraction
def mcd(a,b):
    #   assert type(a) == int and type(b) == int and a>0 and b>0
    if a%b != 0:
        print("return mcd: ", mcd(b,a%b))
        return mcd(b,a%b)
    else:
        print("return b: ", b)
        return b

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
        vector_rev = self.expression[::-1]
        for term in range(len(vector_rev)):
            integral_v.append(str(Fraction(str(vector_rev[term])+ "/" + str(term + 1))))
        integral_v.insert(0, '0')
        return integral_v[::-1]


# términos del polinomio
terms = [8,0]
polinomio = polynomial()
polinomio.expression = terms

print("\npolinomio: ", polinomio.expression)
print("grado del polinomio: ", polinomio.degree)
print("derivada: ", polinomio.derivative)
print("integral: ", polinomio.integral, "\n")