from random import randint


class TicTacToe:

    users = ['user', 'easy', 'medium']

    def __init__(self):
        self.valid_cells = 'XO_'
        self.keyboard_input = ''
        self.level = 'easy'
        self.player_x = ''
        self.player_o = ''
        self.ttt_board = [[f'not.used.{x}:{y}' if x == 0 or y == 0 else ' ' for y in range(4)] for x in range(4)]

    def init_board(self):
        self.ttt_board = [[f'not.used.{x}:{y}' if x == 0 or y == 0 else ' ' for y in range(4)] for x in range(4)]
        return self.ttt_board

    @staticmethod
    def get_action(prompt):
        print(prompt, end='')
        keyboard_input = str.upper(input())
        return keyboard_input

    def move_validation(self):
        if self.keyboard_input == 'None':
            return False
        if 1 < (len(self.keyboard_input)) < 4:
            if (len(self.keyboard_input)) == 3 and self.keyboard_input[1] == ' ':
                self.keyboard_input = self.keyboard_input[0] + self.keyboard_input[2]
            if self.keyboard_input[0] in '123' and self.keyboard_input[1] in '123':
                if self.ttt_board[int(self.keyboard_input[0])][int(self.keyboard_input[1])] in 'XO':
                    return False
                return True
        if not str.isdigit(self.keyboard_input):
            print('You should enter numbers!')
            return False
        print('Coordinates should be from 1 to 3!')
        return False

    def display_board(self):
        print('---------')
        for y in range(1, 4):  # y counts from top down (bottom up is (3,0 -1))
            print('| ', end='')
            for x in range(1, 4):
                print(f'{self.ttt_board[x][y]} ', end='')
            print('|')
        print('---------')

    def get_move(self):
        self.keyboard_input = 'None'
        while not self.move_validation():
            self.keyboard_input = self.get_action('Enter the coordinates: >')
        self.ttt_board[int(self.keyboard_input[0])][int(self.keyboard_input[1])] = self.who_moves()

    def who_moves(self):
        x_char = 0
        o_char = 0
        for y in range(1, 4):  # y counts from top down (bottom up is (3,0 -1))
            for x in range(1, 4):
                if self.ttt_board[x][y] == 'X':
                    x_char += 1
                elif self.ttt_board[x][y] == 'O':
                    o_char += 1
        if x_char <= o_char:
            return 'X'
        else:
            return 'O'

    def determine_state(self):
        for x_or_o in 'XO':
            for x in range(1, 4):
                if self.ttt_board[x][1] == x_or_o and self.ttt_board[x][2] == x_or_o and self.ttt_board[x][3] == x_or_o:
                    return f'{x_or_o} wins'
        for x_or_o in 'XO':
            for y in range(1, 4):
                if self.ttt_board[1][y] == x_or_o and self.ttt_board[2][y] == x_or_o and self.ttt_board[3][y] == x_or_o:
                    return f'{x_or_o} wins'
        for x_or_o in 'XO':
            if self.ttt_board[1][1] == x_or_o and self.ttt_board[2][2] == x_or_o and self.ttt_board[3][3] == x_or_o:
                return f'{x_or_o} wins'
        for x_or_o in 'XO':
            if self.ttt_board[3][1] == x_or_o and self.ttt_board[2][2] == x_or_o and self.ttt_board[1][3] == x_or_o:
                return f'{x_or_o} wins'
        for x in range(1, 4):
            for y in range(1, 4):
                if ' ' in self.ttt_board[x][y]:
                    return 'Game not finished'

        return 'Draw'

    def medium_strategy(self):
        for x_or_o in 'XO':
            for x in range(1, 4):
                if self.ttt_board[x][1] == x_or_o and self.ttt_board[x][2] == x_or_o and self.ttt_board[x][3] == ' ':
                    self.ttt_board[x][3] = self.who_moves()
                    return True
                elif self.ttt_board[x][1] == ' ' and self.ttt_board[x][2] == x_or_o and self.ttt_board[x][3] == x_or_o:
                    self.ttt_board[x][1] = self.who_moves()
                    return True
        for x_or_o in 'XO':
            for y in range(1, 4):
                if self.ttt_board[1][y] == x_or_o and self.ttt_board[2][y] == x_or_o and self.ttt_board[3][y] == ' ':
                    self.ttt_board[3][y] = self.who_moves()
                    return True
                elif self.ttt_board[1][y] == ' ' and self.ttt_board[2][y] == x_or_o and self.ttt_board[3][y] == x_or_o:
                    self.ttt_board[1][y] = self.who_moves()
                    return True
        for x_or_o in 'XO':
            if self.ttt_board[1][1] == x_or_o and self.ttt_board[2][2] == x_or_o and self.ttt_board[3][3] == ' ':
                self.ttt_board[3][3] = self.who_moves()
                return True
            elif self.ttt_board[1][1] == ' ' and self.ttt_board[2][2] == x_or_o and self.ttt_board[3][3] == x_or_o:
                self.ttt_board[1][1] = self.who_moves()
                return True
        for x_or_o in 'XO':
            if self.ttt_board[3][1] == x_or_o and self.ttt_board[2][2] == x_or_o and self.ttt_board[1][3] == ' ':
                self.ttt_board[1][3] = self.who_moves()
                return True
            elif self.ttt_board[3][1] == ' ' and self.ttt_board[2][2] == x_or_o and self.ttt_board[1][3] == x_or_o:
                self.ttt_board[3][1] = self.who_moves()
                return True
        return False

    def make_move(self):
        print(f'Making move level "{self.level}"')
        x = 0
        y = 0
        self.keyboard_input = 'None'

        if self.level == 'medium' and self.medium_strategy():
            self.ttt_board[x][y] = self.who_moves()
            return
        else:
            while not self.move_validation():
                x = randint(1, 3)
                y = randint(1, 3)
                self.keyboard_input = str(x) + str(y)
            self.ttt_board[x][y] = self.who_moves()

    def play_game(self):
        while self.determine_state() == 'Game not finished':
            self.display_board()
            if self.who_moves() == 'X':
                if self.player_x == 'easy':
                    self.level = 'easy'
                    self.make_move()
                elif self.player_x == 'medium':
                    self.level = 'medium'
                    self.make_move()
                elif self.player_x == 'user':
                    self.get_move()
                continue
            if self.who_moves() == 'O':
                if self.player_o == 'easy':
                    self.level = 'easy'
                    self.make_move()
                elif self.player_o == 'medium':
                    self.level = 'medium'
                    self.make_move()
                elif self.player_o == 'user':
                    self.get_move()

        self.display_board()

    def menu_loop(self):
        self.keyboard_input = 'None'
        while self.keyboard_input[0] != 'exit':
            self.keyboard_input = self.get_action('Input command: >')
            self.keyboard_input = str.lower(self.keyboard_input)
            self.keyboard_input = self.keyboard_input.split()
            if self.keyboard_input[0] == 'start' and len(self.keyboard_input) == 3:
                if self.keyboard_input[1] in tic_tac_toe.users and self.keyboard_input[2] in tic_tac_toe.users:
                    self.player_x = self.keyboard_input[1]
                    self.player_o = self.keyboard_input[2]
            elif self.keyboard_input[0] == 'exit':
                continue
            else:
                print('Bad parameters')
                continue
            self.init_board()
            self.play_game()
            print(self.determine_state())

    def main(self):
        self.menu_loop()


tic_tac_toe = TicTacToe()
tic_tac_toe.main()

