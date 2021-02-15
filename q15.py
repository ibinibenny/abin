num=int(input("enter the number"))
sum=0
temp=num
while temp>0:
	d=temp%10
	sum+=pow(d,3)
	temp//=10
if num==sum:
	print(" number is armstrong")
else:
	print(" number is not an armstrong")
	