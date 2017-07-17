import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# + = match 1 or more
# ? = match 0 or 1 repetitions.
# * = match 0 or MORE repetitions
# . = Any character except a new line
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            # print(i)
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #print(tagged)
            #chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkGram = r"""Chunk: {<NNP>+<NN>+}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #chunked.draw()

            #for subtree in chunked.subtrees():
            #    print(subtree)

            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)          #only getting the chunked data

    except Exception as e:
        print(str(e))

process_content()

#---------------------------------------------------------------------------------------------
# <RB.?>* = "0 or more of any tense of adverb," followed by:
#
# <VB.?>* = "0 or more of any tense of verb," followed by:
#
# <NNP>+ = "One or more proper nouns," followed by
#
# <NN>? = "zero or one singular noun."