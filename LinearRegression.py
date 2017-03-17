#This program will show how to implement a linear regression using tensorflow

import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt

x_data = np.random.normal(0, 1,1000)
x_data = np.reshape(x_data, (1000,1))
y_data = np.random.normal(0,1,1000)
y_data = np.reshape(y_data, (1000,1))

X = tf.placeholder(tf.float32,shape=(100,1))
Y = tf.placeholder(tf.float32,shape=(100,1))

with tf.variable_scope("linear-regression"):
	W = tf.get_variable("weights",(1,1))
	b = tf.get_variable("bias",(1,))
	prediction = tf.matmul(X,W)+b
	loss = tf.reduce_sum(((Y-prediction)**2)/100.0)

optimizer = tf.train.AdamOptimizer().minimize(loss)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for _ in range(10000):
		random_index = np.random.choice(1000,100)
		x_batch,y_batch = x_data[random_index],y_data[random_index]
		z, parameter,bias = sess.run([optimizer,W,b],feed_dict={X:x_batch,Y:y_batch})
	

parameter = np.reshape(parameter,(1,1))
bias = np.reshape(bias,(1,1))
y_predict = x_data*parameter + bias

print parameter,bias
print "Parameter is",len(y_predict)

plt.scatter(x_data,y_data)
plt.plot(x_data,y_predict)

plt.show()

