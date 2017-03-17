#This example shows build a comp[utation graph and fetching the result without feeding
import tensorflow as tf 

def main():
	input1 = tf.constant(3.0,name='i1')
	input2 = tf.constant(2.0, name='i2')
	interm = tf.add(input1, input2)
	mul = tf.mul(input1,interm)

	with tf.Session() as sess:
		result = sess.run([mul,interm])
		print result 

main()