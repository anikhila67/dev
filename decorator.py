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