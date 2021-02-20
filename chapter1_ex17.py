from nltk.book import *

indss = []
indpd = [[] for i in range(list(text9).count('sunset'))]

for i in range(list(text9).count('sunset')):
	if i == 0:
		indss.append(text9.index('sunset'))
	else:
		indss.append(text9[(indss[i-1]+1):].index('sunset') + indss[i-1] + 1)

	#ind[i]:i+1番目のsunsetの添字

	indpd[i].append(indss[i] - text9[indss[i]::-1].index('.'))
	indpd[i].append(text9[(indss[i]+1):].index('.') + indss[i] + 1)

	sentense = ''

	for w in text9[indpd[i][0]+1:indpd[i][1]+1]:
		print(w, end = ' ')

	print()
