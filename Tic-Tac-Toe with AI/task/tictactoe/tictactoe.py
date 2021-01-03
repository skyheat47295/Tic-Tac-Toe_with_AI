from random import randint
import copy


class TicTacToe:

    users = ['user', 'easy', 'medium', 'hard']

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

    def hard_strategy(self):
        orig_board = copy.deepcopy(self.ttt_board)
        orig_who_moves = copy.deepcopy(self.who_moves())
        best_move = [0, 0, 0, 0]  # x, y, score, depth
        best_move_ai = [0, 0, 0, 0]  # x, y, score, depth for inner loop
        x = 1
        y = 1
        #  orig_x = [0]
        #  orig_y = [0]

        def minimax():

            def coord_calc():
                #  if best_move[3] == 0:  # finding the base case and making sure we're placing the correct xy pair
                best_move_ai[0] = x
                best_move_ai[1] = y
                #  else:
                # best_move[0] = orig_x[0]
                # best_move[1] = orig_y[0]
                # self.keyboard_input = 'None'

            self.keyboard_input = str(x) + str(y)  # Starting Move
            if self.move_validation():
                # start of evil section
                if not self.medium_strategy():
                    self.ttt_board[x][y] = self.who_moves()
                if self.ttt_board[2][2] == ' ' and self.who_moves() == 'O':
                    self.ttt_board[2][2] = self.who_moves()  # always take center if available
                self.display_board()
            for ai_y in range(1, 4):
                for ai_x in range(1, 4):
                    # if best_move[3] == 0:
                    #    orig_x[0] = ai_x
                    #    orig_y[0] = ai_y
                    self.keyboard_input = str(ai_x) + str(ai_y)
                    if self.move_validation():
                        # start of evil section
                        if not self.medium_strategy():
                            self.ttt_board[ai_x][ai_y] = self.who_moves()
                        if self.ttt_board[2][2] == ' ' and self.who_moves() == 'O':
                            self.ttt_board[2][2] = self.who_moves()  # always take center if available
                        # end of evil section
                        self.display_board()
                        if self.determine_state() == (orig_who_moves + ' wins'):  # maximizer wins
                            coord_calc()
                            best_move_ai[2] += 1
                            break
                        elif self.determine_state() == 'Draw':
                            coord_calc()
                            best_move_ai[2] += 0
                            break
                        elif 'wins' in self.determine_state():  # minimizer wins
                            coord_calc()
                            best_move_ai[2] += -1
                            break
                        else:
                            # if best_move[3] == 0:
                            #     orig_x[0] = ai_x
                            #     orig_y[0] = ai_y
                            best_move_ai[3] += 1
                            minimax()
                            self.keyboard_input = 'None'
                            break

        if self.medium_strategy():
            return True

        for y in range(1, 4):
            for x in range(1, 4):
                minimax()
                print(best_move, ' best move', best_move_ai, 'best move ai')
                if best_move_ai[2] > best_move[2]:
                    best_move = best_move_ai
                best_move_ai = [0, 0, 0, 0]  # Reset best move counter
                self.ttt_board = copy.deepcopy(orig_board)  # clear board for next test
        self.ttt_board = copy.deepcopy(orig_board)
        self.keyboard_input = 'None'

        print(best_move, 'best move')
        if best_move[0] > 0 and best_move[2] >= 0:
            self.ttt_board[best_move[0]][best_move[1]] = self.who_moves()
            self.keyboard_input = 'None'  # zero out the x,y coordinates
            return True
        return False

    def make_move(self):
        print(f'Making move level "{self.level}"')
        x = 0
        y = 0
        self.keyboard_input = 'None'

        if self.level == 'medium' and self.medium_strategy():
            return
        if self.level == 'hard':
            #  if self.ttt_board[2][2] == ' ' and self.who_moves() == 'O':
            #    self.ttt_board[2][2] = self.who_moves()  # always take center if available
            #    return
            if self.hard_strategy():
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
                elif self.player_x == 'hard':
                    self.level = 'hard'
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
                elif self.player_o == 'hard':
                    self.level = 'hard'
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
