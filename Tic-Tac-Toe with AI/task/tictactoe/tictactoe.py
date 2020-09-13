class TicTacToe:

    def __init__(self):
        self.valid_cells = 'XO_'
        # Set board Array
        self.keyboard_input = ''
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
        for character_position in range(len(self.keyboard_input)):
            for y in range(3, 0, -1):
                for x in range(1, 4):
                    self.ttt_board[x][y] = self.keyboard_input[character_position]
        print(self.ttt_board)

    def get_coordinates(self):
        self.keyboard_input = 'None'
        while not self.coordinate_validation():
            self.keyboard_input = self.get_action('Enter cells: >')
        self.populate_coordinates()

    def display_board(self):
        pass

    def main(self):
        self.get_coordinates()


tic_tac_toe = TicTacToe()
tic_tac_toe.main()
