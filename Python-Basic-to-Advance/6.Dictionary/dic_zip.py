# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

dic = {k:v for (k,v) in zip(keys,values)}
print(dic)

#Using fromkeys() Method
dic2 = dic.fromkeys(keys,None)
print(dic2)