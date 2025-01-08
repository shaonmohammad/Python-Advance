# Scope means the accessibility of a variable from any local or global space (inside or outside of function)

# Here x is global variable and we are able to access the variable from inside the func() function
x = 100
def func():
    print(x)
func()
print(x)


# Here x2 is a local variable.We're unable to access the local value x(Inside the function) from global space
def func2():
    x2 = 100
    print(x2)
func2()
# print(x2)


# global keyword is use to copy the value of global variable and change the value (Not Reference) inside the the local Scope(Function)
x3 = 200
def func3():
    global x3
    x3 = 100
    print(x3)
print(x3)

func3()
print(x3)






