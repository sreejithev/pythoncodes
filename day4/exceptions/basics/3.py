def fun():
	print 'before...'
	try:
		a = 1/0
		print 'after zerodivision in try block...'
	except:
		print 'caught...'
fun()
