num = 0
sumw = 0
for num in range(num,12):
	sumw=sumw+bin(2**num).count('1')
print sumw
