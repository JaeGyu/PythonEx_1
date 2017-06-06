import tensorflow as tf
import numpy as np
	
class Predict:
	def __init__(self):
		self.X = tf.placeholder(dtype=tf.float32, shape=[None, 784])

		self.W1 = tf.Variable(tf.random_normal(shape=[784, 512], stddev=0.01), name="w1val")
		self.B1 = tf.Variable(tf.random_normal(shape=[512], stddev=0.01), name="b1val")
		self.L1 = tf.nn.relu(tf.add(tf.matmul(self.X, self.W1), self.B1))

		self.W2 = tf.Variable(tf.random_normal(shape=[512, 256], stddev=0.01), name="w2val")
		self.B2 = tf.Variable(tf.random_normal(shape=[256], stddev=0.01), name="b2val")
		self.L2 = tf.nn.relu(tf.add(tf.matmul(self.L1, self.W2), self.B2))

		self.W3 = tf.Variable(tf.random_normal(shape=[256, 128], stddev=0.01), name="w3val")
		self.B3 = tf.Variable(tf.random_normal(shape=[128], stddev=0.01), name="b3val")
		self.L3 = tf.nn.relu(tf.add(tf.matmul(self.L2, self.W3), self.B3))

		self.W4 = tf.Variable(tf.random_normal([128, 10], stddev=0.01), name="w4val")
		self.B4 = tf.Variable(tf.random_normal(shape=[10], stddev=0.01), name="b4val")
		self.model = tf.add(tf.matmul(self.L3, self.W4), self.B4)

		saver = tf.train.Saver(
			{"w1val": self.W1, "w2val": self.W2, "w3val": self.W3, "w4val": self.W4, "b1val": self.B1, "b2val": self.B2, "b3val": self.B3, "b4val": self.B4})
		
		self.sess = tf.Session()
		saver.restore(self.sess, "./numberRecognition/static/tf_model/mnist")
		
	def predict(self, img_arr):
		predict = self.sess.run([self.model], feed_dict={self.X: img_arr})
		predict = np.array(predict)
		result = np.argmax(predict[0], axis=1)
		print("result : ", result)
		return result
    