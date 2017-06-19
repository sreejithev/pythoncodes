class duck:
	def quack(self):
		print 'quack quack'

class lookslikeduck:
	def quack(self):
		print 'lookslikeduck: quack quack'

	def run(self):
		print 'lookslike: run'
def handle_duck(d):
	d.quack()

d = lookslikeduck()
handle_duck(d)

