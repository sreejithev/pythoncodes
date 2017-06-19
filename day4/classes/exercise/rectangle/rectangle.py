class rectangle:
	def __init__(self, a, b):
		self.length = a
		self.breadth = b
	def smaller(self, other):
		return self.length*self.breadth < other.length*other.breadth
	def __lt__(self, other):
		return self.length*self.breadth < other.length*other.breadth
a = rectangle (3, 4)
b = rectangle (4, 5)
print a.smaller(b)	#print true
print b < a		#print false
