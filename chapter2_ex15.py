import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist( (category, word) for category in brown.categories() for word in brown.words(categories = category))

for category in brown.categories():
	fd = [ word for word in set(brown.words(categories = category)) if cfd[category][word] >= 3]

print(fd)
