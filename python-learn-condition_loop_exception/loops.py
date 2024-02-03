vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
for x in vendors:
    print("The vendor is:" + x)
    
my_string = "Cisco"
for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)
    
r = range(10)
for i in r:
    print(i)

for element_index in range(len(vendors)):
    print(vendors[element_index])
    
for index, element in enumerate(vendors):
    print(index, element)

for element in vendors:
    print(element)
else:
    print("The end of the list has been reached")
    
dicData = {"k1": "Cisco", "k2": "Juniper", "k3": "HP", "k4": "Avaya"}
for k, v in dicData.items():
    print(k, v)
   
x = 1
while x <= 10:
    print(x)
    x += 1
else:
    print("now x is greater than 10")
    
    