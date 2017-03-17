import tensorflow as tf

def main():
	x = tf.constant([1,2,3,4], name = 'x')
	y = tf.Variable(x+5, name = 'y')

	model = tf.initialize_all_variables()

	with tf.Session() as sess:
		sess.run(model)
		print sess.run(y)

main()
