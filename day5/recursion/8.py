# handling tree-like structure

my_expression = ['+', ['+',3,4],8]

def eval(expr):
	if isinstance(expr, int):
		return expr
	else:
		if expr[0] == '+':
			return ???

print eval(my_expression)
