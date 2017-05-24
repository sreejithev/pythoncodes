def sqr(x):
	return x*x
def cube(x):
	return x*x*x 
def differential(f):
		return lambda x: (f(x+0.0001)-f(x))/0.0001
p=differential(sqr)
print p(3)
q=differential(cube)
print q(3)

