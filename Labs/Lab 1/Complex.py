class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary

        return Complex(real, imaginary)


    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary

        return Complex(real, imaginary)


    def __repr__ (self):

        if self.imaginary < 0:
            operator = "-"
        else:
            operator = "+"

        if self.real != 0 and self.imaginary != 0:
            return str(self.real) + " " + operator + " " + str(abs(self.imaginary)) + "i"

        elif self.real == 0 and self.imaginary != 0:
            return str(self.imaginary) + "i"

        else:
            return str(self.real)


    def __mul__(self, other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.imaginary * other.real) + (self.real * other.imaginary)

        return Complex(real, imaginary)





#constructor, output
cplx1 = Complex(5, 2)
print(cplx1) #5 + 2i
cplx2 = Complex(3, 3)
print(cplx2) #3 + 3i

#addition
print(cplx1 + cplx2) #8 + 5i
#subtraction
print(cplx1 - cplx2) #2 - 1i
#multiplication
print(cplx1 * cplx2) #9 + 21i


print(cplx1) #5 + 2i
print(cplx2) #3 + 3i
