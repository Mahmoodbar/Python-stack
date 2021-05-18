class BankAccount:
	def __init__(self,int_rate=0.01,balance=0):
		self.int_rate = int_rate
		self.balance = balance
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
			self.balance = (self.balance * self.int_rate) + self.balance
		return self	



if __name__ == "__main__":
 
	mostafa=BankAccount(0.02,8000)
	mostafa.deposit(1000).withdraw(200).withdraw(300).withdraw(50).withdraw(50).yield_interest().display_account_info()
	# mahmood=BankAccount(0.02,5000)

