import cursor as cursor
import nltk
import sql as sql
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import sqlite3

# conn = sqlite3.connect('test.db')
# print('opened database successfully')


#cursor = conn.execute("SELECT id, name,age, address, salary from COMPANY where age >=30 and age <=70")

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("query.txt")

file = open("query_result.txt", 'w+')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

dict = {}

def process_content():
    try:
        for i in tokenized[:9]:   #only the initial 5 sentences
            words = nltk.word_tokenize(i)    # words me tokenize kia
            #print(words)
            tagged = nltk.pos_tag(words)
            # un words ko tag kia
            #print(tagged)
            file.write(str(tagged))
            #print(file)
    except Exception as e:
        print(str(e))


process_content()

data = ""
st1 = ""

# file2 = file.read("output1.txt", 'w+')
# file2 = open("output1.txt", 'w+')
# print(file2)
file.seek(0)
with open("query_result.txt", 'r') as f:
    st1 = f.readlines()
#print(len(st1))
st1 = str(st1)
print(len(st1))
# st1 = "[('hello', 'NN'), ('man', 'NN'), ('!', '.')][('my', 'PRP$'), ('name', 'NN'), ('is', 'VBZ'), ('Jeorge', 'NNP'), ('.', '.')][('its', 'PRP$'), ('all', 'DT'), ('good', 'JJ'), ('in', 'IN'), ('here', 'RB'), ('.', '.')][('let', 'VB'), ('us', 'PRP'), ('go', 'VB'), ('for', 'IN'), ('a', 'DT'), ('party', 'NN'), ('.', '.')][('thank', 'NN'), ('you', 'PRP'), ('.', '.')]"
new = ""
left = ""
right = ""
#print(len(st1))
#print(st1.split("), ("))
list_noun = []
list_determiner = []
list_adjective = []
list_preposition = []
list_adverb = []
list_verb = []
list_personal_pronoun = []
list_cardinal_digit = []

file3 = open("query_result.txt", 'w+')

wd = 'nothing'
count = 0
for i in range(0, len(st1)):
    #print(st1[i])
    if st1[i].isalpha():
        #new = ' '.join(st1[i])
        new = "{}{}".format(new, st1[i])
    if st1[i] == "(":
        if i != 3:
            count = count+1
            new = "{}{}".format(new, "+")
    if st1[i] == ",":
        new = "{}{}".format(new, ":")
    if st1[i].isdigit():
        new = "{}{}".format(new, st1[i])
    # elif st1[i].__contains__(","):
    #     new = new + " "
print(new)
    # temp = wd
    # while st1[i] != ',':
    #     wd = wd + st1[i]
    # wd = wd.lower()
    # if wd.equals('NN'):
    #     list.append(wd)
#print(list)
default = 'none'
file3.write(new)
new = new.split("+", count)
for k in range(count):
    #print(new[k])

    pos = new[k].split(":", 2)
    #print(pos[0])
    if pos[1] == 'NN':
        dict['NN'] = pos[0]
        list_noun.append(pos[0])
        #print(list_noun)
    if pos[1] == "DT":
        dict['DT'] = pos[0]
        list_determiner.append(pos[0])
        #print("Determiner:{0}".format(pos[0]))
    if pos[1] == "JJ":
        #if pos[0] != 'null':
        if not dict['JJ']:
            dict['JJ'] = 'Null'
        else:
            dict['JJ'] = pos[0]
        list_adjective.append(pos[0])
        continue
        #print("Adjective:{0}".format(pos[0]))
    if pos[1] == "IN":
        if pos[0] != 'null':
            dict['IN'] = pos[0]
        else:
            dict['IN'] = 'null'
        list_preposition.append(pos[0])
        #print("Preposition:{0}".format(pos[0]))
    if pos[1] == "RB":
        dict['RB'] = pos[0]
        list_adverb.append(pos[0])
        #print("Adverb:{0}".format(pos[0]))
    if pos[1] == "VB":
        dict['VB'] = pos[0]
        list_verb.append(pos[0])
    if pos[1] == "PRP":
        dict['PRP'] = pos[0]
        list_personal_pronoun.append(pos[0])
    if pos[1] == "CD":
        dict['CD'] = pos[0]
        list_cardinal_digit.append(pos[0])

        #print("Verb:{0}".format(pos[0]))
print("noun:")
list_noun = [x.strip(' ') for x in list_noun]
print(list_noun)
print("Determiner:")
print(list_determiner)
print("Adjective:")
print(list_adjective)
print("Preposition:")
print(list_preposition)
print("Adverb:")
print(list_adverb)
print("Verb:")
print(list_verb)
print("Personal Pronoun:")
print(list_personal_pronoun)
print("Cardinal digit:")
print(list_cardinal_digit)
    #right = new[k].split(":")
    #print(left+" -- "+right)

# for j in range(len(new)):
#     newbie = ""
#     new
#     if new[j] != '+':
#         newbie = "{} {}".format(newbie, new[j])
#         #print(newbie)
#     elif new[j] == '+':
#         print(newbie + '\n')




print("dict['Noun']: ", dict['NN'])
print("dict['Determiner']: ", dict['DT'])
#print("dict['Adjective']: ", dict['JJ'])
print("dict['Preposition']: ", dict['IN'])
#print("dict['Adverb']: ", dict['RB'])
print("dict['Verb']: ", dict['VB'])
print("dict['Numbers']: ", dict['CD'])

# conn = sqlite3.connect('test.db')
# print('opened database successfully')

#query = ""
# cursor=db.cursor()
# query = 'SELECT * from COMPANY where age IN (%s)'
# in_p = ', '.join(list(map(lambda x: '%s', list_cardinal_digit)))
# sql = sql % in_p
# cursor.execute(sql, list_cardinal_digit)
#
# #cursor = conn.execute(query)
# for row in cursor:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("AGE = ", row[2])
#    print("ADDRESS = ", row[3])
#    print("SALARY = ", row[4], "\n")
# print("Operation done successfully");
# conn.close()
