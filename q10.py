string=input("enter the string")
str1=""
for i in string:
		str1=i+str1
		#print("reverse string:", str1)
if(string==str1):
		print("it is palindrome")
else:
		print("it is not palindrome")