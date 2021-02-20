from nltk.book import *


def hedge(text):

	new_text = text
	num = 0
	for i in range(len(new_text)):
		num += 1
		if num == 3:
			new_text.tokens.insert(i+1, 'like')
			num = -1

	return new_text

ntext = hedge(text8)

