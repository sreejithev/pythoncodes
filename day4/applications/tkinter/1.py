from Tkinter import *

def fun():
	print 'button clicked...'

def main():
	r = Tk()

	b = Button(r, text='Ok', command = fun)
	b.pack()
	r.mainloop()

main()
