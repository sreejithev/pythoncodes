import re
s1 = 'this is a nice line'
pat1 = r'i+s'
r= re.search(pat1,s1)
if r:
	print r.group()

