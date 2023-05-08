import time
def print_board(board):
    print("Current Board:")
    last_row = board[-1]
    for pin in last_row:
        print(pin, end=' ')
    print()
    print()

def initialize_board(num_pins):
    return [['X'] * num_pins]

    
def is_valid_move(board, move):
    if move < 1 or move > 2:
        return False

    last_row = board[-1]
    if move > len(last_row) and len(last_row) != 1:
        return False

    return True


def make_move(board, move):
    last_row = board[-1]
    new_row = last_row[move:]
    board.append(new_row)
    return board


def is_game_over(board):
    return len(board[-1]) == 0


def play_kayles(num_pins):
    board = initialize_board(num_pins)
    current_player = 1

    while True:
        print_board(board)

        if current_player == 1:
            player = "Player 1"
        else:
            player = "Player 2"

        move = int(input(f"{player}, choose your move (1 or 2): "))

        if is_valid_move(board, move):
            board = make_move(board, move)
            if is_game_over(board):
                print_board(board)
                print(f"{player} wins!")
                time.sleep(3)
                break
            current_player = 3 - current_player  # Switch player (1 -> 2, 2 -> 1)
        else:
            print("Invalid move. Try again.")


# Start the game with 10 pins
play_kayles(10)
