def my_first_function():
    """This is a docstring. I have created a function."""
    print("Hello, world!")
def my_second_function(x):
    print(x)    
    
def my_sum(x, y):
    sum = x + y
    return sum ** 2
def param_test_function(x, y, z = 3):
    sum = (x + y) * z
    return sum ** 2
def function_with_tuple(x, *args):
    print(x)
    for arg in args:
        print(arg)
        
def function_with_dict(**kwargs):
    for key, value in kwargs.items():
        print(key + " : " + value)        

help(my_first_function)
my_first_function()
my_second_function("Hello, Python!")
print(my_sum(2, 3))
print(param_test_function(z=2, y=3, x=4))
print(param_test_function(2, 3))
function_with_tuple(1, 2, 3, 4, 5)
function_with_dict(name="John", age="30")
