import re
s1 = '1250:5012'
pat1 = r'(\d+):(\d+)'
r = re.search(pat1,s1)
if r:
	print r.group()
	print r.group(1)
	print r.group(2)

