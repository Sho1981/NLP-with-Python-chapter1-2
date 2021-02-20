import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist( (category, word) for category in brown.categories() for word in brown.words(categories = category))

target_list = []

while True:
	tarword = input('Input one word (if it is all, input "Enter Key") -> ')

	if tarword == '':
		break
	else:
		target_list.append(tarword)

cfd.tabulate(conditions = brown.categories(), samples = target_list)
