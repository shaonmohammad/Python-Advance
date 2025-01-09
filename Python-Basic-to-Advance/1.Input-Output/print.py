# without end parameter
print ("GeeksForGeeks is the best platform to learn Python")

# print() function ends with "**" as set in end parameter.
print ("GeeksForGeeks is the best platform to Learn Python", end= "**")
print("")
print("Welcome to GFG")

# “sep” parameter in print()
a = 1
b = 2 
c = 3
print(a,b,c, sep="-")


# print() Function with file parameter
print("Trying to write a file via print function",file=open("test.txt","w"))


#How to Print Without a Newline in Python?
print("This is line 1",end=" ")
print("This is line 2",)