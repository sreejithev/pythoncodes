def fun2():
	print 'before..'
	try:
		a = 1/0
	except:
		print 'caught..'

def fun1():
	fun2()
	print 'end of fun1...'
fun1()
