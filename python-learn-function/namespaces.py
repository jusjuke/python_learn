print(list(range(10)))
my_var = 10
def my_var_func():
    global my_var
    print(my_var)
    my_var = 20
    return my_var

result = my_var_func()   
print(result)
#print(my_var)    