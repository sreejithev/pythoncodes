x = 100
class foo:
	x = 150
	def __init__(self):
		self.x = 10
	def show(self):
		print foo.x
a = foo()
a.show()

