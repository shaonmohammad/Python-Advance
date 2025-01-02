# Scope means the accessibility of a variable from any local or global space (insdie or outside of function)

# Here x is global variable and we are able to access the variable from insdie the func() function
x = 100
def func():
    print(x)
func()
print(x)


#Here x2 is a local variable.We can'nt able to access the local value x(Insdie the function) from global spcae
def func2():
    x2 = 100
    print(x2)
func2()
# print(x2)


# Global Keyword is use to copy the value of global variable and change the value (Not Reference) insdie the the local Scope(Function)
x3 = 200
def func3():
    global x3
    x3 = 100
    print(x3)
print(x3)
func3()






