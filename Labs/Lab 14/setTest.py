from ChainingHashTableSet import ChainingHashTableSet
mySet1 = ChainingHashTableSet()
mySet2 = ChainingHashTableSet()


for i in range(6):
    mySet1.add(i)


for i in range(0, 12, 2):
    mySet2.add(i)

print(mySet1)
print(mySet2)

print("intersection:", mySet1 & mySet2)
print("union:", mySet1 | mySet2)
print("difference:", mySet1 - mySet2)