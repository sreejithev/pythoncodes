def countdown(n):
	while n > 0:
		yield n
		n -= 1
c = countdown(3)

for k in c:
	print k
