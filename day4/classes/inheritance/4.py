class foo:
	def fun1(self):
		print 'foo: fun1'
	def fun2(self):
		print 'foo: fun2'
class bar(foo):
	def fun1(self):
		print 'bar: fun1'
b = bar()
b.fun1()
b.fun2()
