COLORS = {
    "red": "ff0000",
    "blue": "0000ff",
    "green": "00ff00",
    "orange": "ffa500"
}
board = [' '] * 10
COMPUTER, HUMAN = 'X', 'O'

def clear_board():
    global board
    board = [' '] * 10

def check_win():
    if board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    if board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    if board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    if board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    if board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    if board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    if board[1] == board[5] == board[9] and board[1] != ' ':
        return True
    if board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    return False

def is_win(letter):
    if board[1] == board[2] == board[3] and board[1] == letter:
        return True
    if board[4] == board[5] == board[6] and board[4] == letter:
        return True
    if board[7] == board[8] == board[9] and board[7] == letter:
        return True
    if board[1] == board[4] == board[7] and board[1] == letter:
        return True
    if board[2] == board[5] == board[8] and board[2] ==letter:
        return True
    if board[3] == board[6] == board[9] and board[3] == letter:
        return True
    if board[1] == board[5] == board[9] and board[1] == letter:
        return True
    if board[7] == board[5] == board[3] and board[7] == letter:
        return True
    return False


def check_draw():
    if board.count(' ') < 2:
        return True
    return False


def is_available(pos):
    return True if board[pos] == ' ' else False


def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        if check_win():
            if letter == 'X':
                # print("Computer Wins")
                # # exit()
                return "Computer Wins-blue"
            else:
                print("Human wins")
                return "Human Wins-green"
        if check_draw():
            # print("Draw")
            return "Draw-orange"
            # exit()
    else:
        # pos = int(input("Not Free! Please re-enter a position"))
        insert(letter, pos)


def human_move(pos, letter):
    # pos = int(input("Enter the position to insert:"))
    rv = insert(letter, pos)
    return rv

def computer_move(letter):
    best_score = -100
    best_pos = 0
    for index in range(1, len(board)):
        if is_available(index):
            board[index] = letter
            score = minimax(board, False)
            board[index] = " "
            if score > best_score:
                best_score = score
                best_pos = index
    rv = insert(letter, best_pos)
    return (best_pos, rv)


def minimax(board, is_maximizing):
    if is_win(COMPUTER):
        return 10
    if is_win(HUMAN):
        return -10
    if check_draw():
        return 0
    if is_maximizing: # computer turn
        best_score = -100
        for index in range(1, len(board)):
            if is_available(index):
                board[index] = COMPUTER
                score = minimax(board, False)
                board[index] = " "
                best_score = max(best_score,score)
        return best_score
    # human turn
    best_score = 100
    for index in range(1, len(board)):
        if is_available(index):
            board[index] = HUMAN
            score = minimax(board, True)
            board[index] = " "
            best_score = min(best_score,score)
    return best_score



# # main loop
# while not check_win():
#     computer_move(COMPUTER)
#     human_move(HUMAN)