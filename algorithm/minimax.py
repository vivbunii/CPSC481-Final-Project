from algorithm.ai_utils import get_all_possible_moves, getOpponentColor, game_over
from game_logic.board import evaluate_board


from algorithm.ai_utils import get_all_possible_moves, getOpponentColor, game_over
from game_logic.board import evaluate_board

# Minimax algorithm function
def minimax(board, depth, is_maximizing, current_color):
    # Base case: If the maximum depth is reached or the game is over, return the evaluation score and the current board
    if depth == 0 or game_over(board):
        return evaluate_board(board, current_color), board

    if is_maximizing:  # If it's the maximizing player's turn
        max_eval = float('-inf')  # Initialize the maximum evaluation score to negative infinity
        best_move = None  # Initialize the best move to None

        # Loop through all possible moves for the current player
        for move in get_all_possible_moves(board, current_color):
            evaluation = minimax(move, depth - 1, False, current_color)[0]  # Recursively evaluate the move
            max_eval = max(max_eval, evaluation)  # Update the maximum evaluation score

            if max_eval == evaluation:
                best_move = move  # If the current move leads to the maximum evaluation, set it as the best move

        return max_eval, best_move  # Return the maximum evaluation score and the best move
    else:  # If it's the minimizing player's turn
        min_eval = float('inf')  # Initialize the minimum evaluation score to positive infinity
        best_move = None  # Initialize the best move to None

        # Loop through all possible moves for the opponent player
        for move in get_all_possible_moves(board, getOpponentColor(current_color)):
            evaluation = minimax(move, depth - 1, True, current_color)[0]  # Recursively evaluate the move
            min_eval = min(min_eval, evaluation)  # Update the minimum evaluation score

            if min_eval == evaluation:
                best_move = move  # If the current move leads to the minimum evaluation, set it as the best move

        return min_eval, best_move  # Return the minimum evaluation score and the best move
