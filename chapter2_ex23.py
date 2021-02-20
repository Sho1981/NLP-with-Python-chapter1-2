import nltk
#from nltk.book import *

import numpy as np
import matplotlib.pyplot as plt
import random


def zipfs(text):

	fd = nltk.FreqDist(text)

	rank = []
	freq = []

	num = 0

	for i, word in enumerate(fd):
		if word.isalpha():
			rank.append(num+1)
			freq.append(fd[word])
			num += 1
	
	plt.plot(rank[0:100], freq[0:100])
#	plt.plot(rank, freq)
	ax = plt.gca()
	ax.set_yscale('log')
	plt.grid(which="both")
	plt.show()


#main

random_str = ''

for i in range(1000000):
	random_str += random.choice('abcdefg hijklmn opqrstu vwxyz ')

random_list = random_str.split()

new_text = nltk.Text(random_list)

zipfs(new_text)

