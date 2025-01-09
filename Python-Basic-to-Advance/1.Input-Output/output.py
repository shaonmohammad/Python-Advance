#Formatting Output using String Modulo Operator(%)
# string modulo operator(%)

print("Academy : %2d, Portal : %5.2f" % (1, 05.333)) 
print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
print("%7.3o" % (25))   # print octal value
print("%10.3E" % (356.08977))   # print exponential value


#Formatting Output using The Format Method
print("I very excited  to learn {1} and {0} with {devOps}".format("AI","ML",devOps="devOps"))
print("There are 2 number {0} and {1:.2f}".format(13,2.2323242))


#Formatted String Literals (f-strings) (Python 3.6+):
name = "Afat"
age = 23
print(f"My name is {name} and my age is:{age}")
