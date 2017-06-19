class student:
	pass
student1 = student()
student1.name = 'John'
student1.age = 20
student1.rank = 100

student2 = student()
student2.name = 'Ram'
student.age = 19
student.rank = 120

def higher_rank(a,b):
	if a.rank < b.rank:
		return a
	else:
		return b
s = higher_rank(student1,student2)
print s.name,s.age,s.rank
