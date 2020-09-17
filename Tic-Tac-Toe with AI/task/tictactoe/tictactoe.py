from random import randint


class TicTacToe:

    def __init__(self):
        self.valid_cells = 'XO_'
        self.keyboard_input = ''
        self.level = 'easy'
        # Set board Array
        self.ttt_board = [[f'not.used.{x}:{y}' if x == 0 or y == 0 else ' ' for y in range(4)] for x in range(4)]

    @staticmethod
    def get_action(prompt):
        print(prompt, end='')
        keyboard_input = str.upper(input())
        return keyboard_input

    def coordinate_validation(self):
        if (len(self.keyboard_input)) == 9:
            for character in self.keyboard_input:
                if character in self.valid_cells:
                    continue
                else:
                    return False
            return True
        return False

    def move_validation(self):
        if self.keyboard_input == 'None':
            return False
        if 1 < (len(self.keyboard_input)) < 4:
            if (len(self.keyboard_input)) == 3 and self.keyboard_input[1] == ' ':
                self.keyboard_input = self.keyboard_input[0] + self.keyboard_input[2]
            if self.keyboard_input[0] in '123' and self.keyboard_input[1] in '123':
                if self.ttt_board[int(self.keyboard_input[0])][int(self.keyboard_input[1])] in 'XO':
                    print('This cell is occupied! Choose another one!')
                    return False
                return True
        if not str.isdigit(self.keyboard_input):
            print('You should enter numbers!')
            return False
        print('Coordinates should be from 1 to 3!')
        return False

    def populate_coordinates(self):
        character_position = 0
        for y in range(3, 0, -1):
            for x in range(1, 4):
                self.ttt_board[x][y] = self.keyboard_input[character_position]
                character_position += 1

    def get_coordinates(self):
        self.keyboard_input = 'None'
        while not self.coordinate_validation():
            self.keyboard_input = self.get_action('Enter cells: >')
        self.populate_coordinates()

    def display_board(self):
        print('---------')
        for y in range(3, 0, -1):
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
        for y in range(3, 0, -1):
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

        print('Draw')

    def make_move(self):
        print(f'Making move level "{self.level}"')
        x = 0
        y = 0
        if self.level == 'easy':
            self.keyboard_input = 'None'
            while not self.move_validation():
                x = randint(1, 3)
                y = randint(1, 3)
                self.keyboard_input = str(x) + str(y)
            self.ttt_board[x][y] = self.who_moves()

    def main(self):
        self.display_board()
        self.get_move()
        self.display_board()
        while self.determine_state() == 'Game not finished':
            self.make_move()
            self.display_board()
            self.get_move()
            self.display_board()
        print(self.determine_state())


tic_tac_toe = TicTacToe()
tic_tac_toe.main()
