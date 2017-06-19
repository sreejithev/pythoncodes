# Return lines having the specified world in them

def grep(lines, word):
	for line in lines:
		if word in line:
			print line
