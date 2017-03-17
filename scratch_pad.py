import numpy as np 
import tensorflow as tf 


arr = [[1,2],[1,2,0]]
final = np.empty((0,5))

for vec in arr:
	temp = np.pad(vec, (0,5-len(vec)), mode='constant', constant_values=0)
	print temp
	final = np.append(final,np.reshape(temp,(1,5)),axis = 0)
print final

input_ = tf.placeholder(tf.int32,[2,None],name='input')
oneHot = tf.one_hot(input_,6)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print sess.run(oneHot, feed_dict = {input_:[[0,1,2],[3,4,5]]})