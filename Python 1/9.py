import random
x=list()
xsort=list()

for i in range(50):
	x.append(random.random())

for i in range(50):
	xsort.append(min(x))
	x.remove(min(x))

print (xsort)	
xsort.sort()
print (xsort)	

