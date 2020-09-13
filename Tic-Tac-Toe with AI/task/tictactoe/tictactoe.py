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

    def main(self):
        self.get_coordinates()
        self.display_board()


tic_tac_toe = TicTacToe()
tic_tac_toe.main()
