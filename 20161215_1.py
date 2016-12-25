#_*_ coding: UTF-8 _*_

import tensorflow as tf

a = tf.constant('*')

sess = tf.Session()

print sess.run(a)


for i in range(1,10):
	print '*' * i

print "----------------------"


for i in range(0,10):
	for j in range(0,i):
		print sess.run(a),
	print 


