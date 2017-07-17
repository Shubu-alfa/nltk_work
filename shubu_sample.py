from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import sqlite3

query = input("How may I help you?\n")
stopwords = set(stopwords.words("english"))  # initialize stopwords
query = query.lower()  # change query to lowercase
# print(query)
words = word_tokenize(query)  # tokenize the query terms
# print(words)
filtered_query = []

for w in words:  # filter stopwords
    if w not in stopwords:
        filtered_query.append(w)
# print(filtered_query)

tagged_query = pos_tag(filtered_query)
# print(tagged_query)

conn = sqlite3.connect('project.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tagged_terms(term TEXT, tag TEXT)")


def data_entry(word, tag):
    c.execute("INSERT INTO tagged_terms(term,tag) VALUES (?,?)",
              (word, tag))

    conn.commit()
create_table()
for i, j in tagged_query:
    data_entry(i, j)

c.close()
conn.close()

print("Saved in database")