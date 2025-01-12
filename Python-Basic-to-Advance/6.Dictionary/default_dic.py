from collections import defaultdict

dic = defaultdict(list)
print(dic)

dic['a'] = 1
dic['b'] = 2
dic['fruits'].append('apple')
dic['vegetables'].append('carrot')
dic['fruits'].append('onion')
print(dic)

print(dic['unknown'])