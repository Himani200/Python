#!usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]

a=[]
b=[]

print("No. greater than 5:")
for i in adhoc:
	if i > 5 :
		a.append(i)		
print(a)

print("Nos. less than or equal to 2")
for i in adhoc:	
	if i <= 2 :
		b.append(i)
print(b)

