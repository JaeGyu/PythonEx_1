#_*_ coding: utf-8 _*_
import tensorflow as tf

# Start tf Session
sess = tf.Session()

a = tf.constant(2) #2를 상수로 준 a는 오퍼레이션이다.
b = tf.constant(3) #3을 상수로 준 b는 오퍼레이션이다.

c = a+b #c역시 오퍼레이션이다. 

print "-"*60
print c #c를 출력을 하면 의미 없는 값이 나온다. 

print sess.run(c)
print "-"*60
