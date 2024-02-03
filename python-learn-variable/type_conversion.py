num = 4
f = 4.5
num = str(num)
f = str(f)
print(type(num))
print(type(f))
if(type(num) == str):
    print("Equal")
    
num2 = "5"
float2 = "5.5" 
print(type(int(num2)))
print(type(float(float2)))
print(int(float(float2)))
print(float(int(num2)))

tup1 = (1,2,3,4,5)
print(list(tup1))
print(set(tup1))
list1 = list(tup1)
print(tuple(list1))

num3 = 10
num3_bin = bin(num3)
print(num3_bin)
num_hex = hex(num3)
print(num_hex)
bin_to_num = int(num3_bin, 2)
print(bin_to_num)
hex_to_num = int(num_hex, 16)
print(hex_to_num)