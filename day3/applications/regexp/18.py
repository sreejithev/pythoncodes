import re
s1 = 'this number,12345 and also this one 6789,one more 192837'
pat1 = r'\d+'
r = re.findall(pat1,s1)
print r

