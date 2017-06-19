class student:
        def __init__(self,name,age,rank):
                self.name = name
                self.age = age
                self.rank = rank  
student1 = student('John', 20, 100)
student2 = student('Ram', 19, 120)

def higher_rank(a,b):
        if a.rank < b.rank:
                return a
        else:
                return b
s = higher_rank(student1,student2) 
print s.name,s.age,s.rank 


