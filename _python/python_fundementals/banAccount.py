class BankAccount:
	def __init__(self,int_rate,balance):
		self.int_rate = 0.2
		self.balance = 0
	def deposit(self, amount):
		self.balance += amount
		return self
	def withdraw(self, amount):
		self.balance -= amount
		return self
	def display_account_info(self):
		print(self.balance)
		print(self.int_rate)
		return self
	def yield_interest(self):
		if self.balance >0:
			self.balance = (self.balance * self.int_rat) + self.balance
		return self		

mahmood=BankAccount(0.2,500)
mostafa=BankAccount(0.2,700)
mahmood.deposit(200).withdraw(200).withdraw(300).withdraw(50).withdraw(70).yield_interest().display_account_info()