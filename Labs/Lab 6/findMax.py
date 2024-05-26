def find_max(lst,low,high):
    if low == high: return lst[low]
    else: return max(lst[low], find_max(lst, low + 1, high))

myList = [1,24,5,3,6,7,4]
print(find_max(myList,0,len(myList)-1))