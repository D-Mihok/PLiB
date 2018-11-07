f = open("PanTadeusz.txt", 'r')

t = str( f.read() )

	print(t)

a=t.replace("i", "oraz")

f.closed
print(a)
f = open("PanTadeusz.txt", 'w')
f.write(a)
f.close
