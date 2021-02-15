num=int(input("enter the number"))
f=1
if num<0:
	print("the factorial is not exist in negative values")
elif num==0:
	print("the factorial of 0 is 1")
else:
	for i in range(1,num+1):
		f=f*i
print("the factorial of",num,"is",f)
