import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]  # documents ko categorize kia

random.shuffle(documents)  # shuffle kia

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())  # saare words ko extract kia

all_words = nltk.FreqDist(all_words)  # in the form of keys and values

# print(all_words.keys())

word_features = list(all_words.keys())[:3000]  # getting top 3000 words


# print(word_features)

def find_features(document):    # hame ek document ko lena hai aur usme check karna jo top 3000 me honge unko show
    # karna hai with categories.
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

# Naive Bayes algorithm

featuresets = [(find_features(rev), category) for (rev, category) in documents]

# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]

# classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)

# save_classifier = open("naivebayes.pickle","wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, testing_set))

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, testing_set))