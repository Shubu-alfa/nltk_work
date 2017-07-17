import nltk
from nltk.corpus import wordnet
print(nltk.__file__)

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    #print(syn.definition())
    for l in syn.lemmas():
        #print(l.name())
        # print(l.definition())        AttributeError: 'Lemma' object has no attribute 'definition'
        synonyms.append(l.name())
        if l.antonyms():
            print(l.antonyms()[0].name())





















import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("sample_test.txt")

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

    except Exception as e:
        print(str(e))


process_content()


