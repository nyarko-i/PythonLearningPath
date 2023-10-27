# Creating a banking system


# Catching errors after trying to withdraw more than you have in your account
class BalaceException(Exception):
    pass

# Creating the bank account class


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):  # a function to know the balance in your account
        print(f"\nAccount '{self.name}' balance =${self.balance:.2f}")

    def deposit(self, amount):  # A deposite function allowing you to  deposit into the account
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    # A fucntion (method) to help catch the exception handling above
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalaceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):  # This Function allows users to withdraw their funds
        # Trying and raising an eror when you engtger an amount greater than the amount in your account
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalaceException as error:
            print(f"\nWithdraw interrupted: {error}")

    # Transfer method and also checking for a viable transaction and allowing to transfer to other accounts

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBegining Transfer..🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!✅ \n\n**********')
        except BalaceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

# creating an inheritance class where it overrides the deposit methods and uses the parents class


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


# creating  a savings account that inherits from the interest rewwards class
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalaceException as error:
            print("\nWithdraw interrupted: {error}")
