import tensorflow as tf
import numpy as np

def test():
	print("test")
    
    
def predict_to_number_test():
	X = tf.placeholder(dtype=tf.float32, shape=[None, 784])
	# Y = tf.placeholder(dtype=tf.float32, shape=[None, 10])

	W1 = tf.Variable(tf.random_normal(shape=[784, 256], stddev=0.01), name="w1val")
	L1 = tf.nn.relu(tf.matmul(X, W1))

	W2 = tf.Variable(tf.random_normal(shape=[256, 256], stddev=0.01), name="w2val")
	L2 = tf.nn.relu(tf.matmul(L1, W2))

	W3 = tf.Variable(tf.random_normal([256, 10], stddev=0.01), name="w3val")
	model = tf.matmul(L2, W3)

	saver = tf.train.Saver({"w1val": W1, "w2val": W2, "w3val": W3})

	with tf.Session() as sess:
		saver.restore(sess, "./numberRecognition/static/tf_model/mnist")
		predict = sess.run([model], feed_dict={X: img_arr})
		predict = np.array(predict)
		result = np.argmax(predict[0], axis=1)
		print("result : ", result)
		return result