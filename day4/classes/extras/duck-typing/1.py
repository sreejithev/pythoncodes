class duck:
	def quack(self):
		print 'quack quack'

def handle_duck(d):
		d.quack()

d = duck()
handle_duck(d)
