def sum(a,b):
	s=0
	while(a<=b):
		s=s+a
		a=a+1
	return s
print sum(1,4)

def sum_squares(a,b):
	s=0
	while(a<=b):
		s=s+a*a
		a=a+1
	return s
print sum_squares(1,4)

def sum_cubes(a,b):
	s=0
	while(a<=b):
		s=s+a*a*a
		a=a+1
	return s
print sum_cubes(1,4)

def sum_odd_cubes(a,b):
	s=0
	while(a<=b):
		s=s+a*a*a
		a=a+2
	return s
print sum_odd_cubes(1,4)

