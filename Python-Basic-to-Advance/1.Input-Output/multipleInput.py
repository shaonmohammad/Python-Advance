from customSplit import custom_split
x,y,z = custom_split(input()) # Using input() and split()
print(x,y,z)


x = [i for i in input().split()]  # Takeing multiple input with single space
print(x)


y = [int(z) for z in input().split(",")]  #Taking multiple int input with qomma separed
print(y)


a = map(int,input().split())  #Using map() for Multiple Integer Inputs
print(list(a))


