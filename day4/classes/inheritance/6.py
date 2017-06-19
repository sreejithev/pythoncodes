class A:
	def fun1(self):
		print 'A: fun1'
class B:
	def fun1(self):
		print 'B: fun1'
class C(A, B):
	pass
p = C()
p.fun1()
	
