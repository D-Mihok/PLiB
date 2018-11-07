import random
a=[1,2,12,4]
b=[2,4,2,8]



x=0

 
for k in range(0,len(a)):
	x += a[k] * b[k]

print(x)

x=[a*b for a,b in zip(a,b)]
print(x)

