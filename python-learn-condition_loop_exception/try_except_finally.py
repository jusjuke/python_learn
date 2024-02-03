for i in range(10):
    try:
        print(i / (5 - i))
    except ZeroDivisionError as e:
        print("Division by zero! / " , str(e))
print("multiple exception -------------------")        
for i in range(5):
    try:
        print(i / (3 - i))
    except ZeroDivisionError as e:
        print("Division by zero! / " , str(e))    
    except NameError as e:
        print("You have a name error! / " , str(e))
    except ValueError as e:
        print("You have a value error! / " , str(e))
        
print("all exception -------------------")
for i in range(5):
    try:
        print(i / (3 - i))
    except:
        print("Exception occurred ")
        
print("else -------------------")
for i in range(5):
    try:
        print(i / 1)
    except ZeroDivisionError as e:
        print("Exception occurred ", e) 
    else:
        print("No exceptions")     
        
for i in range(5):
    try:
        print(i / (3 - i))
    except ZeroDivisionError as e:
        print("Division by zero! / " , str(e))  
    finally:
        print("This will always execute")               