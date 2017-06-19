def null(xs):
	return len(xs) == 0

def head(xs):
	return xs [0]

def tail(xs):
	return xs[1:]

def cons(xs):
	return [x] + xs

def is_even(xs):
	return (x%2) == 0

def filter_even(xs):
	# returnj new list composed of even numbers from xs

print filter_even([1,2,3,4])
