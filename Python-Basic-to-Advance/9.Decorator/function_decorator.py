# 1:function decorator
def function_decorator(great):
    def wrapper():
        print("Starting the decorator method...")
        res = great()
        print("Ending the decorator method...")
        return res
    return wrapper

@function_decorator
def great():
    print("Hi,Afat!")
    return "OK"
print(great())