import nltk
from nltk.corpus import cmudict

word_pre = ''
pron_pre = []
flug = False
num = 0
prondif = []

for word, pron in cmudict.entries():
	if (word == word_pre) and (flug == False):
		num += 1
		print(word, ':', pron_pre, pron, end = '')
		prondif.append([word_pre, pron_pre])
		prondif[num - 1].append(pron)
		flug = True
		continue
	elif (word == word_pre) and (flug == True):
		print(pron, end = '')
		prondif[num - 1].append(pron)
		continue
	elif (word != word_pre) and (flug == True):
		print()
		word_pre = word
		pron_pre = pron
		flug = False
	else:
		flug = False
		word_pre = word
		pron_pre = pron

print('num =', num)
