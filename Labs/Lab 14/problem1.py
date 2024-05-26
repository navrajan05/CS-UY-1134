from ChainingHashTableMap import ChainingHashTableMap

def most_frequent(lst):
    myMap = ChainingHashTableMap()
    for i in lst:
        if i in myMap:
            myMap[i] += 1
        else:
            myMap[i] = 0

    greatest = 0
    best = None
    for i in myMap:
        if myMap[i] >= greatest:
            best = i
            greatest = myMap[i]

    return best

def first_unique(lst):
    myMap = ChainingHashTableMap()

    for j in range(len(lst)):
        i = lst[j]
        if i in myMap:
            myMap[i][0] += 1
        else:
            myMap[i] = [0, j]

    minVal = len(lst)
    minKey = None

    for i in myMap:
        if myMap[i][0] == 0:
            if myMap[i][1] < minVal:
                minVal = myMap[i][1]
                minKey = i

    return minKey

print(most_frequent([5,9,2,9,0,5,9,7]))
print(first_unique([5,9,2,9,0,5,9,7]))


# Worst case complexity for both is O(n), this doesn't change if I use strings
