import nltk
#from nltk.book import *

#Global Values

GEN_LENGTH = 15
HIGH_FREQ_WORDS = 500

START_WORD = 'living'

def generate_model(cfdist, word, num):

	for i in range(num):
		print(word, end = ' ')
		word = cfdist[word].max()

def high_freq_word(text, num): # retuen type=list

	fd = nltk.FreqDist(text)
	return list(fd)[:num]


text = nltk.corpus.genesis.words('english-kjv.txt')
hwords = high_freq_word(text, HIGH_FREQ_WORDS)

bigrams = list(nltk.bigrams(text))

cfd = nltk.ConditionalFreqDist( [bg for bg in bigrams if (bg[0] in hwords) & (bg[1] in hwords)] )

#cfd = nltk.ConditionalFreqDist(bigrams)

generate_model(cfd, START_WORD, GEN_LENGTH)

