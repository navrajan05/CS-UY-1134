import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDQ:

    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0
        self.front_ind = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def enqueue_last(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)

        back_ind = (self.front_ind + self.n) % self.capacity
        self.data_arr[back_ind] = elem
        self.n += 1

    def enqueue_first(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)

        self.front_ind = (self.front_ind - 1) % self.capacity
        self.data_arr[self.front_ind] = elem
        self.n += 1

    def dequeue_last(self):

        if (self.is_empty()):
            raise Exception("Queue is empty")

        back_ind = (self.front_ind + self.n) % self.capacity
        value = self.data_arr[back_ind - 1]
        self.data_arr[self.front_ind] = None
        self.n -= 1

        if(self.n < self.capacity // 4):
            self.resize(self.capacity // 2)
        return value

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")

        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1


        if(self.n < self.capacity // 4):
            self.resize(self.capacity // 2)
        return value


    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        back_ind = (self.front_ind + self.n) % self.capacity
        return self.data_arr[back_ind]

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0


myDQ = ArrayDQ()
for i in range(5):
    myDQ.enqueue_last(i)
myDQ.enqueue_first("hello")
print(myDQ.dequeue_first())
for i in range(3):
    print(myDQ.dequeue_last())