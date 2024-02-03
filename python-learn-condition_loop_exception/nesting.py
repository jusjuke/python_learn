x = "Csisco"
if "i" in x:
    if len(x) > 3:
        print(x, len(x))
        
list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:
        print(i * j)
    print(i)
print("-------------------")       
x = 1
while x <= 10:
    print(x)
    x += 1
    z = 1
    while z <= 5:
        print(z)
        z += 1
print("-------------------")        
for number in range(10):
    if 5 <= number <= 9:
        print(number)
    #print(number)
print("break -------------------")       
for number in range(10):
    if number > 6:
        break
    print(number)
print("continue -------------------")       
for number in range(10):
    if number == 6:
        continue
    print(number)
    
print("pass -------------------")
for number in range(10):
    pass
    print(number)