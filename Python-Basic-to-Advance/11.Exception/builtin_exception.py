class InvalidAgeError(Exception):
    def __init__(self,age,msg = "Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'
    
def check_valid_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print("Age set to: ",age)


try:
    check_valid_age(100)
except InvalidAgeError as error:
    print(error)