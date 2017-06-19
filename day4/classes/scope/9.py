class account:
	num_accounts = 0
	
	def __init__(self, balance = 0):
		self.balance = balance
		account.num_accounts += 1

	def deposit(self, amt):
		self.balance += amt
	
	def withdraw(self, amt):
		self.balance -= amt

	def check_balance(self):
		return self.balance

acc1 = account()
acc1.deposit(100)
print acc1.check_balance()

acc2 = account()
acc2.deposit(200)
print acc2.check_balance()

print 'Total number of accounts = %d ' % account.num_accounts
