import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import sqlite3
import datetime

list_verb, list_noun, list_coordinating_conjunction, list_cardinal_digit = [], [], [], []
list_determiner, list_existential, list_foreign_word, list_preposition = [], [], [], []
list_adjective, list_adjective_comparative, list_adjective_superlative, list_marker = [], [], [], []
list_modal, list_noun_plural, list_proper_noun_singular, list_proper_noun_plural = [], [], [], []
list_predeterminer, list_possessive_ending, list_personal_pronoun, list_possessive_pronoun = [], [], [], []
list_adverb, list_adverb_comparative, list_adverb_superlative, list_particle = [], [], [], []
list_to, list_interjection, list_verb_past, list_verb_gerund_present_participle = [], [], [], []
list_verb_past_participle, list_verb_singular_present, list_verb_3rd_person_singular_present, list_wh_determiner = [], [], [], []
list_wh_pronoun, list_possessive_wh_pronoun, list_wh_adverb = [], [], []

count = 0

print("Jarvis at your service sir!")
query = input("How may I help you?\n")
stopwords = set(stopwords.words("english"))
#query = query.lower()
words = word_tokenize(query)
print(words)
tagged_query = pos_tag(words)
# print(tagged_query)
def process_content():
    try:
        for i in words:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<VB.>+<PDT.?>*<DT.?>*<NNS.?>*<VBG.?>+<NN.>+<IN.>+<CD.>+<TO.?>*<CC.?>+<CD>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()





for i, j in tagged_query:
    # print(i, j)
    if j == "VB":
        list_verb.append(i)
        print(list_verb)
    elif j == "NN":
        list_noun.append(i)
    elif j == "CC":
        list_coordinating_conjunction.append(i)
    elif j == "CD":
        list_cardinal_digit.append(i)
    elif j == "DT":
        list_determiner.append(i)
    elif j == "EX":
        list_existential.append(i)
    elif j == "FW":
        list_foreign_word.append(i)
    elif j == "IN":
        list_preposition.append(i)
    elif j == "JJ":
        list_adjective.append(i)
    elif j == "JJR":
        list_adjective_comparative.append(i)
    elif j == "JJS":
        list_adjective_superlative.append(i)
    elif j == "LS":
        list_marker.append(i)
    elif j == "MD":
        list_modal.append(i)
    elif j == "NNS":
        list_noun_plural.append(i)
    elif j == "NNP":
        list_proper_noun_singular.append(i)
    elif j == "NNPS":
        list_proper_noun_plural.append(i)
    elif j == "PDT":
        list_predeterminer.append(i)
    elif j == "POS":
        list_possessive_ending.append(i)
    elif j == "PRP":
        list_personal_pronoun.append(i)
    elif j == "PRP$":
        list_possessive_pronoun.append(i)
    elif j == "RB":
        list_adverb.append(i)
    elif j == "RBR":
        list_adverb_comparative.append(i)
    elif j == "RBS":
        list_adverb_superlative.append(i)
    elif j == "RP":
        list_particle.append(i)
    elif j == "TO":
        list_to.append(i)
    elif j == "UH":
        list_interjection.append(i)
    elif j == "VBD":
        list_verb_past.append(i)
    elif j == "VBG":
        list_verb_gerund_present_participle.append(i)
    elif j == "VBN":
        list_verb_past_participle.append(i)
    elif j == "VBP":
        list_verb_singular_present.append(i)
    elif j == "VBZ":
        list_verb_3rd_person_singular_present.append(i)
    elif j == "WDT":
        list_wh_determiner.append(i)
    elif j == "WP":
        list_wh_pronoun.append(i)
    elif j == "WP$":
        list_possessive_wh_pronoun.append(i)
    elif j == "WRB":
        list_wh_adverb.append(i)
    else:
        print("Didn't understand the word '" + i + "' please train me! ")

now = datetime.datetime.now()


def create_file():
    with open("C:/Users/shubu/PycharmProjects/nltk_project/files/" + now.strftime('%d-%b-%Y %H-%M %p') + ".txt",
              "w+")as output_file:
        output_file.write("q) " + query)  # Write empty string


create_file()

# PRINTING PROCESS STARTS :

# print("List of nouns:")
# print(list_noun)
# print("List of Verbs:")
# print(list_verb)
# print("Coordinating Conjunction:")
# print(list_coordinating_conjunction)
# print("Cardinal digits:")
# print(list_cardinal_digit)
# print("Determiner:")
# print(list_determiner)
# print("Existential:")
# print(list_existential)
# print("Foreign Word:")
# print(list_foreign_word)
# print("Preposition:")
# print(list_preposition)
# print("adjective:")
# print(list_adjective)
# print("adjective comparative:")
# print(list_adverb_comparative)
# print("adjective superlative:")
# print(list_adjective_superlative)
# print("list marker:")
# print(list_marker)
# print("Modal:")
# print(list_modal)
# print("Plural noun:")
# print(list_noun_plural)
# print("Singular Proper noun:")
# print(list_proper_noun_singular)
# print("Plural Proper noun:")
# print(list_proper_noun_plural)
# print("Predeterminer:")
# print(list_predeterminer)
# print("Possessive Ending:")
# print(list_possessive_ending)
# print("personal pronoun:")
# print(list_personal_pronoun)
# print("possessive pronoun:")
# print(list_possessive_pronoun)
# print("Adverb:")
# print(list_adverb)
# print("adverb comparative:")
# print(list_adverb_comparative)
# print("adverb superlative:")
# print(list_adverb_superlative)
# print("particle:")
# print(list_particle)
# print("To:")
# print(list_to)
# print("Interjection:")
# print(list_interjection)
# print("Past tense Verb:")
# print(list_verb_past)
# print("Verb Gerund/Present Participle:")
# print(list_verb_gerund_present_participle)
# print("Verb Past Participle:")
# print(list_verb_past_participle)
# print("Singular Present Verb:")
# print(list_verb_singular_present)
# print("3rd person singular present Verb:")
# print(list_verb_3rd_person_singular_present)
# print("WH-Determiner:")
# print(list_wh_determiner)
# print("WH-Pronoun:")
# print(list_wh_pronoun)
# print("Possessive WH-Pronoun")
# print(list_possessive_wh_pronoun)
# print("WH-Adverb")
# print(list_wh_adverb)

# -----------------------------------------------------------------------------------------------------------------------------------

# dict_verb, dict_noun, dict_coordinating_conjunction, dict_cardinal_digit = {}, {}, {}, {}
# dict_determiner, dict_existential, dict_foreign_word, dict_preposition = {}, {}, {}, {}
# dict_adjective, dict_adjective_comparative, dict_adjective_superlative, dict_marker = {}, {}, {}, {}
# dict_modal, dict_noun_plural, dict_proper_noun_singular, dict_proper_noun_plural = {}, {}, {}, {}
# dict_predeterminer, dict_possessive_ending, dict_personal_pronoun, dict_possessive_pronoun = {}, {}, {}, {}
# dict_adverb, dict_adverb_comparative, dict_adverb_superlative, dict_particle = {}, {}, {}, {}
# dict_to, dict_interjection, dict_verb_past, dict_verb_gerund_present_participle = {}, {}, {}, {}
# dict_verb_past_participle, dict_verb_singular_present, dict_verb_3rd_person_singular_present, dict_wh_determiner = {}, {}, {}, {}
# dict_wh_pronoun, dict_possessive_wh_pronoun, dict_wh_adverb = {}, {}, {}

# ------------------------------------------------------------------------------------------------------------------------------------

dict = {"noun": list_noun, "verb": list_verb, "coordinating_conjunction": list_coordinating_conjunction,
        "cardinal_digit": list_cardinal_digit, "determiner": list_determiner, "existential": list_existential,
        "foreign_word": list_foreign_word, "preposition": list_preposition, "adjective": list_adjective,
        "adjective_comparative": list_adjective_comparative, "adjective_superlative": list_adverb_superlative,
        "marker": list_marker, "modal": list_modal, "noun_plural": list_noun_plural,
        "proper_noun_singular": list_proper_noun_singular, "proper_noun_plural": list_proper_noun_plural,
        "predeterminer": list_predeterminer, "possessive_ending": list_possessive_ending,
        "personal_pronoun": list_personal_pronoun, "possessive_pronoun": list_possessive_pronoun, "adverb": list_adverb,
        "adverb_comparative": list_adverb_comparative, "adverb_superlative": list_adverb_superlative,
        "particle": list_particle, "to": list_to, "interjection": list_interjection, "verb_past": list_verb_past,
        "verb_gerund_present_participle": list_verb_gerund_present_participle,
        "verb_past_participle": list_verb_past_participle, "verb_singular_present": list_verb_singular_present,
        "verb_3rd_person_singular_present": list_verb_3rd_person_singular_present, "wh_determiner": list_wh_determiner,
        "wh_pronoun": list_wh_pronoun, "possessive_wh_pronoun": list_possessive_wh_pronoun, "wh_adverb": list_wh_adverb}
print("Dictionary of the parts of speech:")
print(dict)

conn = sqlite3.connect('test.db')
print("Opened database successfully")

str1 = ""
ouput_file = open("C:/Users/shubu/PycharmProjects/nltk_project/files/" + now.strftime('%d-%b-%Y %H-%M %p') + ".txt",
                  "a+")

for i in list_preposition:
    if dict['preposition'][count] == "between" or "from" or dict['noun'][count] == "range":
        cursor = conn.execute(
            "SELECT * from COMPANY where " + dict['noun'][count - 1] + " > " + dict['cardinal_digit'][0] + " and " +
            dict['noun'][count - 1] + " < " + dict['cardinal_digit'][1])
        for row in cursor:
            print(row)
            str1 = row
            ouput_file.write("\n Solution: " + str(str1))
    count = count + 1


print("Operation done successfully");
conn.close()
