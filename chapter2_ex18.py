import nltk
from nltk.book import *
from nltk.corpus import stopwords

def top50bigram(words):
	bilist = list(bigrams([w.lower() for w in words]))
	cfd = nltk.FreqDist( bigram for bigram in bilist)

	stoplist = stopwords.words('english')

	fd = [(bigram, cfd[bigram]) for bigram in set(bilist)
                              if [(w.isalpha()) & (w not in stoplist)
                              for w in bigram] == [True, True]]

	fd = sorted(fd, reverse=True, key=lambda x: x[1])
	print(fd[:49])

top50bigram(text1)
