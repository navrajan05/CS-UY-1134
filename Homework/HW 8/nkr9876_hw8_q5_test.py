from nkr9876_BinarySearchTreeMap import BinarySearchTreeMap

bst = BinarySearchTreeMap()
bst[7] = None
bst[5] = None
bst[1] = None
bst[14] = None
bst[10] = None
bst[3] = None
bst[9] = None
bst[13] = None
print(bst.get_ith_smallest(3))
print(bst.get_ith_smallest(6))

del bst[14]
del bst[5]

print(bst.get_ith_smallest(3))
print(bst.get_ith_smallest(6))
