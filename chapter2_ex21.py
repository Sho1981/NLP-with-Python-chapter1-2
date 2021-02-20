import nltk
from nltk.book import *

'''
カーネギーメロン大学の発音辞書を利用してテキストに含まれる音節の数を推定する
'''

#各単語の平均音節数を取得
entries = [[word, pron] for word, pron in nltk.corpus.cmudict.entries() if word.isalnum()]
entries = sorted(entries, key=lambda x: x[0])

word_pre = ''
word_num = 0
pron_ave = []

for word, pron in entries:
	if word != word_pre:
		if word_num > 0:
			pron_ave[word_num -1][1] /= same_num
		pron_ave.append([word, len(pron)])
		word_pre = word
		word_num += 1
		same_num = 1

	elif word == word_pre:
		pron_ave[word_num - 1][1] += len(pron)
		word_pre = word
		same_num += 1

	else:
		print('error')


#アルファベットの頭文字の索引
#whead_list = [頭文字, 開始index, 終了index]

whead_list = [[chr(i),0,0] for i in range(97, 123)]

index_pre = -1
for i, ch in enumerate(whead_list):
	whead_list[i][1] = index_pre + 1
	for j, pa in enumerate(pron_ave[(index_pre+1):]):
		if pa[0][0] == ch[0]:
			continue
		else:
			index_pre = index_pre + j + 1
			whead_list[i][2] = index_pre
			break
whead_list[i][2] = index_pre + j + 1


text_pron_total = 0

for w in list(text8):
	index = [0, 0]
	flug = False
	if not(w.isalnum()):
		continue
	for whead in whead_list:
		if w[0].lower() in whead:
			index = [whead[1], whead[2]]
			break
	for pa in pron_ave[index[0]:index[1]]:
		if w.lower() == pa[0]:
			text_pron_total += pa[1]
			flug = True
			break
	if flug == False:
		text_pron_total += len(w) #もし発音辞書になかった場合、文字列の長さを便宜的に発音の長さとする

print(text_pron_total)
