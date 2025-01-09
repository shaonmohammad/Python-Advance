# *args accept the value in a tuple of function perameter
# **kwargs accept the value in a dictionary of a function perameter

def fun(*args):
    print(sum(args))

def fun2(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

fun(1,2,3,4)
fun2(a=1,b=2,c=3)
