

class BankAccount:

    def __init__(self, int_rate = 0.01 , balance = 0.00): 

        self.int_rate = int_rate
        self.balance = balance

        
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self



    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient Funds Charging Fee of $5!')
            self.balance = self.balance - 5
            return self
        else:
            self.balance = self.balance - amount
            return self
    
    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self

    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
            return self


class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02,0.00)
    
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self




account1 = BankAccount()
account2 = BankAccount()
account3 = User('Joe', 'J@DOJO.COM',)



account1.deposit(3000).deposit(300).deposit(700).withdraw(3200).display_account_info()
account2.deposit(100).deposit(1000).withdraw(150).withdraw(100).withdraw(100).withdraw(200).display_account_info()
account3.make_deposit(1000).display_user_balance()