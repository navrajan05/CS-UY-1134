class Vector:

    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0]*d
        else:
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
          self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -1 * self[j]
        return result

    def __mul__(self, other):

        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = other * self[j]
            return result
        else:
            if (len(self) != len(other)):
                raise ValueError("dimensions must agree")
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result

    def __rmul__(self, other):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other * self[j]
        return result


    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)

'''
v1 = Vector(5)
v1[1] = 10
v1[-1] = 10
print(v1)

v2 = Vector([2, 4, 6, 8, 10])
print(v2)

u1 = v1 + v2
print(u1)

u2 = -v2
print(u2)

u3 = 3 * v2
print(u3)

u4 = v2 * 3
print(u4)

u5 = v1 * v2
print(u5)
'''
