import nltk
import random

import pickle
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB , GaussianNB , BernoulliNB
from sklearn.linear_model import LogisticRegression , SGDClassifier

from sklearn.svm import SVC, LinearSVC , NuSVC

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize



class VoteClassifier(ClassifierI):

    def __init__(self,*classifiers):
        self._classifiers = classifiers


    def classify(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

documents = []
short_pos = open('positive.txt','r').read()
short_neg = open('negative.txt','r').read()

##pos = short_pos.readlines()
##neg = short_neg.readlines()

for r in short_pos.split('\n'):
    documents.append((r,"pos"))

for r in short_neg.split('\n'):
    documents.append((r,"neg"))

all_words = []

save_classifier = open("documents.pickle","wb")
pickle.dump(documents,save_classifier)
save_classifier.close()



short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
    all_words.append(w.lower())

for w in short_neg_words:
    all_words.append(w.lower())
           

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:2500]

save_word_features = open("word_features.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

##print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
featuresets = [(find_features(rev),category) for (rev,category) in documents]

save_word_features = open("featuresets.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()



random.shuffle(featuresets)

training_set = featuresets[:2000]
testing_set = featuresets[2000:]

classifier = nltk.NaiveBayesClassifier.train(training_set)


save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier,save_classifier)
save_classifier.close()

print("original naive bayes accuracy : ", (nltk.classify.accuracy(classifier,testing_set))*100)
##classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB accuracy : ", (nltk.classify.accuracy(MNB_classifier,testing_set))*100)

save_classifier = open("MNB.pickle","wb")
pickle.dump(MNB_classifier,save_classifier)
save_classifier.close()

##GuassianNB_classifier = SklearnClassifier(GaussianNB())
##GuassianNB_classifier.train(training_set)
##print("Guassian accuracy : ", (nltk.classify.accuracy(GuassianNB,testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB accuracy : ", (nltk.classify.accuracy(BernoulliNB_classifier,testing_set))*100)


save_classifier = open("BernoulliNB.pickle","wb")
pickle.dump(BernoulliNB_classifier,save_classifier)
save_classifier.close()



##LogisticRegression , SGDClassifier
##SVC, LinearSVC , NuSVC
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression accuracy : ", (nltk.classify.accuracy(LogisticRegression_classifier,testing_set))*100)


save_classifier = open("LogisticRegression.pickle","wb")
pickle.dump(LogisticRegression_classifier,save_classifier)
save_classifier.close()



SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier accuracy : ", (nltk.classify.accuracy(SGDClassifier_classifier,testing_set))*100)


save_classifier = open("SGDClassifier.pickle","wb")
pickle.dump(SGDClassifier_classifier,save_classifier)
save_classifier.close()




LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC accuracy : ", (nltk.classify.accuracy(LinearSVC_classifier,testing_set))*100)

save_classifier = open("LinearSVC.pickle","wb")
pickle.dump(LinearSVC_classifier,save_classifier)
save_classifier.close()



NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC accuracy : ", (nltk.classify.accuracy(NuSVC_classifier,testing_set))*100)


save_classifier = open("NuSVC.pickle","wb")
pickle.dump(NuSVC_classifier,save_classifier)
save_classifier.close()


voted_classifier = VoteClassifier(classifier,MNB_classifier,BernoulliNB_classifier,NuSVC_classifier,LinearSVC_classifier,SGDClassifier_classifier,LogisticRegression_classifier)

print("voted : ",(nltk.classify.accuracy(voted_classifier,training_set))*100)

print("Classification : ", voted_classifier.classify(testing_set[0][0]),"confidence : " ,voted_classifier.confidence(testing_set[0][0])*100)
print("Classification : ", voted_classifier.classify(testing_set[1][0]),"confidence : " ,voted_classifier.confidence(testing_set[1][0])*100)

print("Classification : ", voted_classifier.classify(testing_set[2][0]),"confidence : " ,voted_classifier.confidence(testing_set[2][0])*100)

print("Classification : ", voted_classifier.classify(testing_set[3][0]),"confidence : " ,voted_classifier.confidence(testing_set[3][0])*100)
print("Classification : ", voted_classifier.classify(testing_set[4][0]),"confidence : " ,voted_classifier.confidence(testing_set[4][0])*100)

