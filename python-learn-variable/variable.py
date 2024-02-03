import subprocess

a, b, c = 1, 2, 3
print(a, b , c)
print(id(a))
print(id(b))
a = b
print(id(a))

ip = '127.0.0.1'
ping_reply = subprocess.call('ping %s /n 2' % (ip), stdout = subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(ping_reply)

my_string = '''
This 
is 
My String
'''
print(my_string)

my_string = '''
This \
is \
My String\
'''
print(my_string)

string1 = "SCISCO ROUTER SWITCH"
print(string1[3])
print(string1[-3])
print(len(string1))
print(string1.index("I"))
print(string1.count("I"))
print(string1.find("ROUTER"))
print(string1.find("my"))
print(string1.lower())
print(string1.startswith("S"))
print(string1.endswith("H"))

b = "     sisco router switch    "
print(b.strip())
c = "$$$$$$sisco router switch$$$$$$"
print(c.strip("$"))
print(b.replace(" ", ""))

network_user = "John,Jane,Tom,Robert"
print(network_user.split(",")) # list 
print("_".join(string1))
x = "Cisco"
y = " Switch"
print(x + y)
print( x * 3)
print("o" in x)
print("b" in x)
print("o" not in x)
print("Cisco Model: %s, %d WAN slots, IOS %.2f" % ("2600 XM", 2, 12.4))
print("Cisco Model: {}, {} WAN slots, IOS {}" .format("2600 XM", 2, 12.4))
print("Cisco Model: {0}, {1} WAN slots, IOS {2}")

model = "2600 XM"
slots = 2
ios = 12.3
#f string
print(f"Cisco Model: {model},  {slots} WAN slots, IOS {ios}")
print(f"Cisco Model: {model.lower()},  {slots * 3} WAN slots, IOS {ios}")

mystring = "this is my own string 556677"
print(mystring[3: 6])
print(mystring[3:])
print(mystring[: 10])
print(mystring[-4:-1])
#skip every 2th character
print(mystring[::2])
print(mystring[::-1])

mystring = "0123456789"

print(mystring[: : 2])
print(mystring[1: : 2])

#math operation

