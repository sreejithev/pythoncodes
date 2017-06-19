# handling tree-like structure

my_expression = 12

def eval(expr):
	if isinstance(expr, int):
		return expr

print eval(my_expression)
