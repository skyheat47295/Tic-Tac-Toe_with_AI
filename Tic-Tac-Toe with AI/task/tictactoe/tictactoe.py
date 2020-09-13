class TicTacToe:

    def __init__(self):
        self.valid_cells = 'XO_'
        # Set board Array
        self.keyboard_input = ''
        self.ttt_board = [[f'not_used_{x}:{y}' if x == 0 or y == 0 else None for y in range(4)] for x in range(4)]

    def get_action(self, prompt):
        print(prompt, end='')
        keyboard_input = str.upper(input())
        return keyboard_input

    def coordinate_validation(self):
        if self.keyboard_input in self.valid_cells:
            return True
        else:
            return False

    def populate_coordinates(self):
        print(self.keyboard_input)

    def get_coordinates(self):
        self.keyboard_input = 'None'
        while not self.coordinate_validation():
            self.keyboard_input = self.get_action('Enter cells: >')
            self.populate_coordinates()

    def main(self):
        self.get_coordinates()


tic_tac_toe = TicTacToe()
tic_tac_toe.main()
