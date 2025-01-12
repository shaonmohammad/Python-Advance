# How to create a dictionary
dic1 = {1:"Afat",2:"Tasruba",3:"Shaon"}

# create dictionary using dict() constructor
dic2 = dict(a="Afat",b="Tasruba",c="Shaon")

# Access by key and get method
print(dic1[1])
print(dic1.get(2))

# Removing Dictionary Items using pop(),remove(),popitem()
dic1.pop(1)
print(dic1)

# for delete last key value pairs
dic1.popitem()
print(dic1)


new = {'a':1,'b':2,'c':[1,2,3]}
new['c'].append(10)
print(new)
print(new.get('d'))