from nltk.corpus import wordnet
syns = wordnet.synsets("program")
print(syns[0].name())
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):   # giving the synonyms of good
    for l in syn.lemmas():            # getting the lemmas of each synonym
        synonyms.append(l.name())     # adding up all the lemmas names to a list
        if l.antonyms():              # if antonyms exist of those lemmas
            antonyms.append(l.antonyms()[0].name())    # add them to the list

print(set(synonyms))
print(set(antonyms))