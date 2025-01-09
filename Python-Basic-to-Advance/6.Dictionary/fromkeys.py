#Demonstrating the working of fromkeys() 
seq = {'a', 'b', 'c', 'd', 'e'}
list1 = [1,2]

dic1 = dict.fromkeys(seq,list(list1))
print(dic1)

list1.append(3)
print(dic1)

""""
 Here in the case of fromkeys, when we modfiy the value of keys(mutable) after create the dictionary then it reflect the dict's values.To solved this,we can use dictionary comprehension
"""
list2 = [3,4]
dic2 = {k:list(list2) for k in seq}
print(dic2)
list2.append(5)
print(dic2)