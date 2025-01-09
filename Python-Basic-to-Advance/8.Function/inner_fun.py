# Uses of nonlocal keyword
def parent(input):
    input = input
    def child():
        nonlocal input
        print(input)
    child()
    print(input)

parent("Tasruba")


# Closure in Python
def increase_value(value):
    count = 100
    def increase():
        nonlocal count
        count+=value
        return count
    return increase

counter = increase_value(100)  # create a closure
print(counter())
print(counter())
