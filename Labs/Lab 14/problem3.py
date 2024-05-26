from ChainingHashTableMap import ChainingHashTableMap


def two_sum(lst, target):

    myMap = ChainingHashTableMap()
    for i in lst:
        myMap[i] = target - i

    for i in myMap:
        if myMap[i] in myMap:
            return (lst.index(i), lst.index(myMap[i]))

    return (None, None)

print(two_sum([1,2,4,6,5], 10))

