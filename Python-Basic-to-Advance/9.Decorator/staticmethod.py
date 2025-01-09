class User:
    def __init__(self,username,password):
        self.username = username
        if not self.check_valid_password(password):
            raise ValueError("Invalid Password❌")
        self.password = password
       
    @staticmethod
    def check_valid_password(password):
        return len(password) > 3

try:
    user = User("Afat","1234")
    print("CREATED✅")
except ValueError as error:
    print(error)

        