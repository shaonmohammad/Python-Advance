def new_class(cls):
    class NewClass:
        def new_method(self):
            return "This is new class method"
    return NewClass
@new_class
class OldClass:
    def old_method(self):
        return "This is a old class method"
    
obj = OldClass()
print(obj.new_method())