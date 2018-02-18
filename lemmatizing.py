from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
lemmatizer = WordNetLemmatizer()
stm = PorterStemmer()
import nltk
print(nltk.__file__)
print (lemmatizer.lemmatize("bating"))
print(stm.stem("bating"))
