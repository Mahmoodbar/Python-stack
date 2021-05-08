import banAccount
# from banAccount import BankAccount
class User:
    def __init__(self, name, email,int_rate=0.01,balance=0):
        self.name = name
        self.email = email
        self.account = banAccount.BankAccount(int_rate, balance)
    
    def make_deposit(self,amount):
        self.account.deposit(amount)		
        return self

    def make_withdraw(self,amount):
        self.account.withdraw(amount)	
        
    def display_accountinfo(self):
        print('user:', self.name , 'balance', self.account.balance)
    
samer = User('samer','email@email')
samer.make_deposit(50).display_accountinfo()
# samer.account.deposit(50) >>> new method to call the make_deposit

    
# actually when i comment all the lines from 2 up to 16 > it returns the same output for the banAccount >> since i import it 
# so how should i know if its working (the code) or what ? since the output should return the same output as well?