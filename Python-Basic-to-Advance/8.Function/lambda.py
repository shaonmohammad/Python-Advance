n = int(input())
a = lambda n:"Positive" if n % 2 == 0 else "Negetive"
print(a(n))

b = lambda a,b:[print(i,end=" ") for i in range(a,b+1)]
b(1,100)


# sort string by length
words = ["apple", "kiwi", "banana", "cherry"]
c = lambda words:sorted(words,key=len)
print(c(words))

# reverse string list
words2 = ["hello", "world", "python"]
d = lambda words2:list(map(lambda w:''.join(reversed(w)),words2))
d2 = lambda words2:[word[::-1] for word in words2]  # Alternaive best approch
print(d(words2))

