class D(object):
	def __init__(self):
		self.x = 10
		print 'A: __init'
	def fun1(self):
		print 'D: fun1'
class B(D):
	def __init__(self):
		self.y =20
		super(B, self).__init__()
		super(B, self).fun1()
p = B()
