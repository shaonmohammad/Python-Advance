# A generator is just like a normal function.it used yield keyword instead of return keyword

def mygenerator():
    yield 1
    yield 2
    yield 3

result = mygenerator()
value = next(result)
print(value)

value = next(result)
print(value)

value = next(result)
print(value)


def my_countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = my_countdown(4)
cd_result = next(cd)
print(cd_result)
cd_result = next(cd)
print(cd_result)

cd_result = next(cd)
print(cd_result)
cd_result = next(cd)
print(cd_result)


def sum_nums(n):

    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def sum_nums_generator(n):
    nums = []
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(sum_nums(5)))
