import random
import time

random.seed(a=1, version=2)
def mtx_mlt(A,B):
	return [[sum([A[i][m]*B[m][j] for m in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))]

n=300
m=300
q=300
p=300
ar1  =[[0 for j in range  (0 , n)] for i in range (0 , m)]
ar2  =[[0 for j in range  (0 , q)] for i in range (0 , p)]

wynik=[[0 for j in range  (0 , q)] for i in range (0 , m)]
m1=[[0 for j in range  (0 , q)] for i in range (0 , m)]

for i in range(0 , m):
	for j in range(0 , n):
		ar1[i][j]=int( random.random()*10 )

for i in range(0 , p):
	for j in range(0 , q):
		ar2[i][j]=int( random.random()*10 )


############################################################
t1=time.clock()
for j in range(0 , q):
	for i in range(0 , m):
		for k in range(0 , n):
			wynik[j][i] += ar1[k][i] * ar2[j][k]   
print(time.clock()-t1)           
############################################################                
t2=time.clock()

mtx_mlt(ar1,ar2)

print(time.clock()-t2)

##########################################                
t3=time.clock()

ar1 = [[row[i] for row in ar1] for i in range(len(ar1[0]))]
for i in range(0 , p):
	for j in range(0 , q):
		a=ar1[i]
		b=ar2[j]
		m1[j][i]=sum([a*b for a,b in zip(a,b)])

print(time.clock()-t3)
##################




'''
for i in range(len(ar2)):
        for j in range(len(ar2[0])):
            print("\t",ar2[i][j],end=" ")
        print("\n")    
print("\n")
for i in range(len(ar1)):
        for j in range(len(ar1[0])):
            print("\t",ar1[i][j],end=" ")
        print("\n")    

print("\n")
for i in range(len(wynik)):
        for j in range(len(wynik[0])):
            print("\t",wynik[i][j],end=" ")
        print("\n")    

print("\n")    
for i in range(len(m1)):
        for j in range(len(m1[0])):
            print("\t",m1[i][j],end=" ")
        print("\n")    
'''
