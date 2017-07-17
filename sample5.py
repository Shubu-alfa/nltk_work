import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("sample_test.txt")

file = open("output1.txt", 'w+')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized[:5]:   #only the initial 5 sentences
            words = nltk.word_tokenize(i)    # words me tokenize kia
            #print(words)
            tagged = nltk.pos_tag(words)
            # un words ko tag kia
            print(tagged)
            file.write(str(tagged))
            #print(file)
    except Exception as e:
        print(str(e))


process_content()

# file2 = file.read("output1.txt", 'w+')
# file2 = open("output1.txt", 'w+')
# print(file2)

