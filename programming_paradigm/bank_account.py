# Define a class named BankAccount.
class BankAccount:

    # Using __init__ method to initialize account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero

    def __init__(self, account_balance, balance=0):
        self.account_balance = account_balance
        self.balance = balance

    # Deposit Method to add the specified amount to account_balance
    def deposit(self, amount):
        if amount > 0:
            return self.account_balance + amount

    # withdraw Method to deduct the amount from account_balance if funds are sufficient
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            return self.account_balance - amount
        

    # display_balance prints the current balance in a user-friendly format
    def display_balance(self):
        return "Current Balance:", self.balance