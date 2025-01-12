# Single Inheritence
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

class Employee(Person):  # Single Inheritence
    def __init__(self, name, age,joining_date):
        super().__init__(name,age)
        self.joining_date = joining_date

    def show_info(self):
        return print(f"{self.name} {self.age} {self.joining_date}")

emp1 = Employee("Afat",200,"11-2-2025")
emp1.show_info()


# Example of Multiple Inheritence

class Engineer:
    def __init__(self,name,expertise):
        self.name = name
        self.expertise = expertise

    def engineer_info(self):
        return print(f"{self.name} with Expert in {self.expertise}")


class Manager:
    def __init__(self,name,team_members):
        self.team_members  = team_members
        self.name  = name
    def manager_info(self):
        return print(f"{self.name} with team member:{self.team_members}")
    
class TeamLead(Engineer,Manager):
    def __init__(self, name, expertise,team_members):
        Engineer.__init__(self,name,expertise)
        Manager.__init__(self,name,team_members)
    
    def guide(self):
        print(f"{self.name} guides the team while working on {self.expertise}.")


teamlead1 = TeamLead("Afat","AI/ML",100)
teamlead1.guide()
teamlead1.engineer_info()


# Example of MultiLevel Inheritence
class Product:
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
        
    def show_product_info(self):
        return print(f"Product: {self.name} price:{self.price} color:{self.color}")
    

class Laptop(Product):
    def __init__(self, name, price, color,core_i,ssd,ram):
        super().__init__(name, price, color)
        self.core_i = core_i
        self.ssd = ssd
        self.ram = ram

    def laptop_info(self):
        return print(f"Laptop: {self.name} price:{self.price} color:{self.color} with core-i{self.core_i} and ram:{self.ram} also ssd:{self.ssd}")

class GammingLaptop(Laptop):
    def __init__(self, name, price, color, core_i, ssd, ram,gpu,refresh_rate):
        super().__init__(name, price, color, core_i, ssd, ram)
        self.gpu = gpu
        self.refresh_rate = refresh_rate

    def gamming_laptop_info(self): 
        return print(f"Gamming Laptop:{self.name} price:{self.price} color:{self.color} with core-i{self.core_i} and ram:{self.ram} also ssd:{self.ssd},gpu:{self.gpu}")


    
gamming_laptop = GammingLaptop("Ausus A2G",100000,"Gray",7,256,16,36,100)

gamming_laptop.laptop_info()
gamming_laptop.gamming_laptop_info()