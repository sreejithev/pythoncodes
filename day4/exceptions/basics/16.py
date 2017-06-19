a = []
try:
	print a[0]
except (NameError, ZeroDivisionError):
	print 'divide by zero symbol not defined error'
