
#l=[]
#n=int(input("enter the number of elements:"))
#for i in range(0,n):
	#elements=input()
	#l.append(elements)
#print(l)


l=[]
n=input("enter the string:")
l.append(n)
for i in n:
	if i not in "a,e,i,o,u,A,E,I,O,U":
		print(i)
print(l)

s = input("Enter any string to remove all vowels:")
vowels = "aeiou"  
s = s.lower()
for x in s:
	if x in vowels:
		s = s.replace(x, " ")   
print(list(s))
