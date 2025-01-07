name = 'afat'
amount = 10

# Those all are the previous way to instead of f-string

#No:1
massage = "\n" + name + " has " + str(amount) + " taka."
print(massage)

#No:2
massage = "\n%s has %s taka."%(name,amount) 
print(massage)

#No:3
massage = "\n{} has {} taka.".format(name,amount) 
print(massage)

#No:4
massage = "\n{1} has {0} taka.".format(amount,name) 
print(massage)

#No:5
massage = "\n{name} has {amount} taka.".format(amount=amount,name=name) 
print(massage)

#No:6
data = {'name':"afat",'amount':10}
massage = "\n{name} has {amount} taka.".format(**data) 
print(massage)

# ------------- This is the way of f-string -------------


class PersonInfo():
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        print(f"{self.name} has {self.amount*10} taka.")


person1 = PersonInfo("Afat",10)
person1.get_info()

data2 = {'name':'Tasruba','amount':10}
person2 = PersonInfo(**data2)
person2.get_info()