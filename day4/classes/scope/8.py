x = 100
class foo:
	x = 150

	def __init__(self):
		self.x = 10

	def show(self):
		print foo.x
	def inc(self):
		foo.x +=1
a = foo()
a.show()
a.inc()

b = foo()
b.show()

