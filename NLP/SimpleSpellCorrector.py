#This contains the Simple Spell Corrector Hackerrank problem

import re

def construct_dict(txt):
	vocab = re.findall(r'\w+',txt.lower())
	dictonary = {}
	for word in vocab:
		if word in dictonary:
			dictonary[word] = dictonary[word]+1
		else:
			dictonary[word] = 0
	return dictonary

vocab = construct_dict(open('corpus').read())

def edit_distance_one(word):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	splits = [(word[:i],word[i:]) for i in range(len(word)+1)]
	delete = [L+R[1:] for L,R in splits if R]
	transpose = [L+R[1]+R[0]+R[2:] for L,R in splits if len(R) > 1]
	insert = [L+C+R for L,R in splits for C in alphabet]
	modify = [L+C+R[1:] for L,R in splits for C in alphabet if R]

	return set(insert+delete+transpose+modify)

def known(word_list):	return [w for w in word_list if w in vocab]

def correction(word):
	if word in vocab.keys():
		return word
	candidate_words = known(edit_distance_one(word))
	if len(candidate_words)== 0:
		return word
	word_freq = {w:vocab[w] for w in candidate_words}
	max_word = [w for w in word_freq.keys() if word_freq[w] == max(word_freq.values())]
	max_word.sort()
	return max_word[0]

n = int(raw_input())
for i in range(n):
	str = raw_input()
	print correction(str)