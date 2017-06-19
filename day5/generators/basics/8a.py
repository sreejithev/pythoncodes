def small_lines(filename, n):
	result = []
	for line in open(filename):
		if len(line) < n:
			result.append(line)
	return result

def grep(lines, word):
	for line in lines:
		if word in line:
			print line

r = small_lines('data.txt', 10)

grep(r, 'ok')

