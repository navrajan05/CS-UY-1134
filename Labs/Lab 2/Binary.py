class UnsignedBinaryInteger:
    # makes the list
    def __init__(self, num_str):
        self.num = []
        for i in num_str:
            self.num.append(int(i))

        # remove leading zeroes from input
        for i in range(len(self.num)):
            if self.num[0] == 0:
                self.num.pop(0)
            else:
                break



    def __lt__(self, other):

        #convenience variables
        myLength = len(self.num)
        otherLength = len(other.num)

        if myLength < otherLength:
            return True
        elif otherLength < myLength:
            return False
        else:
            for i in range(myLength):
                if self.num[i] < other.num[i]:
                    return True
                elif self.num[i] > other.num[i]:
                    return False
        return False


    def __gt__(self, other):
        myLength = len(self.num)
        otherLength = len(other.num)

        if myLength > otherLength:
            return True
        elif otherLength > myLength:
            return False
        else:
            for i in range(myLength):
                if self.num[i] > other.num[i]:
                    return True
                elif self.num[i] < other.num[i]:
                    return False
        return False

    def __eq__(self, other):
        myLength = len(self.num)
        otherLength = len(other.num)

        if myLength != otherLength:
            return False
        else:
            for i in range(myLength):
                if self.num[i] != other.num[i]:
                    return False

        return True


    def is_twos_power(self):
        myLength = len(self.num)

        digits = 0;
        for i in range(myLength):
            if self.num[i] == 1:
                digits +=1
            if digits > 1:
                break

        return digits == 1

    def largest_twos_power(self):
        if self.is_twos_power():
            return pow(2, len(self.num) - 1)
        else:
            return pow(2, len(self.num))

    def __repr__(self):
        out = "0b"
        for i in self.num:
            out += str(i)
        return(out)

    def __add__(self, other):
        greater = max(len(self.num), len(other.num))

        fill = [0] * greater
        padded = fill[len(self.num):] + self.num
        paddedOther = fill[len(other.num):] + other.num

        out = [0] * (greater + 1)
        outStr = ""
        for i in range(1,greater+1):
            sum = out[-i] + padded[-i] + paddedOther[-i]
            if sum == 0 :
                out[-i] = 0
            elif sum == 1:
                out[-i] = 1
            elif sum == 2:
                out[-i] = 0
                out[-i -1] = 1
            elif sum == 3:
                out[-i] = 1
                out[-i - 1] = 1


        for i in out:
            outStr += str(i)

        return UnsignedBinaryInteger(outStr)

    def __or__(self, other):
        greater = max(len(self.num), len(other.num))

        fill = [0] * greater
        padded = self.num + fill[len(self.num):]
        paddedOther = other.num + fill[len(other.num):]

        out = [0] * (greater)

        for i in range(greater):


        for i in out:
            outStr += str(i)

        return UnsignedBinaryInteger(outStr)





b1 = UnsignedBinaryInteger("1001111")
b2 = UnsignedBinaryInteger("11111")
b3 = UnsignedBinaryInteger("10000")
b4 = UnsignedBinaryInteger("10000")

print(b3.largest_twos_power())
print(b2.largest_twos_power())
b6 = b2 + b3
print(b6)