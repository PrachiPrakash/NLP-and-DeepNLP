import tensorflow as tf 

def main():
	state = tf.Variable(0, name = 'counter')
	new_value = tf.add(state, tf.constant(1))
	update = tf.assign(state, new_value)

	with tf.Session() as sess:
		sess.run(tf.initialize_all_variables())
		for _ in range(3):
			print sess.run(update)


main()