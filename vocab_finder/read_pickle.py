import pickle

with open('master_word_list.pickle', 'rb') as f:
    words = pickle.load(f)

if 'overlooked' in words[:20000]:
    print('True')
