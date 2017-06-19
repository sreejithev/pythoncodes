class mycomplex():
	def __init__(self, re, im):
		self.re = re 
		self.im = im
	def add(self, other):
		return mycomplex(self.re + other.re, self.im + other.im)
	def _add__(self, other):
		return mycomplex(self.re + other.re, self.im + other.im)
	def __str__(self):
		return '(%d + %dj)' % (self.re, self.im)
c = mycomplex(1, 2)
d = mycomplex(3, 4)
e = c.add(d)
print c.re, c.im	#prints 4,6
print c			#print (4+6j)..#implement __str__method
#e = c + d		#implement the__add__method
print e
