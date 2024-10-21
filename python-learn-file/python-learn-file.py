#myfile = open("C:\\Users\\jusju\\python_repo\\python_learn\\python-learn-file\\routers.txt", "r")
myfile = open(r"C:\Users\jusju\python_repo\python_learn\python-learn-file\routers.txt", "r") #raw string
print(myfile.mode)
print(myfile.read())
myfile.seek(0)
print(myfile.tell())
print("read 5 characters:")
print(myfile.read(5))
myfile.seek(0)
print(myfile.readline())
print(myfile.readline())
myfile.seek(0)
print(myfile.readlines())
myfile.seek(0)
print("\print line:")
for line in myfile:
    if(line.startswith("C")):
        print(line)
myfile.seek(0)     
for line in myfile.readlines():
    if(line.startswith("A")):
        print(line)   

#File already exists        
#myfile = open("C:\\Users\\jusju\\python_repo\\python_learn\\python-learn-file\\routers.txt", "x")

