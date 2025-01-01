# 2 types of decorator
# Function decorator and Class Decorator

# Decorator basically is a function that take a function as a perameter and chnage the beheaver fo this funtion

def start_end_decorator(func):
    def wraper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wraper


@start_end_decorator
def make_double(x):
    return x * 2


# start_end_decorator(print_name)()
result = make_double(4)
print(result)
