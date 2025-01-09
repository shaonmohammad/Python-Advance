mylist = [1,'a',4,"afat",'tasruba']

# Append and Delete
mylist.append("tasruu")
print(mylist)
mylist.remove("tasruba")
print(mylist)

# Using list() Constructor
mylist2 = list((1,2,"c"))
print(mylist2)

# Creating List with Repeated Elements
a = [3] * 4
print(a)

# Adding Elements into List append(),insert(),extend()
a.insert(0,"X")
print(a)

a.extend(mylist)
print(a)