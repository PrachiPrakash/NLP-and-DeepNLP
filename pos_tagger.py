import tensorflow as tf 
import numpy as np 
import re

batch_size = 100
state_size = 10

content = open('./output.txt').read().strip('\n')
word_pos_pairs = re.findall(r'([\w.\'\"]+)/([\w.-]+)',content)
pos_list = list(set([pos for word,pos in word_pos_pairs]))
word_list = list(set([word.strip('"\'').lower() for word,pos in word_pos_pairs]))

word_index = {word_list[i]:i for i in xrange(len(word_list))}
index_word = {i:word_list[i] for i in xrange(len(word_list))}
pos_index = {pos_list[i]:i for i in xrange(len(pos_list))}
index_pos = {i:pos_list[i] for i in xrange(len(pos_list))}

print 'Number of words in vocab',len(word_list)
print 'Number of tag types',len(pos_list)
print 'Index creation done'

def get_train_data(sentences):
	sentences = [s+' ./.' for s in sentences]
	

	x = []
	y = []

	#for each sentence find the numbers
	for s in sentences:
		pairs = re.findall(r'([\w.\'\"]+)/([\w.-]+)',s)
		we = [word_index[w.strip('"\'').lower()] for w,p in pairs]
		pe = [pos_index[p] for w,p in pairs]
		x.append(we)
		y.append(pe)

	return x,y

sentences = content.split('./.')
x,y = get_train_data(sentences)

#find the sequence length of each input and the max sequence length
len_vec = np.array([len(x_i) for x_i in x],dtype=np.int32)
max_len = max(len_vec)
print max_len
input_mat = np.empty((0,max_len), dtype=np.int32)
output_mat = np.empty((0,max_len), dtype=np.int32)

#padding the data
for i in xrange(len(x)):
	x_temp = np.pad(x[i],(0,max_len-len(x[i])),mode='constant',constant_values=0)
	y_temp = np.pad(y[i],(0,max_len-len(x[i])),mode='constant', constant_values=0)
	input_mat = np.append(input_mat,np.reshape(x_temp,(1,max_len)),axis=0)
	output_mat = np.append(output_mat,np.reshape(y_temp,(1,max_len)),axis=0)

input_mat = np.reshape(input_mat,(len(sentences),max_len))
output_mat = np.reshape(output_mat,(len(sentences),max_len))
len_vec = np.reshape(len_vec, len(sentences))
print 'preparing data done'
#for performance inprovement
del x
del y

#here comes rnn dragon
inp = tf.placeholder(tf.int32, [batch_size,max_len])
X = tf.one_hot(inp,len(word_index))
seq_size = tf.placeholder(tf.int32,[batch_size])
init_states = tf.zeros([batch_size,state_size])
Y = tf.placeholder(tf.int32,[batch_size,max_len])

rnn = tf.nn.rnn_cell.GRUCell(state_size)
rnn_outputs,final_state = tf.nn.dynamic_rnn(rnn, X, sequence_length=seq_size,
                                                 initial_state=init_states)

with tf.variable_scope('softmax'):
    W = tf.get_variable('W', [state_size, len(pos_index)])
    b = tf.get_variable('b', [len(pos_index)], initializer=tf.constant_initializer(0.0))
logits = tf.reshape(
            tf.matmul(tf.reshape(rnn_outputs, [-1, state_size]), W) + b,
            [batch_size, max_len, len(pos_index)])

predictions = tf.nn.softmax(logits)

losses = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=Y, logits=logits)
total_loss = tf.reduce_mean(losses)
train_step = tf.train.AdagradOptimizer(0.1).minimize(total_loss)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for _ in range(30):
		random_index = np.random.choice(len(sentences),batch_size)
		x_batch,y_batch,seq_batch = input_mat[random_index],output_mat[random_index],len_vec[random_index]
		z,loss = sess.run([train_step,total_loss],feed_dict={inp:x_batch,Y:y_batch,seq_size:seq_batch})
		print loss

