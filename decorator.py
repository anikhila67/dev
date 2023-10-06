def deco1(func):
    
    arr1 = []
    
    def func1():
        var1 = 9
        var3 = func()
        print(var1 + var3)
        # return 
    return func1

@deco1
def callFunc(): 
    print('this is the calling function')
    var3 = 4
    return var3

callFunc()

# deco1(callFunc())
# print(deco1(callFunc()))
def hello_decorator(func):
    def inner1(*args, **kwargs):
         
        print("before Execution")
         
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
         
        # returning the value to the original frame
        return returned_value
         
    return inner1
 
 
# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
a, b = 1, 2
 
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))