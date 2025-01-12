from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def make_sound(self):
        pass
    
    
class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    def make_sound(self):
        return "Hi!"

dog = Dog()
print(dog.make_sound())