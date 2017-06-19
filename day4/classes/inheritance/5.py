class account:
	def __init__(self, balance = 0):
		self.balance = balance
	def deposit(self, amt):
		self.balance += amt
	def withdraw(self, amt):
		self.balance += amt
	def check_balance(self):
		return self.balance
class limitedaccount(account):
	def withdraw(self, amt):
		if (self.balance - amt) < 0:
			print 'balance is only: %d' % self.balance
			print 'can not withdraw:%d'% amt
		else:
			self.balance -= amt
			print 'succes'
acc = limitedaccount(500)
acc.withdraw(500)
