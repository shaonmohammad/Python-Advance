"""
======================Iterable vs Iterator:=================================
:::Iterable:::
An iterable is any object that can be looped over, like lists, tuples, strings, or dictionaries. It implements the __iter__() method, which returns an iterator.

:::Iterator:::
An iterator is an object that produces values one at a time when you call its __next__() method. It implements both the __iter__() and __next__() methods.

"""

mylist =[3,4,"acb"]  #This is Iterable object.Also iterable object like:tuple,dictionary,set

itr = iter(mylist)
print(itr.__next__())  #This next method is iterator that loop of the iterable object
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())  #This line will raise an Exception(StopIteration) since the value of mylist(iterable) is over. 