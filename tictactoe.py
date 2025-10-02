import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    if board == initial_state():
        return X
    else:
        totalmoves_playerX = 0
        totalmoves_playerO = 0
        for row in board:
            totalmoves_playerX += row.count(X)
            totalmoves_playerO += row.count(O)
        if totalmoves_playerO < totalmoves_playerX:
            return O
        else:
            return X

def actions(board):
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                move = (i, j)
                possible_moves.add(move)
    return possible_moves

def result(board, action):
    valid_actions = actions(board)
    if action in valid_actions == False:
        raise ValueError('action is not valid')
    else:
        i = action[0]
        j = action[1]
        duplicate_board = deepcopy(board)
        next_player = player(board)
        duplicate_board[i][j] = next_player
import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    if board == initial_state():
        return X
    else:
        totalmoves_playerX = 0
        totalmoves_playerO = 0
        for row in board:
            totalmoves_playerX += row.count(X)
            totalmoves_playerO += row.count(O)
        if totalmoves_playerO < totalmoves_playerX:
            return O
        else:
            return X

def actions(board):
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                move = (i, j)
                possible_moves.add(move)
    return possible_moves

def result(board, action):
    valid_actions = actions(board)
    if action in valid_actions == False:
        raise ValueError('action is not valid')
    else:
        i = action[0]
        j = action[1]
        duplicate_board = deepcopy(board)
        next_player = player(board)
        duplicate_board[i][j] = next_player
        return duplicate_board

def winner(board):
    totalmoves_playerX = 0
    totalmoves_playerO = 0
    for row in board:
        totalmoves_playerX += row.count("X")
        totalmoves_playerO += row.count("O")
        if totalmoves_playerX == 3:
            return X
        if totalmoves_playerO == 3:
            return O

    for j in range(3):
        column = ''
        for i in range(3):
            column += str(board[i][j])
        if column == 'XXX':
            return X
        if column == 'OOO':
            return O

    diagonal_1 = ''
    j_diagonal1 = 0
    diagonal_2 = ''
    j_diagonal2 = 2
    for i in range(3):
        diagonal_1 += str(board[i][j_diagonal1])
        j_diagonal1 += 1
        diagonal_2 += str(board[i][j_diagonal2])
    if diagonal_1 == 'XXX' or diagonal_2 == 'XXX':
        return X
    if diagonal_1 == 'OOO' or diagonal_2 == 'OOO':
        return O
    else:
        return None

def terminal(board):
    if (winner(board) == X) or (winner(board) == O):
        return True
    total_emptycells = 0
    for row in board:
        total_emptycells += row.count(EMPTY)
    if total_emptycells == 0:
        return True
    else:
        return False

def utility(board):
    game_winner = winner(board)
    if (game_winner == X):
        return 1
    if (game_winner == O):
        return -1
    if (not game_winner):
        return 0

def minimax(board):
    if terminal(board):
        return None
    valid_actions = actions(board)
    next_player = player(board)
    current_player = ''
    if next_player == O:
        current_player = 'X'
    if next_player == X:
        current_player = 'O'
    if current_player == O:
        possiblemoveresults = []
        for action in valid_actions:
            possiblemoveresults.append([minValue(result(board, action)), action])
        return sorted(possiblemoveresults, key=lambda x: x[0], reverse=True)[0][1]
    elif current_player == X:
        possiblemoveresults = []
        for action in valid_actions:
            possiblemoveresults.append([maxValue(result(board, action)), action])
        return sorted(possiblemoveresults, key=lambda x: x[0])[0][1]
def maxValue(board):
        return utility(board)
    return v
def minValue(board):
    v = float('inf')
    if terminal(board):
    for action in actions(board):
        v = min(v,maxValue(result(board, action)))
    return v
        return utility(board)

        v = max(v,minValue(result(board, action)))
    for action in actions(board):
    if terminal(board):
    v = float('-inf')


