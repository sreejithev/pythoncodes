class student:
	def __init__(self, name, age, rank):
		self.name = name
		self.age = age
		self.rank = rank
	def __str__(self):
		return 'name = %s, age = %d, rank = %d' % (self.name, self.age, self.rank)
	def __lt__(self, other):
		if self.rank > other.rank:
			return True
		else:
			return False
student1 = student('John', 20, 100)
student2 = student('Ram', 19, 120)
s = student2 < student1
print s


# s = student2__lt__(student1)
