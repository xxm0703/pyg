import collections
import pygame

Move = collections.namedtuple('Move', ['score', 'index'])

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

ai_p = 'X'
hu_p = 'O'


def free_spots(board):
    return [x for x in board if x != ai_p and x != hu_p]


def draw(board):
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0, 100], [300, 100], 3)
    pygame.draw.line(screen, BLACK, [0, 200], [300, 200], 3)
    pygame.draw.line(screen, BLACK, [100, 0], [100, 300], 3)
    pygame.draw.line(screen, BLACK, [200, 0], [200, 300], 3)
    for i in range(9):
        if board[i] == ai_p:
            x = (i % 3) * 100
            y = (i // 3) * 100
            pygame.draw.line(screen, BLACK, [x + 6, y + 6], [x + 94, y + 94], 3)
            pygame.draw.line(screen, BLACK, [x + 94, y + 6], [x + 6, y + 94], 3)
        elif board[i] == hu_p:
            x = (i % 3) * 100
            y = (i // 3) * 100
            pygame.draw.ellipse(screen, BLACK, [x + 6, y + 6, 88, 88], 3)

    pygame.display.flip()


def other_p(player):
    return ai_p if player == hu_p else hu_p


def winning(spot, player):
    if (spot[0] == player and spot[1] == player and spot[2] == player) or \
            (spot[3] == player and spot[4] == player and spot[5] == player) or \
            (spot[6] == player and spot[7] == player and spot[8] == player) or \
            (spot[0] == player and spot[3] == player and spot[6] == player) or \
            (spot[1] == player and spot[4] == player and spot[7] == player) or \
            (spot[2] == player and spot[5] == player and spot[8] == player) or \
            (spot[0] == player and spot[4] == player and spot[8] == player) or \
            (spot[2] == player and spot[4] == player and spot[6] == player):
        return True
    else:
        return False


def minmax(board, player):
    moves = free_spots(board)
    score = 20 if player == hu_p else -20
    best_move = Move(score, 0)
    static_board = board[:]
    if not winning(board, other_p(player)):
        for mv in moves:
            board = static_board[:]
            board[mv] = player
            if not free_spots(board) or winning(board, player):
                if winning(board, player):
                    score = 10 if player == ai_p else -10
                    return Move(score, mv)
                return Move(0, mv)
            move = minmax(board[:], other_p(player))
            if player == hu_p and move.score < best_move.score:
                best_move = Move(move.score, mv)
            elif player == ai_p and move.score > best_move.score:
                best_move = Move(move.score, mv)

    return best_move


done = False
board = [x for x in range(9)]
draw(board)

with open(".last_player", 'r') as f:
    first_p = other_p(f.read())

c_player = first_p
a = None

while not done:
    if c_player == hu_p:
        while a is None or a not in free_spots(board):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    a = pos.y//100 * pos.y%100  # TODO
    else:
        a = minmax(board[:], ai_p).index
    board[a] = c_player
    draw(board)
    if winning(board, c_player) or not free_spots(board):
        break

    c_player = other_p(c_player)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
if not done:
    if not free_spots(board):
        print("DRAW")
    else:
        print("{0} WINS!".format(c_player))
with open(".last_player", 'w') as f:
    f.write(first_p)
pygame.quit()
