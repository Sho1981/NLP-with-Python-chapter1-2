import nltk
from nltk.corpus import gutenberg

cfd = nltk.ConditionalFreqDist( (genre, words)
											for genre in gutenberg.fileids()
                      for words in gutenberg.words(genre))

genres = gutenberg.fileids()

i=0

for genre in gutenberg.fileids():
	fd = [ (word, cfd[genre][word])
	                      for word in set(gutenberg.words(genre))
	                      if word.isalpha()]
	fd = sorted(fd, reverse=True, key=lambda x: x[1])

	num = 0
	total = len([w for w in gutenberg.words(genre) if w.isalpha()])

	for i, w in enumerate(fd):
		num += w[1]
		if num / total > 0.333:
			break

	print(genre, '1/3 over:', i)
