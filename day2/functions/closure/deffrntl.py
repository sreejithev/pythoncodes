def sqr(x):
	return x*x
def differential(f):
	return lambda x: (f(x+0.0000001)-f(x))/0.0000001
s= differential(sqr)
print s(4)
