set1 = {1,3,4,5,6}  # creating a set
print(set1)

# Creating a Set with the use of a List
set2 = set(["Afat", "Uddin", "shaon"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Afat", "Uddin", "shaon")
print(set(tup))

# create a set using dictionary
data = {"name":"Afat","age":"23"}
set3 = set(data)
print(set3)

# Adding element in the set
set1.add(8)
set1.update("999")
print(set1)

# Python set Union() Method Example
A = {2, 4, 5, 6} 
B = {4, 6, 7, 8}
print("A U B is: ", A.union(B))

# Python set Intersection() Method Example
A = {2, 4, 5, 6} 
B = {4, 6, 7, 8}
print("A I B is: ", A.intersection(B))