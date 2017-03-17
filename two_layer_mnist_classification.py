#this one of the easiest neural network for clasiification of hand-written digits

import numpy as np 
import tensorflow as tf
import collections 


def prepare_data(content):
	raw_data = content.split('\n')
	raw_data = raw_data[1:]
	raw_data = [[row.split(',')[0],row.split(',')[1:]] for row in raw_data if len(row.split(',')) == 785]
	
	feature_matrix = [map(float,X) for Y,X in raw_data if len(X)==784]


	output = [float(Y) for Y,X in raw_data]
	x_data = np.array(feature_matrix,dtype=np.float32)
	x_data = np.reshape(x_data, (len(x_data),784))

	y_data = np.zeros((len(raw_data), 10),dtype=np.float32)

	for i in range(len(output)):
		y_data[i,output[i]] = 1

	return x_data,y_data

def train(x_data,y_data,epochs = 1000):
	x = tf.placeholder(tf.float32, [None,784])
	y_ = tf.placeholder(tf.float32,[None,10])

	W = tf.Variable(tf.zeros([784,10]),name='W')
	b = tf.Variable(tf.zeros([10]), name='w')

	y = tf.nn.softmax(tf.matmul(x,W)+b)
	loss = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))

	optimizer = tf.train.GradientDescentOptimizer(0.000005).minimize(loss)

	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		for _ in range(1500):
			index = np.random.choice(len(x_data),100)
			x_batch, y_batch = x_data[index],y_data[index]
			z,l,p,bias = sess.run([optimizer,loss,W,b],feed_dict = {x:x_batch, y_:y_batch})
			print l

	return p,bias

def predict(data,weight,bias):
	y = data * weight + b

	return np.argmax(y)

x_data, y_data = prepare_data(open('mnist_train.csv').read())
x_test, y_test = prepare_data(open('mnist_test.csv').read())

print len(x_data)
weight,bias = train(x_data,y_data)
print type(weight),type(bias)
print len(x_test)
y_obtained = [predict(x_test[i],weight,bias) == y_test[i]  for i in range(len(x_test))]

count = collections.Counter(y_obtained)
print count.keys()




