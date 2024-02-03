my_tuple = ()
print(type(my_tuple))
my_tuple = (9)
print(type(my_tuple))
my_tuple = (3,9)
print(type(my_tuple))
my_tuple = (1,2,3,4,5)
print(my_tuple[3])
#Error
#my_tuple[2] = 10
#del my_tuple[3]
tuple1 = ("Cisco", "2600", "12.4")
#tuple unpacking
(vendor, model, ios) = tuple1 
print(model)
print(tuple1)

#tuple vs list
#tuple  - immutable
#list - mutable
#fixed length - variable length
#tuple ()
#list ()
a = ()
b = []
print(type(a))
print(type(b))
print(dir(a))
print(dir(b))
print(len(tuple1))
print(min(tuple1))
print(tuple1 + (5,7,8))
print(tuple1 * 2)
print(tuple1[:2])
print("2600" in tuple1)
del tuple1
print(tuple1)
