"""
A program to play Tic-Tac-Toe

"""
import random


class Player:
    def __init__(self, symbol, difficulty="user"):
        self.symbol = symbol
        self.difficulty = difficulty

    def user_move(self):
        """
        Completes one move for the game and prints the result

        returns:
            None
        """
        move_coordinate = input("Enter the coordinates:")
        try:
            coordinate = list(map(int, move_coordinate.split()))
            if any(coord not in range(1, 4) for coord in coordinate):
                print("Coordinates should be from 1 to 3!")
                self.user_move()

            elif table[coordinate[0] - 1][coordinate[1] - 1] == "X" or \
                    table[coordinate[0] - 1][coordinate[1] - 1] == "O":
                print("This cell is occupied! Choose another one!")
                self.user_move()

            else:
                table[coordinate[0] - 1][coordinate[1] - 1] = self.symbol
                print_table()
                check_win()

        except ValueError:
            print("You should enter numbers!")
            self.user_move()

    def easy_move(self):
        """
        Completes one random move for the computer and prints the result

        returns:
            None
        """
        random_coordinate_1 = random.randint(1, 3)
        random_coordinate_2 = random.randint(1, 3)
        coordinate = [random_coordinate_1, random_coordinate_2]
        if table[coordinate[0] - 1][coordinate[1] - 1] != "_":
            self.easy_move()

        else:
            table[coordinate[0] - 1][coordinate[1] - 1] = self.symbol
            print(f"Making move level \"{self.difficulty}\"")
            print_table()
            check_win()

    def medium_move(self, opponent):
        """
        Completes one move of medium difficulty for the computer and prints the result

        parameter:
            opponent - the other player

        returns:
            None
        """
        row_count_1 = 0
        for row in table:
            if row.count(self.symbol) == 2 and "_" in row:
                table[row_count_1][row.index("_")] = self.symbol
                print(f"Making move level \"{self.difficulty}\"")
                print_table()
                check_win()
                return
            row_count_1 += 1

        for i in range(len(table)):
            temp_col = [table[0][i], table[1][i], table[2][i]]
            if temp_col.count(self.symbol) == 2 and "_" in temp_col:
                table[temp_col.index("_")][i] = self.symbol
                print(f"Making move level \"{self.difficulty}\"")
                print_table()
                check_win()
                return

        diagonal_1 = [table[0][0], table[1][1], table[2][2]]
        diagonal_2 = [table[0][2], table[1][1], table[2][0]]
        if diagonal_1.count(self.symbol) == 2 and "_" in diagonal_1:
            table[diagonal_1.index("_")][diagonal_1.index("_")] = self.symbol
            print(f"Making move level \"{self.difficulty}\"")
            print_table()
            check_win()
            return

        elif diagonal_2.count(self.symbol) == 2 and "_" in diagonal_2:
            table[diagonal_2.index("_")][2 - diagonal_2.index("_")] = self.symbol
            print(f"Making move level \"{self.difficulty}\"")
            print_table()
            check_win()
            return

        row_count_2 = 0
        for row in table:
            if row.count(opponent.symbol) == 2 and "_" in row:
                table[row_count_2][row.index("_")] = self.symbol
                print(f"Making move level \"{self.difficulty}\"")
                print_table()
                check_win()
                return
            row_count_2 += 1

        for i in range(len(table)):
            temp_col = [table[0][i], table[1][i], table[2][i]]
            if temp_col.count(opponent.symbol) == 2 and "_" in temp_col:
                table[temp_col.index("_")][i] = self.symbol
                print(f"Making move level \"{self.difficulty}\"")
                print_table()
                check_win()
                return

        if diagonal_1.count(opponent.symbol) == 2 and "_" in diagonal_1:
            table[diagonal_1.index("_")][diagonal_1.index("_")] = self.symbol
            print(f"Making move level \"{self.difficulty}\"")
            print_table()
            check_win()
            return

        elif diagonal_2.count(opponent.symbol) == 2 and "_" in diagonal_2:
            table[diagonal_2.index("_")][2 - diagonal_2.index("_")] = self.symbol
            print(f"Making move level \"{self.difficulty}\"")
            print_table()
            check_win()
            return

        else:
            self.easy_move()


player_1 = Player("X")
player_2 = Player("O")

exit_condition = 0


def game_menu():
    """
    Prompts player for a command to start or exit the game

    returns:
        None
    """
    global exit_condition
    input_command = input("Input command:").split()
    if input_command == ["exit"]:
        exit_condition += 1
    else:
        try:
            if input_command[0] != "start" or \
                    (input_command[1] != "user" and input_command[1] != "easy" and input_command[1] != "medium") \
                    or (input_command[2] != "user" and input_command[2] != "easy" and input_command[2] != "medium"):
                print("Bad parameters!")
                game_menu()
            else:
                player_1.difficulty = input_command[1]
                player_2.difficulty = input_command[2]

        except IndexError:
            print("Bad parameters!")
            game_menu()


table = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def print_table():
    """
    Prints the matrix "table" as a Tic-Tac-Toe board

    returns:
        None
    """
    for i in range(len(table) * 3):
        print('-', end='')

    print()

    for row in range(len(table)):
        print('|', end=' ')
        for col in range(len(table)):
            if table[row][col] == '_':
                print(' ', end=' ')
            else:
                print(table[row][col], end=' ')
        print('|')

    for i in range(len(table) * 3):
        print('-', end='')
    print()


win = 0
draw = 0


def check_win():
    """
    Determines the state of the Tic-Tac_Toe board as "win", "draw", or "Game not finished" and prints the result

    returns:
        None
    """
    global win
    global draw
    winning_symbol = ""
    for i in range(len(table)):
        if table[i][0] == table[i][1] and table[i][1] == table[i][2] and table[i][0] != "_":
            win += 1
            if winning_symbol == "":
                winning_symbol = table[i][0]

        elif table[0][i] == table[1][i] and table[1][i] == table[2][i] and table[0][i] != "_":
            win += 1
            if winning_symbol == "":
                winning_symbol = table[0][i]

    if table[0][0] == table[1][1] and table[1][1] == table[2][2] and table[0][0] != "_":
        win += 1
        if winning_symbol == "":
            winning_symbol = table[0][0]

    elif table[0][2] == table[1][1] and table[1][1] == table[2][0] and table[0][2] != "_":
        win += 1
        if winning_symbol == "":
            winning_symbol = table[0][2]

    if win > 0:
        print(winning_symbol, "wins")

    elif not any("_" in cell for cell in table):
        draw += 1
        print("Draw")


def play_game():
    """
    Let's players make their moves until the game ends

    returns:
        None
    """
    global win
    global draw
    global table
    print_table()
    while win == 0 and draw == 0:
        if player_1.difficulty == "user":
            player_1.user_move()
        elif player_1.difficulty == "easy":
            player_1.easy_move()
        elif player_1.difficulty == "medium":
            player_1.medium_move(player_2)

        if win == 0 and draw == 0:
            if player_2.difficulty == "user":
                player_2.user_move()
            elif player_2.difficulty == "easy":
                player_2.easy_move()
            elif player_2.difficulty == "medium":
                player_2.medium_move(player_1)
    win = 0
    draw = 0
    table = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']] ## what


def main():
    """
    Main Wrapper Function

    returns:
        None
    """
    while exit_condition == 0:
        game_menu()
        if exit_condition == 0:
            play_game()
        else:
            exit(main())


if __name__ == "__main__":
    main()
