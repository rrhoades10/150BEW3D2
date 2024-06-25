# Inherit from bank account into a Savings Account and a Checkings Account
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    # Method to add the interest to the current balance
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        # calling a method from the parent class
        self.deposit(interest)
        print(f"Interest ${interest} added to your balance.")

    # method overriding - overrides the parent withdraw method to include a withdraw limit
    def withdraw(self, amount):
        if amount > 500:
            print("Withdrawal limit exceeded")
        else:
            # calls the parent version of the withdraw method
            super().withdraw(amount)

# creating a CheckingAccount that also inherits from BankAccount
class CheckingAcount(BankAccount):

    def __init__(self, account_holder, initial_balance, transaction_fee):
        super().__init__(account_holder, initial_balance)
        self.transaction_fee = transaction_fee

    # Override the withdraw method to include the transaction fee
    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        # using getter from the parent method
        if total_amount <= self.get_balance():
            self.set_balance(self.get_balance() - total_amount)
            print(f"Withdrawn: {amount}, Transaction fee: {self.transaction_fee}")
        else:
            print("Insufficient balance for withdrawal and transaction fee.")

# instantiating our accounts
savings = SavingsAccount("Lando", 1500, 0.07)
checking = CheckingAcount("Han", 2000, 20)

# using the savings account
savings.add_interest()
savings.add_interest()
# getter from the parent method
print(savings.get_balance())

# trying to exceed the withdraw limit from savings
savings.withdraw(500)
print(savings.get_balance())

# using our checking account
# calling the parent method of deposit
checking.deposit(1000)
# calling the overriden method
checking.withdraw(500)
# checking out checking balance
print(checking.get_balance())