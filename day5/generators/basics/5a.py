def countdown(n):
	while n > 0:
		yield n
		n -= 1

c = countdown(10)

d = list(c)

print d
