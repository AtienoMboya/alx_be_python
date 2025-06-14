class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        return int(self.account_balance + amount)
    
    def withdraw(self, amount):
        if amount < self.account_balance:
            return int(self.account_balance - amount)
        else:
            pass
    
    def display_balance(self):
        print(f'Current Balance: ${self.account_balance:.2f}') #to display the account balance in 2dp