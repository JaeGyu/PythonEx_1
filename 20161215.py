#_*_ coding: UTF-8 _*_
import tensorflow as tf


a = tf.constant([5],dtype=tf.float32)
b = tf.constant([10],dtype = tf.float32)

d = a + b

sess = tf.Session()
result = sess.run(d)

print(result)
