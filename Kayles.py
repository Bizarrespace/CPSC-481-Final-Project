import time

class KaylesGame:
    def __init__(self, num_pins):
        self.board = self.initialize_board(num_pins)
        self.current_player = 1

    def print_board(self):
        print("Current Board:")
        last_row = self.board[-1]
        for pin in last_row:
            print(pin, end=' ')
        print("\n")

    def initialize_board(self, num_pins):
        return [['X'] * num_pins]

    def is_valid_move(self, move):
        if move < 1 or move > 2:
            return False

        last_row = self.board[-1]
        if move > len(last_row) and len(last_row) != 1:
            return False

        return True

    def make_move(self, move):
        last_row = self.board[-1]
        new_row = last_row[move:]
        self.board.append(new_row)

    def is_game_over(self):
        return len(self.board[-1]) == 0

    def play(self):
        while True:
            self.print_board()

            if self.current_player == 1:
                player = "Player 1"
            else:
                player = "Player 2"

            try:
                move = int(input(f"{player}, choose your move (1 or 2): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if self.is_valid_move(move):
                self.make_move(move)
                print("\n\n\n\n\n\n")
                if self.is_game_over():
                    self.print_board()
                    print(f"{player} wins!")
                    time.sleep(1)
                    break
                self.current_player = 3 - self.current_player  # Switch player (1 -> 2, 2 -> 1)
            else:
                print("Invalid move. Try again.")

# Start the game loop
while True:
    try:
        how_many_pins = int(input("How many pins do you want to play with? "))
    except ValueError:
                print("Invalid input. Please enter a number.")
                continue
    game = KaylesGame(how_many_pins)
    game.play()

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break
