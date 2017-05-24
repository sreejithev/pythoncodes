from pylab import *
x=linspace(0,2*pi,400)
y=sin(x)
i=3
n=0
while(n < 100):
	y=y+(1.0/i)*sin(i*x)
	i=i+2
	n=n+1
plot(x,y)
show()


#write a "while" loop which will sum the first 100 terms of the
#series: sin(x) + (1.0/3)*sin(3*x) + (1.0/5)*sin(5*x) + ...
#the result should be in y
