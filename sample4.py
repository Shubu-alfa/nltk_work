from nltk.tokenize import word_tokenize
#from ntlk.tag import parts_of_speech_tagging
from nltk.corpus import stopwords
import nltk

fname = input("Enter the file name:\n")
file = open(fname, 'r')
desire = input("\nWhat do you want to extract?\n")
stopwords = set(stopwords.words("english"))
while desire.lower() != 'exit':
    if desire.lower() == 'noun':
        ext = 'NN'
    elif desire.lower() == 'verb':
        ext = 'VB'
p = file.read()
words = word_tokenize(p)

filtered_sent = []

for w in words:
    if w not in stopwords:
        filtered_sent.append(w)

tagged_sent = nltk.pos_tag(words)
#print(tagged_sent)
propernouns = [word for word,pos in tagged_sent if pos == ext]

print(propernouns)