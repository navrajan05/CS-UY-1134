def list_sum_triangle(lst):
    if len(lst) == 1:
        print(lst)
    else:
        newList = []
        for i in range(len(lst) - 1):
            newList.append(lst[i] + lst[i+1])
        list_sum_triangle(newList)
        print(lst)


myList = [1,2,3,4,5,6,7]
list_sum_triangle(myList)