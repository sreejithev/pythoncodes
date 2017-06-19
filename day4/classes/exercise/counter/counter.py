class counter:
	def __init__(self, count=0):
		self.c = count

	def increment(self):
		self.c += 1

	def decrement(self):
		self.c -= 1

	def show(self):
		print self.c

	def __str__(self):
		return 'counter : %d' % self.c

c = counter()
c.show()	#prints 0
c.increment()
c.show()	#prints 1
c.decrement()
c.show()	#prints 0
print c		#prints counter: 0 (implement the __str__method)
c = counter(10)	#__init__should accept an argument
c.show()	#prints 10
