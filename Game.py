import numpy as np
import collections, pygame, socket, copy

Move = collections.namedtuple('Move', ['score', 'index'])

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ai_player = 'X'
human_player = 'O'


class Board(object):
    def __init__(self):
        self.cells = np.zeros([9], dtype=str)

    def __getitem__(self, tup):
        x, y = tup
        return self.cells[x * 3 + y]

    def set_cell(self, player, x):
        self.cells[x] = player

    def winning(self, player, spot=None):
        if spot is None:
            spot = self.cells
        if (spot[0] == player and spot[1] == player and spot[2] == player) or \
                (spot[3] == player and spot[4] == player and spot[5] == player) or \
                (spot[6] == player and spot[7] == player and spot[8] == player) or \
                (spot[0] == player and spot[3] == player and spot[6] == player) or \
                (spot[1] == player and spot[4] == player and spot[7] == player) or \
                (spot[2] == player and spot[5] == player and spot[8] == player) or \
                (spot[0] == player and spot[4] == player and spot[8] == player) or \
                (spot[2] == player and spot[4] == player and spot[6] == player):
            return True
        return False

    def free_cells(self, board=None):
        if board is None:
            return [i for i in range(9) if self.cells[i] == '']
        return [i for i in range(9) if board[i] == '']


class GameEngine(object):
    def __init__(self, size):
        self.board = Board()
        self.size = size
        self.cell_size = self.size // 3
        self.screen = pygame.display.set_mode([size, size])
        with open(".last_player", 'r') as f:
            self.current_player = self.next_player(f.read())
        pygame.display.set_caption("Tic Tac Toe")
        self.draw()
        self.prepare()

    def prepare(self):
        self.game_type = int(input('1 for Bot\n2 for LAN\n3 for 1v1\n' + 10 * '_' + '\n'))
        if self.game_type == 2:
            self.server = socket.socket()  # Create a socket object
            host = '192.168.1.102'  # Get local machine name
            port = 50000  # Reserve a port for your service.
            self.server.connect((host, port))

        self.game_loop()

    def game_loop(self):
        while True:
            if self.game_type == 1:
                self.bot()
            elif self.game_type == 2:
                self.lan()
            else:
                self.player_input()

            self.draw()

            if self.board.winning(self.current_player):
                print("{} WIN!".format(self.current_player))
                break
            if not self.board.free_cells():
                print("DRAW!")
                break

            self.current_player = self.next_player(self.current_player)

    def player_input(self):
        index = None
        while index is None or index not in self.board.free_cells():
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    index = pos[0] // self.cell_size + 3 * (pos[1] // self.cell_size)
        self.board.set_cell(self.current_player, index)
        return index

    @staticmethod
    def next_player(player):
        return ai_player if player == human_player else human_player

    def lan(self):
        while True:
            data = self.server.recv(1024)
            if data != '':
                break
        selected_cell = None
        if data[-1] == "Y":
            while selected_cell not in self.board.free_cells():
                selected_cell = self.player_input()
            self.server.send(str(selected_cell))
        data = self.server.recv(1024)
        self.board.set_cell(self.current_player, int(data[0]))
        return int(data[0])

    def bot(self):
        if self.current_player == human_player:
            self.player_input()
        else:
            self.board.set_cell(ai_player, self.minmax([x for x in self.board.cells], ai_player).index)

    def minmax(self, b, player):
        moves = self.board.free_cells(b)
        score = 20 if player == human_player else -20
        best_move = Move(score, 0)
        static_board = b[:]
        if not self.board.winning(self.next_player(player), b):
            for mv in moves:
                b = static_board[:]
                b[mv] = player
                if not self.board.free_cells(b) or self.board.winning(player, b):
                    if self.board.winning(player, b):
                        score = 10 if player == ai_player else -10
                        return Move(score, mv)
                    return Move(0, mv)
                move = self.minmax(b[:], self.next_player(player))
                if player == human_player and move.score < best_move.score:
                    best_move = Move(move.score, mv)
                elif player == ai_player and move.score > best_move.score:
                    best_move = Move(move.score, mv)

        return best_move

    def draw(self):
        self.screen.fill(WHITE)
        for i in range(3):
            for j in range(3):
                x = i * self.cell_size
                y = j * self.cell_size
                pygame.draw.rect(self.screen, BLACK, [x, y, x + self.cell_size, y + self.cell_size], 3)
                if self.board[j, i] == ai_player:
                    pygame.draw.line(self.screen, BLACK, [x + 6, y + 6],
                                     [x + self.cell_size - 6, y + self.cell_size - 6], 3)
                    pygame.draw.line(self.screen, BLACK, [x + self.cell_size - 6, y + 6],
                                     [x + 6, y + self.cell_size - 6], 3)
                elif self.board[j, i] == human_player:
                    pygame.draw.ellipse(self.screen, BLACK, [x + 6, y + 6, self.cell_size - 12, self.cell_size - 12], 3)

        pygame.display.flip()


g = GameEngine(300)
with open(".last_player", 'w') as f:
    f.write(g.current_player)
if g.game_type == 2:
    g.server.close()
pygame.quit()
