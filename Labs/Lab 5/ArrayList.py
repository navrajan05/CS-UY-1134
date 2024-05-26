import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self, x=None):
        try:
            iter(x)
            length = len(x)
            self.data_arr = make_array(length)
            self.capacity = length
            self.n = length
            for i in range(length):
                self.data_arr[i] = x[i]

        except TypeError as te:
            self.data_arr = make_array(1)
            self.capacity = 1
            self.n = 0

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size

    def __getitem__(self, ind):
        if ind < -self.n or ind >= self.n:
            raise IndexError('invalid index')
        return self.data_arr[ind%self.n]

    def __setitem__(self, ind, val):
        if ind < -self.n or ind >= self.n:
            raise IndexError('invalid index')
        self.data_arr[ind%self.n] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  # could also yield self[i]

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        myString = "["
        for i in range(self.n):
            myString += str(self.data_arr[i]) + ", "

        myString = myString[:-2]+"]"
        return myString

    def __add__(self, other):
        out = ArrayList()
        size = self.n + other.n

        out.resize(size)
        for i in range(self.n):
            out.data_arr[i] = self.data_arr[i]

        for i in range(other.n):
            out.data_arr[self.n + i] = other.data_arr[i]

        out.n = size

        return out

    def __iadd__(self, other):
        size = self.n + other.n

        self.resize(size)


        for i in range(other.n):
            self.data_arr[self.n + i] = other.data_arr[i]

        self.n = size

    def __mul__(self, other):
        out = ArrayList()
        size = self.n * other

        out.resize(size)
        for i in range(self.n):
            for j in range(other):
                out.data_arr[(j * self.n) + i] = self.data_arr[i]

        out.n = size
        return out

    def remove(self,target):
        found = False
        targets = []
        for i in self.data_arr:

            if found:
                targets.append(-1)
            else:
                targets.append(0)
            if i == target:
                found = True

        for i in range(self.n):
            self.data_arr[i + targets[i]] = self.data_arr[i]

        if found: self.n -= 1

    def removeAll(self,target):
        found = 0
        targets = []
        for i in self.data_arr:

            targets.append(found)
            if i == target:
                found -= 1

        for i in range(self.n):
            self.data_arr[i + targets[i]] = self.data_arr[i]

        self.n += found




x = ArrayList()
x.append(4)
x.append(5)
x.append(6)

x[2] = 3

y = ArrayList()
y.append(8)

print(x)
print(y)

z = x + y

print(z)
print(z*3)

q = ArrayList("Hello")
print(q)

q.remove('e')
print(q)
q.removeAll('l')
print(q)