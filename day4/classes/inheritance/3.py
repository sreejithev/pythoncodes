class foo:
	def fun1(self):
		print 'foo:fun1'
class bar(foo):
	def fun2(self):
		print 'bar: fun2'
b = bar()
b.fun1()
