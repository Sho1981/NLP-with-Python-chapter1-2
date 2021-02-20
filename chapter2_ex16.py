import nltk
from nltk.corpus import brown as bn
import pprint

score_div = [(cat,
							len(bn.words(categories = cat)),
							len(set(bn.words(categories = cat))),
							len(bn.words(categories = cat))/len(set(bn.words(categories = cat))))
							for cat in bn.categories()]

score_div = sorted(score_div, reverse=True, key=lambda x: x[3])

pprint.pprint(score_div)

