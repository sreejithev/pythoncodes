import re
s1 = 'this is a niiice line'
pat1 = r'i+'
r = re.search(pat1,s1)
if r:
	print r.group()

