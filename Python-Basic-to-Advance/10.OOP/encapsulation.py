# Encapsulation is a way that limit the access of data (attribute) from outside of class.Python achieves encapsulation through public,private and prodtected attributes

class Bank:
    def __init__(self,account_name,initial_balance):
        self.name = account_name
        self.__initial_balance = initial_balance

    def get_balance(self):
        return f"Balance is: {self.__initial_balance}"
    
bank = Bank("Afat",1000)
bank.__initial_balance = 500
# print(bank._Bank__initial_balance)
print(bank.__initial_balance)

        