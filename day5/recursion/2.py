def null(xs):
	return len(xs) == 0

def head(xs):
	return xs[0]

def tail(xs):
	return xs[1:]

def my_len(xs):
# Recursively compute length
	if (null(xs)):
		return 0
	return 1 + my_len(tail(xs))
