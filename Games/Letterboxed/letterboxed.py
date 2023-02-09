import urllib.request
import re
import pickle


encoding = 'utf-8'

word_page = urllib.request.urlopen('http://www.mieliestronk.com/corncob_caps.txt').read()

word_page = word_page.decode(encoding)

words = word_page.split('\n')

print (len(words))
for i in range(0,len(words) - 1):
    words[i] = words[i][:-1]

if 'LAUNDRY' in words:
    print('True1')

words1 = []

# def elim():
#     for word in words:
#
#         for j in range (0, len(word) - 1):
#             if word[j] == word[j + 1]:
#                 words.remove(word)
#                 break
# elim()

def elim():
    for word in words:

        for j in range (0, len(word) - 1):
            if word[j] == word[j + 1]:
                words1.append(word)

elim()



for word in words1:
    if word in words:
        words.remove(word)


if 'LAUNDRY' in words:
    print('True')
with open('objs.pkl', 'wb') as f:
    pickle.dump([words], f)
