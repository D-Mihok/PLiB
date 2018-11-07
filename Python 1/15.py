import numpy
import random
x=list()

for i in range(16):
	x.append(random.random())


x = reshape(x,(4,4)) 
print(numpy.linalg.det(x))
