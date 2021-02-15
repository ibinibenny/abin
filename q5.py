t=int(input("how many terms needed"))
x=0
y=1
c=0
if t<=0:
	print("intiger is")
elif t==1:
	print("fibonocci",t,":")
	print(x)
else:
	print("fibonocci series ")
	while c<t:
		print(x)
		z=x+y
		x=y
		y=z
		c=c+1

