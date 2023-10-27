from bank_account import *

King = BankAccount(1000, "King")
Bee = BankAccount(2000, "Bee")

King.getBalance()
Bee.getBalance()


King.deposit(500)

Bee.withdraw(30000)

King.transfer(300000, Bee)

King.transfer(200, Bee)

Jane = InterestRewardsAcct(10000, "Jane")
Jane.getBalance()
Jane.deposit(1000)

Jane.transfer(100, King)

Jakes = SavingsAcct(1000, "Jakes")
Jakes.getBalance()
Jakes.deposit(100)
Jakes.transfer(1000, Bee)
