class TicTacToe:

    def __init__(self):
        self.valid_cells = 'XO_'
        self.keyboard_input = ''
        # Set board Array
        self.ttt_board = [[f'not_used_{x}:{y}' if x == 0 or y == 0 else None for y in range(4)] for x in range(4)]

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
        pass

    def main(self):
        self.get_coordinates()
        self.display_board()
        self.get_move()
        self.display_board()


tic_tac_toe = TicTacToe()
tic_tac_toe.main()
