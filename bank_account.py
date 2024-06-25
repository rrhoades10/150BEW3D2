# getters and setters within a bankaccount
class BankAccount:   #                                    default parameter of 0 - 
    
    def __init__(self, account_holder, initial_balance=0):
        # private attribute
        self.__balance = initial_balance
        # public attribute
        self.account_holder = account_holder

    # getter for the balance
    def get_balance(self):
        return self.__balance
    
    # setter balance
    def set_balance(self, new_balance): #used for depositing and withdrawing from our account
        self.__balance = new_balance

    # getter for account_holder
    def get_account_holder(self):
        return self.account_holder
    
    # setter for account_holder
    def set_account_holder(self, new_holder):
        self.account_holder = new_holder
    
    # deposit - use our setter to change the balance
    def deposit(self, amount):
        if amount > 0:
            #                using the getter to access the curent balance and add it to passed in argument
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited: ${amount}")
        else:
            print("Invalid Deposit Amount")

    # withdraw
    def withdraw(self, amount):
        if 0 < amount < self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid withdrawal ammount of insufficient balance")