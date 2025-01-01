from collections import Counter, namedtuple, OrderedDict, defaultdict

a = "aaaaaabbbbcccccdddd"
my_counter = Counter(a)

# to find most common
# print(my_counter.most_common(1))

# to convert each element of string as a list item
# print(list(my_counter.elements()))


# working with nametuple
# this is mainly used to crated a class in single line with attribute


# Working with OrderDict
order_dic = OrderedDict()
order_dic['a'] = 1
order_dic['b'] = 2
order_dic['c'] = 3
order_dic['d'] = 4
# print(order_dic['b'])


# Working with defaultdict
# It used if i want to use default value of any key
mydic = defaultdict(list)

mydic['a'] = 1
mydic['b'] = 2
mydic['c'] = 3

# print(mydic['d'])
