#_*_ coding: utf-8 _*_

order = "a"
menu = {"a":100,
                "b":200,
				"c":300,
				"d":400}
price = menu[order]
print price

a = ['cat','cow','tiger']

for x in a:
	print len(x),x,
print 

for x in [1,2,3]:
	print x,
print

for x in range(10):
	print x,
print 

sum = 0
for x in range(1,11):
	sum+=x
print sum

prod =1
for x in range(1,11):
	prod *= x
print prod

l = ['cat','dog','bird','pig']
for k,animal in enumerate(l):
	print k,animal

for k in enumerate(l):
	print k

d = {'c':'cat',
        'd':'dog',
		'b':'bird',
		'p':'pig'}
for idx,keyOfD in enumerate(d):
	print idx,keyOfD,d[keyOfD]

for x in range(10):
	if x>3:
		break
	print x
else:
	print 'else block'
print 'done\n'

for x in range(10):
	if x % 2 == 0:
		continue
	print x
else:
	print 'else block'
print 'done\n'

for x in range(10):
	print x,
else:
	print 'else block'
print 'done\n'

for x in range(2,10):
	for y in range(1,10):
		print "%d * %d = %d" % (x,y,x*y)
	print 

count = 1
while count < 11:
	print count
	count += 1



	
