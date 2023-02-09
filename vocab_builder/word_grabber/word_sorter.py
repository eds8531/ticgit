import pickle

list1 = open("master_word_list.pickle", "rb")

list1a = pickle.load(list1)

list1.close()

NGSL_wordlist = list1a

print(len(NGSL_wordlist))

master = open("master_word_list.pickle", "wb")

pickle.dump(NGSL_wordlist, master)

master.close()
