import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]         # Document wise categorize karre

random.shuffle(documents)

print(documents[2])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])


# -------------------------------------------------------------------------------------------- Basically,
# in plain English, the above code is translated to: In each category (we have pos or neg), take all of the file IDs
# (each review has its own ID), then store the word_tokenized version (a list of words) for the file ID, followed by
# the positive or negative label in one big list.
#
# Next, we use random to shuffle our documents. This is because we're going to be training and testing. If we left
# them in order, ' 'chances are we'd train on all of the negatives, some positives, and then test only against
# positives. We don't want that, so we shuffle the data.