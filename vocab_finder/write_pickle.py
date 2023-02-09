import pickle

f1 = open('wiki-100k.txt', 'r', encoding = 'utf8')

f = f1.read()
f = f.split('\n')

master_word_list = []

for line in f:
    if not line.startswith('#'):
        master_word_list.append(line.lower())

pickle_out = open('master_word_list.pickle', 'wb')
pickle.dump(master_word_list, pickle_out)
f1.close()
pickle_out.close()
