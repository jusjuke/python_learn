list1 = ["Cysco", "Avaya", 10, 10.5, -11]
list1.append(100)
print(list1)
del list1[4]
print(list1)
list1.pop(0)
list1.remove("Avaya")
print(list1)
list1.insert(2, "Test")
print(list1)
list2 = [9,99,9999, 1, 25, 500]
list1.extend(list2)
print(list1)
print(list1.index("Test"))
list1.append(100)
print(list1.count(100))
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2 = sorted(list2)
print('Sorted: ' + ",".join(str(e) for e in list2))
list2 = sorted(list2, reverse=True)
print(list2)
print(list1 + list2)
print(list2 * 3)
list3 = [1, 2, 3, "a", "b", "c"]

print(list3[2:5]) #not include 5
print(list3[-4:-1])
print(list3[::2])
print(list3[::-1])
list3.append(list1)
print(list3)