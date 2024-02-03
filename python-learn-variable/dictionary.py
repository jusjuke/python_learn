dict1 = {'Vendor': 'Cisco', 'Model': "2600", 'IOS': '12.4', 'Ports': '4'}
print(type(dict1))
print(dict1)
dict2 = {1:"Cisco", 2:"2600", 3:"12.4", 4:"4"}
print(dict2)
print(dict1["IOS"])
dict1['RAM'] = '128'
print(dict1)
del(dict1['RAM'])
print(dict1)
print("IOS" in dict1)
print("IOS2" not in dict1)
print(dict1.keys())
print(dict1.values())
# return tuple
print(dict1.items())