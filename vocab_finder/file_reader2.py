def update():
    filename = '/Users/ericschlosser/Desktop/Notes/Notes1.txt'

    output = []

    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        if line[0] == '!':
            card = line.split('-')
            card[0] = card[0][1:]
            output.append(card)

    print(output)
