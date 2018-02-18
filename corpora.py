from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
sample = gutenberg.raw("bible-kjv.txt")


tokens = sent_tokenize(sample)

print(tokens[5:50])
