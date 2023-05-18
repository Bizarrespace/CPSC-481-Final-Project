
from games import *

class Kayles(Game):
    def __init__(self, board):
        moves = [1,2]
        self.initial = GameState(to_move='Player1', utility=0, board=board, moves=moves)

    def result(self, state, move):
        board = state.board.copy()
        new_row = board[move:]
        if len(new_row) >= 2:
            moves = [1,2]
        else:
            moves = [1]
        player = state.to_move
        return GameState(to_move=("Player2" if state.to_move == "Player1" else "Player1"),
                         utility=self.compute_utility(new_row, player),
                         board=new_row, moves=moves)
    
    def actions(self, state):
        if len(state.board) >= 2:
            moves = [1,2]
        else:
            moves = [1]
        return moves
    
    def terminal_test(self, state):
        return state.utility != 0 or len(state.board) == 0
    
    def utility(self, state, player):
        return state.utility if player == 'Player1' else -state.utility
    
    def compute_utility(self, board, player):
        """If 'MAX' wins with this move, return 1; if 'MIN' wins return -1; else return 0."""
        if (len(board) == 0):
            return +1 if player == 'Player1' else -1
        else:
            return 0

    def to_move(self, state):
        return super().to_move(state)
    
    def display(self, state):
        # board = state.board
        print("board: ", state.board)


if __name__ == "__main__":
    while True:
        try:
            how_many_pins = int(input("How many pins do you want to play with? "))
        except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        board = ['X'] * how_many_pins
        kayles = Kayles(board=board) 

        play_against = input("Play Menu: \n Human Vs Computer (1) \n Human Vs Human (2) \n AI VS AI (3) \n")
        print(play_against)


        if play_against.lower() == "computer" or play_against.lower() == "1":
            utility = kayles.play_game(alpha_beta_player, query_player) # human vs ai
            if (utility < 0):
                print("\nPlayer won the game")
            else:
                print("\nComputer won the game")
        elif play_against.lower() == "player" or play_against.lower() == "2":
            utility = kayles.play_game(query_player, query_player) # human vs human 
            if (utility < 0):
                print("\nPlayer 2 won the game")
            else:
                print("\nPlayer 1 won the game")
        elif play_against.lower() == "AI vs AI" or play_against.lower() == "3":
            utility = kayles.play_game(alpha_beta_player, alpha_beta_player2) # human vs human 
            if (utility < 0):
                print("\nComputer 2 won the game")
            else:
                print("\nComputer 1 won the game")
        

        play_again = input("\nDo you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            break