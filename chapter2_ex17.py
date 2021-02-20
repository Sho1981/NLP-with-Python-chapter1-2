import nltk
from nltk.book import *
from nltk.corpus import stopwords

def top50(words):
	cfd = nltk.FreqDist( word.lower() for word in words)

	stopword = stopwords.words('english')

	fd = [(word, cfd[word]) for word in set([w.lower() for w in words])
                          if (word.isalpha()) & (word not in stopword)]

	fd = sorted(fd, reverse=True, key=lambda x: x[1])
	print(fd[:49])


top50(list(text1))
