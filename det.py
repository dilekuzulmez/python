det=0
x=1
y=2
det=det(x,y)*(-1)**(x,y)+[(x,y)*(-(x,y))-(x,y)*(x,y)]
if y==3:
	print det
else:
	y=y+1
	print det
