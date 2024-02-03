# return range
range1 = range(10)
print("," . join(str(e) for e in range1))
range2 = range(2, 10, 2)
print("," . join(str(e) for e in range2))
range3 = range(-2, -10, -2)
print("," . join(str(e) for e in range3))
print(type(range3))
print("," . join(str(e) for e in range1[2:6]))