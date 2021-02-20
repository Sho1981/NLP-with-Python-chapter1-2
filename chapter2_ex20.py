import nltk
from nltk.corpus import brown

def word_freq(word, category):

	fd = nltk.FreqDist(w for w in brown.words(categories = category))
	return fd[word]


print(word_freq('can', 'news'))

