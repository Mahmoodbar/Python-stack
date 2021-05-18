class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print ('name:',self.name,'account_balance:',self.account_balance)
    
    def  transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)


mahmood = User("Mahmood Barakat", "email@email")
mostafa = User("mostafa barakat", 'email@@email')
mohamad = User ('Mohamad Barakat', 'email@@@email')


mahmood.make_deposit(8000)
mahmood.make_deposit(200)
mahmood.make_deposit(300)
mahmood.make_withdrawal(550)

mostafa.make_deposit(200)
mostafa.make_deposit(8000)
mostafa.make_withdrawal(300)
mostafa.make_withdrawal(400)

mohamad.make_deposit(5800)
mohamad.make_withdrawal(300)
mohamad.make_withdrawal(300)
mohamad.make_withdrawal(600)

mahmood.transfer_money(mohamad ,800)

mohamad.display_user_balance()
mahmood.display_user_balance()