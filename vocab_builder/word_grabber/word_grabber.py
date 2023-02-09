import pickle

f = open("/Users/ericschlosser/Desktop/TheHardWay/vocab_builder/word_grabber/TSL_basewrd.txt", "r")


contents = f.read()

contents = contents.split('\n\n')

n = 0
contents = [n for n in contents if len(n) > 0]

for n in range(0, len(contents)):
    contents[n] = contents[n].replace('\t', '')
    n +=1

TSL_wordlist = contents

master = open("masterTSL_word_list.pickle", "wb")

pickle.dump(TSL_wordlist, master)

master.close()
