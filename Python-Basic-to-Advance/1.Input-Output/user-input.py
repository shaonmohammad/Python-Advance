import datetime
#Taking input in Python
value = input("Enter the value: ")
print(type(value))

#There are various function that are used to take as desired input few of them are : –
# int(input())
# float(input())

#How to input time in Python?
time_str = input("Enter the Time format %HH:MM%:%SS: ")
time = datetime.datetime.strptime(time_str,"%H:%M:%S")
print(type(time))