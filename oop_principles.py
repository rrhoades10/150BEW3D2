# Object Oriented Principles
# Guidelines for writing OOP well


# Encapsulation - Data Bundling or Data Hiding within our Classes
# allows to have more control over who and what is accessing our class attributes and methods
# packages attributes and methods managing their accessibility

# Public Attribute - most accessible - accessible within the class and outside the class their defined in
# self.name

# Protected Attribute - mildly accessibly - only accessibly within the class and subclasses(classes that inherit)
# self._settings --- underscore to denote a protected attribute

# Private Attribute - least accessible -  only accessible within the class they're defined in.
# self.__id
# Python does the best job at actually guarding with the naming convention
# __ python mangles the attribute so we cant access it by the name



#^^ PYTHON NAMING CONVENTIONS FOR THE ATTTRIBUTES ^^

class SmartPhone:
    def __init__(self, model, operating_system, serial_number,):
        self.model = model # Public Attribute
        self._operating_system = operating_system #Protected Attribute
        self.__serial_number = serial_number

    def show_info(self):
        print(f"Model: {self.model}")
        print(f"Operating System: {self._operating_system}")
        # we only want to access private attributes through getters and setters
        # use those getters or setters in other methods
        # check out getters and setters below
        print(f"Serial Number: Private for security reasons ...")

# creating an instance of our smartphone
my_phone = SmartPhone("Iphone 13", "IOS", "v37b45")

# accessing a public attribute
print(my_phone.model)

# accessing a protected attribute - this is possible - BUT its not recommended
print(my_phone._operating_system)  # BUT YOU SHOULDN'T....please

# trying to access a private attribute will give you an error
# print(my_phone.__serial_number) # AttributeError
print(my_phone._SmartPhone__serial_number) # accessing the mangled private attribute

# calling the show_info method
my_phone.show_info()

# Implenting Getters and Setters 

# getter is a class method that is used to read or access private attributes
# setter is a method that allows us to change the value of private attributes

# provide controlled ways to interact with our class attributes, whether its viewing or modifying
class SmartPhone:
    def __init__(self, model, operating_system, serial_number,):
        self.model = model # Public Attribute
        self._operating_system = operating_system #Protected Attribute
        self.__serial_number = serial_number

    def show_info(self):
        print(f"Model: {self.model}")
        print(f"Operating System: {self._operating_system}")
        # we only want to access private attributes through getters and setters
        # use those getters or setters in other methods
        # check out getters and setters below
        print(f"Serial Number: Private for security reasons ...")

    # getter for the __serial_number
    def get_serial_number(self):
        # only thing a getter needs to do is return the specified attribute
        return self.__serial_number
    
    # setter for the __serial_number
    def set_serial_number(self, new_number):
        self.__serial_number = new_number


my_phone = SmartPhone("IPhone 13", "IOS", "x2bn64")
# using the getter
serial_number = my_phone.get_serial_number()
print(serial_number, "before calling the setter")
# using the setter
my_phone.set_serial_number("g23n769")
print(my_phone.get_serial_number(), "after calling the setter")


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

# using our bank account
account = BankAccount("Ryan", 1000)
print(f"Account Holder: {account.get_account_holder()}")
print(f"Initial Balance: ${account.get_balance()}")

# depositing and withdrawing from our account
account.deposit(700)
account.withdraw(200)
print(f"Updated Balance: ${account.get_balance()}")

# changing the account holder
account.set_account_holder("Selena")
print(f"New Account Holder: {account.get_account_holder()}")

# new_holder = input("who is the new person? ")
# account.set_account_holder(new_holder)
# account.account_holder = new_holder


# Inheritance - Classes can inherit functionaly and attributes from other classes
# while also having their own unique functionality

# Parent Class - Super Class
class SmartPhone:
    def __init__(self, model):
        self.model = model

    def make_call(self, number):
        print(f"Making a call to {number}")

    def send_message(self, number, message):
        print(f"Sending a message tp {number}: {message}")

# Child Class - Sub Class
#                      class we're inheriting form goes in the parentheses
class SmartCameraPhone(SmartPhone):
    def __init__(self, model, camera_resolution):
        # super.init() - calls the init of the parent class and initializes any of those attributes
        super().__init__(model) # ** also calls any method from the parent class
        self.camera_resolution = camera_resolution
    
    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution} resolution. Like and subscribe ttyl omg hagas")

# creating instances of the parent class
boring_phone = SmartPhone("Nokia Brick Phones")
# calling parent methods through the parent class
boring_phone.send_message("773202LUNA", "Im tryign to get some new floors. What can you do for me? Also great jingle")
boring_phone.make_call("6308675309")
# trying to call the child method through parent calss - AttributeError
# boring_phone.take_photo() - cannot access methods in the child class

# creating instances of the child class
banana_phone = SmartCameraPhone("Cool Updated Phone", "4k")
# accessing attributes from the parent class
print(banana_phone.model)
# parent class methods
banana_phone.send_message("7489541235", "Hi sweetie, don't forget to eat your vegetables at lunch today. You really need more fiber in your diet.")
banana_phone.make_call("7894561232")
# accessing the child method that is UNIQUE to the child class
banana_phone.take_photo()





# Polymorphism - the ability of objects of different classes to respond to the same method call in in their 
# own unique ways - method overloading - repurposing methods from an inherited class

# Method Overloading - when we keep the same method name as the parent class but the number of paremeters or the type of parameters change
class Character:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name
    # parent method
    def attack(self, damage):
        print(f"You attack for {damage} damage")

    


class Ranger(Character):
    def __init__(self, name, class_name):
        super().__init__(name, class_name)
#   method overloading - changing the number of paramaters
    def attack(self, damage, weapon, damage_type):
        print(f"You attack with {weapon} for {damage} {damage_type} damage")

generic_character = Character("Bartholomeu", "Fighter")
generic_character.attack(10)

cool_character = Ranger("Percy", "Ranger")
cool_character.attack(16, "long bow", "piercing")




# Method Overiding - keep the same method name as the parent class - changes the implementation - the functionality may change

# Abstraction - The layer between the functionality of the code and the code itself. 
# creating cli applications


# class Character:
    
#     # class attribute - shared across all instances of the class
#     gold = 0

#     def __init__(self, name, class_type):
#         self.name = name
#         self.class_type = class_type

#     def collect_gold(self, amount):
#         Character.gold += amount

# archer = Character("Legolas", "Archer")
# fighter = Character("Aragorn", "Fighter")
# barbarian = Character("Gimli", "Barbarian")

# print(archer.gold)
# print(fighter.gold)
# print(barbarian.gold)
# archer.collect_gold(20)
# print(archer.gold)
# print(fighter.gold)
# print(barbarian.gold)



