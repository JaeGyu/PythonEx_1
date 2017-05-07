import tensorflow as tf
import json

#x_train = [1,2,3]
#y_train = [1,2,3]

#위의 x와 y를 placeholder로 줄 수 있다. 

x_train = tf.placeholder(tf.float32, shape=[None])
y_train = tf.placeholder(tf.float32, shape=[None])

# H(x) = wx + b

#여기서 Variable는 텐서플로가 사용하는 것이다.  즉 텐서플로를 실행시키면 텐서플로가 자동으로 변경시키는 값이다. 
#텐서플로가 학습을 하면서 자동을 변경을 시키는 값을 나타낸다. 
# w와 b는 최초에 랜덤 값을 부여받아 시작한다. 
# 그리고 shape를 결정해준다. [1]은 1차원 array를 뜻한다. 랭크가 1이다. 
W = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = x_train * W + b

#reduce_mean은 어떤 텐서 예를 들면 t = [1,2,3,4,5] 가  주어졌을때 평균을 내주는 것이다. 
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

#cost 펑션까지 주어졌는데 이젠 이걸 최소화하는 것이 필요하다.
#텐서플로에서는 크래디언트디센트를 사용할 수 있다. 

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

#텐서플로에서 train이라는 크래프의 노드를 만들었다. 
train = optimizer.minimize(cost)

#위에까지는 텐서플로의 그래프를 구현해 준것이다.
#이걸 실행 할려면 세션(아마 서버같은 개념일 듯)을 개설 해주고 그 세션에서 돌려야 한다. 
#그래프는 세션 안에서 실행이 된다. 
sess = tf.Session()

#global_variables를 사용했는데 W,b  반드시 초기화를 해줘야 한다. 
sess.run(tf.global_variables_initializer())

#아래에서 sess.run의 결과값들을 리턴 받아 변수들에게 입력하는데 왜 저렇게 해야 에러가 안나는지 모르겠음

for step in range(2001):
    cost_val, w_val, b_val, _ = sess.run([cost,W,b,train], feed_dict={x_train: [1, 2, 3, 4, 5], y_train: [2.1, 3.1, 4.1, 5.1, 6.1]})
    if step % 20 == 0:
        print(step, cost_val, w_val, b_val)
    #    print(step, sess.run(cost), sess.run(W), sess.run(b))


result = sess.run(hypothesis, feed_dict={x_train: [6]})
print("result : ", result)
print("result[0] : ", result[0])

value = json.dumps({"a": float(result[0])})
print(value) 
