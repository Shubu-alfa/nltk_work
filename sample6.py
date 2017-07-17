st1 = "[('hello', 'NN'), ('man', 'NN'), ('!', '.')][('my', 'PRP$'), ('name', 'NN'), ('is', 'VBZ'), ('Jeorge', 'NNP'), ('.', '.')][('its', 'PRP$'), ('all', 'DT'), ('good', 'JJ'), ('in', 'IN'), ('here', 'RB'), ('.', '.')][('let', 'VB'), ('us', 'PRP'), ('go', 'VB'), ('for', 'IN'), ('a', 'DT'), ('party', 'NN'), ('.', '.')][('thank', 'NN'), ('you', 'PRP'), ('.', '.')]"
new = ""
left = ""
right = ""
print(len(st1))
#print(st1.split("), ("))
list_noun = []
list_determiner = []
list_adjective = []
list_preposition = []
list_adverb = []
list_verb = []
list_personal_pronoun = []
file = open("output1.txt", 'w+')

wd = 'nothing'
count = 0
for i in range(0, len(st1)):
    #print(st1[i])
    if st1[i].isalpha():
        #new = ' '.join(st1[i])
        new = "{} {}".format(new, st1[i])
    if st1[i] == "(":
        if i != 1:
            count = count+1
            new = "{} {}".format(new, "+")
    if st1[i] == ",":
        new = "{} {}".format(new, ":")
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

file.write(new)
new = new.split("+", count)
for k in range(count):
    #print(new[k])

    pos = new[k].split(":", 2)
    # print(pos[0])
    if pos[1] == ' N N ' :
        list_noun.append(pos[0])
        #print(list_noun)
    elif pos[1] == " D T ":
        list_determiner.append(pos[0])
        #print("Determiner:{0}".format(pos[0]))
    elif pos[1] == " J J ":
        list_adjective.append(pos[0])
        #print("Adjective:{0}".format(pos[0]))
    elif pos[1] == " I N ":
        list_preposition.append(pos[0])
        #print("Preposition:{0}".format(pos[0]))
    elif pos[1] == " R B ":
        list_adverb.append(pos[0])
        #print("Adverb:{0}".format(pos[0]))
    elif pos[1] == " V B ":
        list_verb.append(pos[0])
    elif pos[1] == " P R P ":
        list_personal_pronoun.append(pos[0])

        #print("Verb:{0}".format(pos[0]))
print("noun:")
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
print("Personal Pronoun")
print(list_personal_pronoun)
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