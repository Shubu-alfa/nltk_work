import nltk
# import tagging as tagging
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = input("Hello! Sir,How may Jarvis help you? :" + "\n")
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import sqlite3

file = open("final_code.txt", 'w+')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

dict_sample = {}
list_input = []
temp = []

dict_sample = {'NN': ['none'], 'CC': ['none'], 'CD': ['none'], 'DT': ['none'], 'EX': ['none'], 'FW': ['none'],
               'IN': ['none'], 'JJ': ['none'], 'JJR': ['none'], 'JJS': ['none'], 'LS': ['none'], 'MD': ['none'],
               'NNS': ['none'], 'NNP': ['none'], 'NNPS': ['none'], 'PDT': ['none'], 'POS': ['none'], 'PRP': ['none'],
               'PRP$': ['none'], 'RB': ['none'], 'RBR': ['none'], 'RBS': ['none'], 'RP': ['none'], 'TO': ['none'],
               'UH': ['none'], 'VB': ['none'], 'VBD': ['none'], 'VBG': ['none'], 'VBN': ['none'], 'VBP': ['none'],
               'VBZ': ['none'], 'WDT': ['none'], 'WP': ['none'], 'WP$': ['none'], 'WRB': ['none']}

def process_content():
    try:
        for i in tokenized[:1]:  # only the initial 1 sentences
            words = nltk.word_tokenize(i)  # words me tokenize kia
            # print(words)
            list_input = nltk.pos_tag(words)
            # un words ko tag kia
            # print(list_input)
            # for j, k in list_input:
            #     print(j, k)
            #     if j == 'NN':
            #         dict['NN'] = list

            for j, k in list_input:
                print(list_input)
                for l in dict_sample:
                    print(l + ":")

                    if l == 'NN':
                        list = dict_sample[l]
                        for m in list:
                            print(m)
                    if l == 'VB':
                        list = dict_sample[l]
                        if k == 'VB':
                            list.append(j)  # create it by default for all
                        # for m in list:
                        #     #print(m)
                    if l == 'DT':
                        list = dict_sample[l]
                        if k == '.':
                            list.append(j)
                        # for m in list:
                        #     #print(m)

            file.write(str(list_input))
            # print(file)

    except Exception as e:
        print(str(e))


process_content()
