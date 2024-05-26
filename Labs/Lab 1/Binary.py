def add_binary(bin_num1, bin_num2):


    dec_num1 = 0

    for i in range(len(bin_num1)):
        index = -1 * (i + 1)
        if bin_num1[index] == "1":
            dec_num1 += pow(2,i)

    dec_num2 = 0

    for i in range(len(bin_num2)):
        index = -1 * (i + 1)
        if bin_num2[index] == "1":
            dec_num2 += pow(2, i)


    sum = dec_num1 + dec_num2
    empty = ['0']
    out = []

    value = 1
    while value <= sum:
        value = value *2
        out = out + empty


    digitCount = len(out)



    for i in range(digitCount):
        value = pow(2, digitCount - 1 - i)
        if value <= sum:
            sum = sum - value
            out[i] = "1"

    out2 = ""
    for x in out:
        out2 += x

    print(out2)


add_binary("1101","11")