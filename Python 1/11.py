f = open("PanTadeusz.txt", 'r')

slownik = {'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy' , 'dlaczego' : 'czemu'}

t = str( f.read() )
print(t)

for slowo, first in slownik.items():
	a = t.replace(slowo.lower(), first)

f.closed

print(a)

f = open("PanTadeusz.txt", 'w')
f.write(a)
f.close
