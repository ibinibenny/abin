p='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string=input("enter the string")
np=""
for char in string:
	if char not in p:
		np=np+char
print(np)