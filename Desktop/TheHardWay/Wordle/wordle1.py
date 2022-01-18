import shelve
import random

shelfFile = shelve.open('five_words')
five_words = shelfFile['five_words']

def wordle_blitz(five_words1, guess1, guess2, guess3):

    count = 0
    right = 0
    wrong = 0
    round_dict = {1:0,2:0,3:0,4:0,5:0,6:0}
    while count < 10000:
        if count%100 ==0:
            print(count)
        guess_list = []
        five_words = five_words1
        count += 1
        random.shuffle(five_words)
        target_word = random.choice(five_words)
        guesses = 0
        while guesses < 6:
            if guesses == 0:
                guess = guess1
            elif guesses == 1:
                guess = guess2
            elif guesses == 2:
                guess = guess3
            else:
                guess = random.choice(five_words)
            guess_list.append(guess)
            if guess == target_word:
                right +=1
                break

            guesses +=1
            for i in range(0,5):
                if guess[i] == target_word[i]:
                    five_words = [word for word in five_words if  word[i] == guess[i]]
                elif guess[i] in target_word:
                    #Includes letters in words, but in the wrong spaces
                    five_words = [word for word in five_words if guess[i] in word]
                    #Exclude the words with the right letters in the wrong places
                    five_words = [word for word in five_words if  word[i] != guess[i]]

                else:
                    five_words = [word for word in five_words if guess[i] not in word]
        if guesses == 6:
            wrong +=1
            if wrong%25 == 0:
                print(target_word)
                print(guess_list)
    print(guess1)
    print(guess2)
    print(guess3)
    print(count)
    print('Correct tries: ' + str(right))
    print('Incorrect tries: ' + str(wrong))
    print('Percent correct: {:.2%}'.format(right/10000))

wordle_blitz(five_words, 'brick', 'stomp', 'nudge')
