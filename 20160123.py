

L = []
for k in range(10):
	L.append(k*k)

print L


L = [k * k for k in range(10)]
print L


for s in range(10):
	print '*' * s

for s in range(1,11):
	print '*' * s

L = ['*'*s for s in range(1,11)]

print L

L = [k*k for k in range(10) if k % 2]
print L

if 0:
	print 0
else:
	print 1

if 1:
	print 0
else:
	print 1

if -1:
	print 0
else:
	print 1

L = [(i,j,i*j) for i in range(2,20,2) for j in range(3,20,3) if (i+j) % 7 == 0]
print L


for i in range(1,11):
	print ' ' * (11-i) + '*'*i

L = [' ' * (11-i) + '*'*i for i in range(1,11)]
print L

for k in L:
	print k

for i in range(1,11):
	print ' ' * (11-i) + '*'*i

for i in range(1,11):
	print '*' * i

seq1 = 'abc'
seq2 = (1,2,3)

print [(x,y) for x in seq1 for y in seq2]


words = 'The quick brown fox jumps\
 over the lazy dog'.split()

stuff=[[w.upper(), w.lower(), len(w)]
  for w in words]

for i in stuff:
	print i


seq1 = 'abc'
seq2 = (1,2,3)
seq3 = [4,5,6]

L = [(a,b,c) for a in seq1 for b in seq2 for c in seq3]
print L

L = [3,2,1]

print sorted(L)

L.sort()
print L

