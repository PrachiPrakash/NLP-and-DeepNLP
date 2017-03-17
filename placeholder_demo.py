import tensorflow as tf 

def main():
	x = tf.placeholder("float",3)
	y = 2 * x
	

	with tf.Session() as session:
		print session.run(y,feed_dict={x:[1,2,3]})


main()