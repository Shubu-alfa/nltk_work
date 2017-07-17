import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("sample_test.txt")
flag1 = []
flag2 = []
flag3 = []
flag4 = []
flag5 = []
flag6 = []
flag7 = []
flag8 = []
#wsj = nltk.corpus.treebank.tagged_words(tagset='universal')    # -
#word_tag_fd = nltk.FreqDist(wsj)
#print(word_tag_fd)
#[wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB']

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized[:5]:   #only the initial 5 sentences
            words = nltk.word_tokenize(i)    # words me tokenize kia
            #print(words)
            tagged = nltk.pos_tag(words)
            #print(tagged)
            # un words ko tag kia
            chunkGram_Noun = r"""Chunk_Noun: {<NNP>|<NN>|<NNS>.}  
                                        Chunk_Verb: {<VB>|<VBD>|<VBG>|<VBN>|<VBP>|<VBP>|<VBZ>.}
                                        Chunk_adverb: {<RB>|<RBR>|<RBS>|<WRB>.}
                                        Chunk_Pronoun: {<NNP>|<NNPS>|<PRP>|<PRP$>.}
                                        Chunk_Adjective: {<JJ>|<JJR>|<JJS>.}
                                        Chunk_Preposition: {<IN>.}
                                        Chunk_Determiner: {<DD>.}
                                        Chunk_Conjunction: {<CC>.}"""
            #chunkgram_Verb = r"""Chunk_Verb: {<VB>|<VBD>|<VBG>|<VBN>|<VBP>|<VBP>|<VBZ>.}"""
            chunkParser_Noun = nltk.RegexpParser(chunkGram_Noun)
            #chunkgram_verb = nltk.RegexpParser(chunkgram_verb)
            chunked_Noun = chunkParser_Noun.parse(tagged)
            #chunked_verb = chunkParser_verb.parse(tagged)
            chunked_Noun.draw()
            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_Noun'):
                flag1.append(subtree)
                #print(flag1)
                #chunked.draw()
                continue

            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_Verb'):
                flag2.append(subtree)
                continue
            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_adverb'):
                flag3.append(subtree)
                continue
            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_Pronoun'):
                flag4.append(subtree)
                continue
            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_Adjective'):
                flag5.append(subtree)
                continue
            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_Preposition'):
                flag6.append(subtree)
                continue
            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_Determiner'):
                flag7.append(subtree)
                continue
            for subtree in chunked_Noun.subtrees(filter=lambda t: t.label() == 'Chunk_Conjunction'):
                flag8.append(subtree)
                continue





    except Exception as e:
        print(str(e))


process_content()

