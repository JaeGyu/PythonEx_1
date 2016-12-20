#_*_ coding: utf-8 _*_
import tensorflow as tf

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a,b) #텐서플로에 있는 add라는 함수를 사용한다. 파라매터 a,b는 위에서 placeholder를 통해 정의 해준 int16형의 데이터만 받겠다 
mul = tf.mul(a,b)

with tf.Session() as sess:
	print "-"*60
	print "Addition with variables: %i" % sess.run(add, feed_dict={a:2, b:3.4})
	print "Multiplication with variables: %i" % sess.run(mul, feed_dict={a:2,b:3.4})
	print "-"*60


