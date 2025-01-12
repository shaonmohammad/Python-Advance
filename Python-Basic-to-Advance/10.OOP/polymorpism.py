# Operator Overloding
def add(a, b):
    return a + b  # '+' operator work different task for different data type

print(add(3, 4))  # Integer addition
print(add("Hello, ", "World!"))  # String concatenation
print(add([1, 2], [3, 4]))  # List concatenation


# Method Overloding
class Shape:
    def __init__(self):
        pass

    def area(self):
        return "Undifined"

class Circle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    
    @property
    def area(self):
        return self.length * self.width
    
class Ractangle(Shape):
    def __init__(self,redius):
        super().__init__()
        self.redius = redius

    @property
    def area(self):
        return 3.1416 * self.redius
    

circle = Circle(100,200)
print(circle.area)

ractagle =  Ractangle(100)
print(ractagle.area)
