from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

print(stop_words)

word_tokens = word_tokenize(example_sent) #extracts all the words.

#filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)   #filtering and getting only those words which are not in the stopwords list.

print(word_tokens)
print(filtered_sentence)