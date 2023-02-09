import pickle

list1 = open("master_word_list.pickle", "rb")

list1a = pickle.load(list1)

list1.close()

print(len(list1a))

f = open("suplemental_basewrd.txt", "r")

contents = f.read()

contents = contents.split('\n\n')

n = 0
contents = [n for n in contents if len(n) > 0]

for n in range(0, len(contents)):
    contents[n] = contents[n].replace('\t', '')
    n +=1

NGSL_wordlist = list1a + contents

print(len(NGSL_wordlist))

master = open("master_word_list.pickle", "wb")

pickle.dump(NGSL_wordlist, master)

master.close()
