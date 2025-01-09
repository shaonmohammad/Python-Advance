class BalanceException(Exception):
    pass
class BankAccount():
    def __init__(self,account_name,initial_amount):
        self.account_name = account_name
        self.balance = initial_amount
        print(f"Account Created {self.account_name}")

    def GetBalance(self):
        return print(f"Account:{self.account_name} balance is :{self.balance}💵")

    def Deposite(self,amount):
        self.balance += amount
        print("Deposite Completed.✅")
        self.GetBalance()

    def ViableTransaction(self,amount):
        
        if self.balance > amount:
            return 
        else:
            raise BalanceException(
                (f"Sorry, {self.account_name} have only {self.balance} taka")
            )
          
    def Withdraw(self,amount):
        try:
            self.ViableTransaction(amount)
            self.balance -= amount
            print("Withdraw is Completed✅")
            self.GetBalance()
        except BalanceException as error:
            print(f"Withdraw interrepted ❌:{error}")

    def Transfer(self,amount,account):
        try:
            print("Start Transaction....🚀")
            self.ViableTransaction(amount)
            self.balance -= amount
            account.Deposite(amount)
            print("Transfer Completed ✅")
        except BalanceException as error:
            print(f"Transfer Failed❌:{error}")

