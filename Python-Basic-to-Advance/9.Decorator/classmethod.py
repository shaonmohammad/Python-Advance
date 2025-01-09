from datetime import date
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year - year)
    
    @staticmethod
    def isAdult(age):
        return age > 18
    
person1 = Person("Afat",12)
person2 = Person.fromBirthYear("Tasruba",2002)

print(f"The age of {person1.name} is {person1.age}")
print(f"The age of {person2.name} is {person2.age}")


print(f"Is the {person1.name} adult or not?{ 'Yeah' if Person.isAdult(person1.age) else 'No'} ")
print(f"Is the {person2.name} adult or not?{ 'Yeah' if Person.isAdult(person2.age) else 'No'} ")