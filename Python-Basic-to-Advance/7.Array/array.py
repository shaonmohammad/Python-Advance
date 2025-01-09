import array as arr

myarr = arr.array('i',[1,2,3,4,5])
for i in range(0,len(myarr)):
    print(myarr[i],end=" ")
print()


myarr.insert(1,0)
print("After insert :",*myarr)  # Use *myarr for unpack the array element

print(myarr[1])  # Access element by index

myarr.pop(1)

print(*myarr)

myarr[0] = 100  # Update the element by index
print(*myarr)

