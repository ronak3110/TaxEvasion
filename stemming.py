from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

text = "barnik barniking ronak ronaked"

word = ["python","pythoner","pythoning","pythoned","pythonly"]

##for w in word:
##    print(ps.stem(w))
    
words = word_tokenize(text)
print(words)
for w in words:
    print(ps.stem(w))
