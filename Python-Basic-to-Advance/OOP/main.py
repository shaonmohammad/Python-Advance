from bank import *

shaon = BankAccount("Afat Uddin",1000)

shaon.GetBalance()
shaon.Deposite(200)

shaon.Withdraw(200)

tasruba = BankAccount("Tasruba",500)
tasruba.GetBalance()

shaon.Transfer(500,tasruba)
