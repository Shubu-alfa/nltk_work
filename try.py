dict = {}
list_input = []
# dict_noun = {}
# dict_adj = {}
# dict_adv = {}
list = []
# #dict['NN']=['array','array2','array3']
# list_n = []
dict = {'shubham': [22, 'B-tech'],'chavi': [21, 'BJMC'], 'shivam': [22, 'B-Arch']}

list_input = [('hello', 'NN'), ('man', 'NN'), ('!', '.')]


for i, j in list_input:
    print(i, j)


# #dict['NN']=100
# i = 0
# for i in dict:
#     print(dict[i])
#
#words = input("Enter the word"+"\n")
#print(dict['shubham'][1])

# dict_n = {}
# dict_n = {'shubham':['shubu', 21, 'indian', 'B-tech', '3rd yr', 'cse']}
# print(dict_n['shubham'])
# list_n = dict_n['shubham']
# for j in list_n:
#     print(j)



# dict_noun = {'noun': ['shubu', 'edward', 'shivam', 'rohit']}
# dict_adj = {'adjective': ['good', 'bad', 'nice']}
# dict_adv = {'adverb': ['near', 'forward']}
#dict['chavi'] = dict['chavi'].append(21)
#print(dict)
for i, j in list_input:
    for k in dict:
        print(k+":")
        if k == 'shubham':
            list = dict[k]
            for l in list:
                print(l)
        if k == 'chavi':
            list = dict[k]
            if j == 'NN':
                list.append(i)   # create it by default for all
            for l in list:
                print(l)
        if k == 'shivam':
            list = dict[k]
            if j == '.':
                list.append(i)
            for l in list:
                print(l)
# we have to make different list altogether
for l in list:
    print(l)


print(dict)



