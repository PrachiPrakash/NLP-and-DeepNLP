#This is a program will demonstrate the basic lanhuage modelling task using markov chain without any smoothinh
#@author Prachi Prakash

import re

def get_unigram_bigram(txt):
	sentences = txt.split('\n')
	appended_sentences = ['<s> '+s+' </s>' for s in sentences]

	unigrams = {}
	bigrams = {}

	unigrams['<s>'] = 0
	unigrams['</s>'] = 0

	for s in appended_sentences:

		words = s.split(' ')
		unigrams[words[0]] = unigrams[words[0]] + 1

		for i in range(1,len(words)):

			if words[i] in unigrams:
				unigrams[words[i]] = unigrams[words[i]] + 1
			else:
				unigrams[words[i]] = 1

			bigram = words[i-1]+' '+words[i]

			if bigram in bigrams:
				bigrams[bigram] = bigrams[bigram] + 1
			else:
				bigrams[bigram] = 1

	return unigrams, bigrams



