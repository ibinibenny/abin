a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3nd number"))
if (a<=b) and (a<=c):
	largest=a
elif (b<=a) and (b<=c):
	largest=b
else:
	print("largest is:",largest)
