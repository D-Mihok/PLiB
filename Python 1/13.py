import random
n=2
m=2
q=2
p=2
ar1=[[0 for j in range  (0 , n)] for i in range (0 , m)]
ar2=[[0 for j in range  (0 , q)] for i in range (0 , p)]
wynik=[[0 for j in range  (0 , q)] for i in range (0 , m)]
 

for i in range(0 , m):
	for j in range(0 , n):
		ar1[i][j]=int (	random.random()*10 )

for i in range(0 , p):
	for j in range(0 , q):
		ar2[i][j]=int( random.random()*10 )

for i in range(0 , m):
	for j in range(0 , q):
		wynik[i][j] += ar1[i][j] + ar2[i][j]
                

for i in range(len(ar1)):
        for j in range(len(ar1[0])):
            print("\t",ar1[i][j],end=" ")
        print("\n")    
                
print("\n")

for i in range(len(ar2)):
        for j in range(len(ar2[0])):
            print("\t",ar2[i][j],end=" ")
        print("\n")    
print("\n")


for i in range(len(wynik)):
        for j in range(len(wynik[0])):
            print("\t",wynik[i][j],end=" ")
        print("\n")    

