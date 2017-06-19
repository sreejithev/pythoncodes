class foo:
	pass

def fun(f):
	f.x = 1
fun(foo)

print foo.x
