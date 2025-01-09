class Rectangular:
    def __init__(self,length,width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    @length.setter
    def length(self,value):
        if value <= 0:
            raise ValueError("Value can not negetive!")
        else:
            self._length = value
            
    @width.setter
    def width(self,value):
        if value < 0:
            raise ValueError("Value can not negetive!")
        else:
            self._width = value
    @property
    def area(self):
        return self.length * self.width

obj1 = Rectangular(100,200)
print(obj1.length)
print(obj1.width)

obj1.length = 200
obj1.width = 300

print(obj1.length)
print(obj1.width)

