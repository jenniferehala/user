from typing import NamedTuple


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")


Picard = User('Picard', 'picard@gmail.com')
Riker = User('Riker','riker@gmail.com')
Worf = User('Worf', 'worf@gmail.com')

Picard.make_deposit(50)
Picard.make_deposit(50)
Picard.make_deposit(50)
Picard.make_withdrawal(50)
Picard.display_user_balance()

Riker.make_deposit(200)
Riker.make_deposit(200)
Riker.make_withdrawal(50)
Riker.make_withdrawal(50)
Riker.display_user_balance()

Worf.make_deposit(200)
Worf.make_withdrawal(50)
Worf.make_withdrawal(50)
Worf.make_withdrawal(50)
Worf.display_user_balance()