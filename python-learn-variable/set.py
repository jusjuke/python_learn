list4 = [1,2,3,4,5,2,3]
print(set(list4))
set2 = {1, 2, 3, 4, 5, 11}
print(len(set2))
print(11 in set2)
print(10 not in set2)
set2.add(16)
print(set2)
set2.remove(11)
print(set2)
set2.add(16)
print(set2)

set3 = {3,5,6}
print(set2.intersection(set3))
print(set2.difference(set3))
print(set2.union(set3))
print(set2.pop())
print(set2)
set2.clear()
print(set2)

list5 = [5,9,10]

fset1 = frozenset(list4)
fset2 = frozenset(list5)
print(type(fset1))
print(fset1.intersection(fset2))
