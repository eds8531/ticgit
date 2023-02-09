def printFileBoard(board):
    string = ""
    string = string + "*********************\n"
    for x in range(0, 9):
        if x == 3 or x == 6:
            string = string + "*********************\n"
        for y in range(0, 9):
            if y == 3 or y == 6:
                string = string + " * "
            string = string + str(board[x][y]) + " "
        string = string + "\n"
    string = string + "*********************\n"
    return string

# function to print the board on to the console
def printBoard(board):
    print("*********************")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("*********************")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("*", end=" ")
            print(board[x][y], end=" ")
        print()
    print("*********************")

def isFull(board):
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == 0:
                return False
    return True

def possibleEntries(board, i, j):

    possibilityArray = {}

    for x in range(1, 10):
        possibilityArray[x] = 0


    for y in range(0, 9):
        if not board[i][y] == 0:
            possibilityArray[board[i][y]] = 1

    for x in range (0,9):
        if not board[x][j] == 0:
            possibilityArray[board[x][j]] = 1

    k = 0
    l = 0
    if i>= 0 and i <=2:
        k=0
    elif i >=3 and i <=5:
        k =3
    else:
        k = 6
    if j>=0 and j<=2:
        l=0
    elif j >= 3 and j<=5:
        l = 3
    else:
        l = 6

    for x in range (k, k +3):
        for y in range (l, l + 3):
            if not board[x][y] == 0:
                possibilityArray[board[x][y]] = 1

    for x in range (1, 10):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0

    return possibilityArray

def sudokuSolver(board):

    i = 0
    j = 0

    possibilities ={}

    # t=0
    if isFull(board):
        print("Board Solved Successfully!")
        printBoard(board)
        return
    else:
        for x in range (0,9):
            for y in range (0,9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    #print('first open spot', x, y)
                    break
            else:
                continue

            #print('fail')
            break

        possibilities = possibleEntries(board, i, j)

        for x in range(1, 10):
            if not possibilities[x] ==0:
                board[i][j] = possibilities[x]
                # if t < 10 or t % 10 == 0:
                #     printBoard(board)
                sudokuSolver(board)
        board[i][j] = 0

def main():
    sB0 = input('line 1: ')
    sB1 = input('line 2: ')
    sB2 = input('line 3: ')
    sB3 = input('line 4: ')
    sB4 = input('line 5: ')
    sB5 = input('line 6: ')
    sB6 = input('line 7: ')
    sB7 = input('line 8: ')
    sB8 = input('line 9: ')
    SudokuBoard = [[0 for x in range(9)] for x in range(9)]
    SudokuBoard[0] = [int(d) for d in str(sB0)]
    SudokuBoard[1] = [int(d) for d in str(sB1)]
    SudokuBoard[2] = [int(d) for d in str(sB2)]
    SudokuBoard[3] = [int(d) for d in str(sB3)]
    SudokuBoard[4] = [int(d) for d in str(sB4)]
    SudokuBoard[5] = [int(d) for d in str(sB5)]
    SudokuBoard[6] = [int(d) for d in str(sB6)]
    SudokuBoard[7] = [int(d) for d in str(sB7)]
    SudokuBoard[8] = [int(d) for d in str(sB8)]
    printBoard(SudokuBoard)
    sudokuSolver(SudokuBoard)
    #file.close()

if __name__ == "__main__":
    main()
