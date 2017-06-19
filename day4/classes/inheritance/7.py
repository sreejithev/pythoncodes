class A:
	def fun2(self):
		print 'A:fun2'
class B(A):
	pass
class C:
	def fun1(self):
		print 'C: fun1'
class D(B,C):
	pass
p = D()
p.fun1()
