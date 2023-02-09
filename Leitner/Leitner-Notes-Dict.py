import random
import shelve
import datetime
from datetime import timedelta, datetime, date

#  is a function for developers only and will not be in the finished program. It resets the shelf file where words are saved to a blank list.
# Creates an empty list and sends it to 'fcdata'

def init():
    sure = input("Are you sure you want to recreate the shelf file (y/n)?  ")
    if sure.lower()[0] == 'y':
        shelfFile = shelve.open('fcdata')
        output = []
        shelfFile['output'] = output
        shelfFile.close()
        main()
    else:
        main()

# Another developer function that I use to run various tasks. Not part of the final program.
def six():
    shelfFile = shelve.open('fcdata')
    output = shelfFile['output']
    for card in output:
        card[2] = card[2] + timedelta(days = -1)
        print(card[2])
    shelfFile['output'] = output
    shelfFile.close()
    main()


# A method that adds words and definitions from 'Notes1.txt' to the shelfFile output list
# Takes list of dictionaries from 'fcdata'
# Takes data from .txt file
# Produces list with new dictionaries added.

def update():
    notes_source = input('Enter notes file name: ')
    filename = '/Users/ericschlosser/Desktop/Notes/' + notes_source + '.txt'
    l = 0
    shelfFile = shelve.open('fcdata')
    output = shelfFile['output']
    with open(filename) as file_object:
        lines = file_object.readlines()

    # Creates list of values within each card.
    # list[0] = item
    # List[1] = definition
    # list[2] = datetime date // This is the date the card will next be used.
    # list[3] = Number of consecutive right answers
    # list[4] = binary state that shows if the card has been used today
    for line in lines:

        if line[0] == '@':
            subject = line[1:]

        if line[0] == '!':
            l += 1
            card = line.split('--')
            card[0] = card[0][1:]
            card = card[:2]
            print(card[0] + ' - ' + card[1])

            #Add code to deal with duplcates
            term_dict = {}
            term_dict['term'] = card[0]
            term_dict['subject'] = subject
            term_dict['definition'] = card[1]
            term_dict['date'] = date.today()
            term_dict['consecutive right'] = 0
            term_dict['card used'] = 0
            output.append(term_dict)

    shelfFile['output'] = output
    shelfFile.close()
    print('\n\nUpdate Sucessful.\n\n')
    print(str(l) + ' new cards added.')
    main()

# Prints a list of today's words and definitions.
#Change to accomodate different subjects.

def print_list():
    shelfFile = shelve.open('fcdata')
    print("\n\n\nLIST OF TODAY'S WORDS\n\n\n")
    row = "{:15}: {:60}"
    word_list_today = shelfFile['output']
    #print(type(word_list_today))
    #print(word_list_today)
    for card in shelfFile['output']:

        if card['date'] <= date.today():
            print(row.format(card['term'], card['definition']))
    shelfFile.close()
    main()

# Quizes user with that day's flashcards.
def fc():
    word_list_today = []
    word_list_future = []
    shelfFile = shelve.open('fcdata')
    word_list = shelfFile['output']
    #print(word_list)
    for card in word_list:
        card['card used'] = 0
        #for key in card:
            #print(key)
            #card[key]['card used'] = 0
            #card.get('card used') = 0
    for card in word_list:
        if card['date'] <= date.today():
            word_list_today.append(card)
        else:
            word_list_future.append(card)

    print("There are " + str(len(word_list_today)) + " words in today's word list.")

    while len(word_list_today) > 0:
        #print(word_list_today[0])
        print('Subject: ' + word_list_today[0]['subject'])
        print(word_list_today[0]['term'] + '\n\n')
        answer = input('Enter definition: ')
        print('\n\n' + word_list_today[0]['definition'] + '\n\n')
        card = word_list_today.pop(0)
        correct = input(' Did you get the question right or wrong or have you mastered the concept (type r, w, m or q)? ')
        if correct[0].lower() == 'r':
            if card['card used'] == 0:
                card['card used'] += 1
                card['consecutive right'] += 1
                card['date'] = date.today() + timedelta(days = card['consecutive right'] * 2)
            word_list_today.append(card)
        if correct[0].lower() == 'm':
            if card['card used'] == 0:
                card['card used'] +=1
                card['consecutive right'] +=1
                card['date'] = date.today() + timedelta(days = card['consecutive right'] * 2)
            word_list_future.append(card)
        #Flip function: removed, but I may readd.
        # if correct[0].lower() == 'f':
        #     card[0], card[1] = card[1], card[0]
        #     word_list_today.append(card)
        if correct[0].lower() == 'w':
            if card['card used'] == 0:
                card['card used'] += 1
                card['consecutive right'] = 1
                card['date'] = date.today() + timedelta(days = 1)
            word_list_today.append(card)
        if correct[0].lower() == 'q':
            break
        #The following is for wrong answers. I used an 'else' statement as a filler to handle exceptions.



    for i in word_list_today:
        word_list_future.append(i)
    tomorrows_words = 0
    for card in word_list_future:
        if card['date'] <= date.today() +timedelta(days = 1):
            tomorrows_words += 1
    print("There are " + str(tomorrows_words) + " words in tomorrow's word list.")

    shelfFile['output'] = word_list_future
    shelfFile.close()
    cont = input('\n\nList Completed: Type "y" to return to the main menu.')
    if cont == 'y':
        main()
    else:
        pass

# A menu function. Option 4 has not been added yet.

def main():
    print("\n\n\nFlashcards: Main Menu\n\n")
    print("Print list of today's flashcards: Press['1']\n")
    print("Run today's flashcards:           Press['2']\n")
    print("Scan notes for flashcards:        Press['3']\n")
    print("Manually enter flashcards:        Press['4']\n")
    print("Quit:                             Press['5']\n")
    menu_choice = input("> ")
    if menu_choice == '1':
        print_list()
    elif menu_choice == '2':
        fc()
    elif menu_choice == '3':
        update()
    elif menu_choice == '4':
        manual()
    elif menu_choice == '5':
        pass
    elif menu_choice == '6':
        six()
    elif menu_choice == '0':
        init()

main()
