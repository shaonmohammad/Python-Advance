keys = [1, 2, 3, 4, 5]
values = ['a', 'b', 'c', 'd', 'e', 'f']
# result = {k: v for (k, v) in zip(keys, values)}

# also can do this
result = dict(zip(keys, values))

# print(result)


# Using dictionary comprehension make dictionary
mydict = {x: x*x if x > 2 else x for x in range(0, 5)}
print(mydict)
