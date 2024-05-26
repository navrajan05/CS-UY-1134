import math

class Polynomial():
    def __init__ (self, coefficients):
        self.factors = []
        for i in coefficients:
            self.factors.append(i)

    def __add__ (self, other):

        greater = max(len(self.factors),len(other.factors))

        fill = [0] * greater
        padded = self.factors + fill[len(self.factors):]
        paddedOther = other.factors + fill[len(other.factors):]

        out = []
        for i in range(greater):
            out.append(padded[i] + paddedOther[i])

        return(Polynomial(out))

    def __call__(self, param):
        sum = 0;
        for i in range(len(self.factors)):
            sum += (self.factors[i] * pow(param, i))

        print(sum)
        return sum

    def __repr__(self):
        out = ""
        length = len(self.factors)
        for i in range(1, length + 1):

            exponent = length - i
            term = "x^" + str(exponent) + " + "
            if exponent == 1:
                term = "x + "
            elif exponent == 0:
                term = ""

            out += str(self.factors[-i]) + term

        return(out)

    def derive(self):

        length = len(self.factors)
        if length == 0:
            self.factors = [0]
        else:
            newFactors = []
            for i in range(1,length):
                newFactors.append(i * self.factors[i])
            self.factors = newFactors;

    def __mul__ (self, other):

        length = len(self.factors)
        lengthOther = len(other.factors)

        out = [0] * (length + lengthOther - 1)

        for i in range(length):
            for j in range(lengthOther):
                out[i + j] += self.factors[i] * other.factors[j]

        return(Polynomial(out))

p1 = Polynomial([1,1,0,1])
p2 = Polynomial([0,2])

print(p1(2))
print(p1)

print(p2 * p1)