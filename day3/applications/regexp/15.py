import re
s1 = 'My number: 9633819750.Please do not call'
pat1 = r'\d+'
r = re.search(pat1,s1)
if r:
	print r.group()


#\d matches single occurrence of a decimal digit(0,1....9)

