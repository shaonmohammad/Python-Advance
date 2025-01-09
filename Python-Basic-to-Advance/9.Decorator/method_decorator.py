def method_decorator(great):
    def wrapper(self,*args,**kwargs):
        print(args, kwargs)
        print("Starting method decorator...")
        res = great(self,*args,**kwargs)
        print("Ending method decorator...")  
        return res 
    return wrapper
    
class MethodDecorator:
    def __init__(self):
        pass
    
    @method_decorator
    def great(self,*args, **kwargs):
        print("Hi,Afat!")
        return "Bye Afat!"
        

obj = MethodDecorator()
print(obj.great(100,200,300,a="Afat",b="Tasruba"))

