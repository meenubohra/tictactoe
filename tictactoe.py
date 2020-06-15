# create a board
# board = [
#         ['_', '_', '_'],
#         ['_', '_', '_'],
#         ['_', '_', '_']
# ]
# create board using list comprehension#list of lists#_ is the throwaway variable->its value is not required
def main():
    board = [['_' for _ in range(3)] for _ in range(3)]
    # calling functions#while to get rows frm user one after another
# switching player with is_x variable
    is_x = True
    count = 0
    while True:
        displayBoard(board)
        try:
            selection = selectSquare()
            # print(mapUserInput(selection))
            putPiecesOnBoard(mapUserInput(selection), is_x, board)
        except ValueError:
            print('Enter a valid number between 1-9')
            continue
        is_x = not is_x
        count += 1
        if count > 9:
            print('Draw! No more moves')
            break
        if isWin(board):
            break

# print the board


def displayBoard(board):
    for row in board:
        print(row)

# prints individual element
# for i in range(3):
#     for j in range(3):
#         print(board[i][j])

# Running speed test
# import timeit
# start = timeit.default_timer()
# for row in board:
#     print(board)
# end = timeit.default_timer()
# print(f"time for for loop : {end-start}")

# start = timeit.default_timer()
# [print(row) for row in board]
# end = timeit.default_timer()
# print(f"time for list comph : {end-start}")  # this takes more time

# prompt the user#type conversion#validate 1-9#exceptional problems#refactor it by making it a function


def selectSquare():
    square = int(input('Please enter the square between 1 to 9 :'))

    if square > 9 or square < 1:
        raise ValueError
    return square

# map user input into the board squares#map 1-9 to i,j


def mapUserInput(selection):
    selection -= 1  # range0-8 ,below formula works perfectly
    return (selection)//3, (selection) % 3

# update the board#selection is a tuple here
 # no overwrting others move


def putPiecesOnBoard(selection, is_x, board):
    i, j = selection
    if board[i][j] == '_':
        board[i][j] = 'X' if is_x else 'O'
    else:
        raise ValueError


def isWin(board):
    win = None
    for i in range(3):
        # horizontal win
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            win = board[i][0]
        # vertical win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            win = board[0][i]
    # diagonal win
    if board[1][1] != '_':
        if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
            win = board[1][1]
    if win != None:
        displayBoard(board)
        print(f"winner is {win}")
        return True
    return False


if __name__ == '__main__':
    main()
