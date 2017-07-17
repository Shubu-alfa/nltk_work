from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import random
import sqlite3

##tagger_path = '/path/to/nltk_data/taggers/maxent_treebank_pos_tagger/english.pickle'
##default_tagger = nltk.data.load(tagger_path)
##model = {'select': 'VB'}
##tagger = nltk.tag.UnigramTagger(model=model, backoff=default_tagger)


print("Hello! I'm Dexter")
query = input("How may I help you?\n")
stopwords = set(stopwords.words("english"))  # initialize stopwords
query = query.lower()  # change query to lowercase
# print(query)
words = word_tokenize(query)  # tokenize the query terms
#print(words)
filtered_query = []

# for w in words:  # filter stopwords
#     if w not in stopwords:
#         filtered_query.append(w)
# print(filtered_query)

tagged_query = pos_tag(words)
print(tagged_query)

# # Sentences we'll respond with if the user greeted us
# GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "yo")
#
# GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", ]

#
# def check_for_greeting(sentence):
#     """If any of the words in the user's input was a greeting, return a greeting response"""
#     for word in sentence:
#         if word.lower() in GREETING_KEYWORDS:
#             return random.choice(GREETING_RESPONSES)
#         else:
#             return "I Dont know"


conn = sqlite3.connect('project.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tagged_terms(term TEXT, tag TEXT)")


def data_entry(word, tag):
    c.execute("INSERT INTO tagged_terms(term,tag) VALUES (?,?)",
              (word, tag))

    conn.commit()


create_table()



# print(check_for_greeting(tagged_query))

for i, j in query:
    data_entry(i, j)

c.close()
conn.close()

print("Saved in database")
