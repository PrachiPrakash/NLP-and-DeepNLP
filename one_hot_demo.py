import tensorflow as tf 

def main():
	x = tf.placeholder(tf.int32,[5],name='X')
	x_one_hot = tf.one_hot(x,2)

	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		print sess.run(x_one_hot,feed_dict={x:[0,0,1,0,1]})

main()