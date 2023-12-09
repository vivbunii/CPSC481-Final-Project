import pygame

# Function to populate the game board with pieces and tiles 
def populateBoard():
    from ui.colors import red, black
    from game_logic.tile import Tile
    from ui.game_view import board, tileSize
    from game_logic.piece import Piece

    # Loop through rows and columns to create tiles and add pieces
    for i in range(8):
        row = list()
        for j in range(8):
            # Determine the tile color based on row and column
            color = red if (i + j) % 2 == 0 else black
            piece = None
            if i < 3 and color == black:
                piece = Piece(black, (i, j))
            elif i > 4 and color == black:
                piece = Piece(red, (i, j))
            # Create a tile and add it to the row
            row.append(Tile(color, piece, pygame.Vector2(j * tileSize, i * tileSize)))  # Swap i and j
        board.append(row)

# Function to evaluate the board position
def evaluate_board(board, color):
    from game_logic.piece import get_all_pieces, get_all_kings
    from algorithm.ai_utils import getOpponentColor
    piece_weight = 1
    king_weight = 2

    # Get player's and opponent's pieces and kings
    player_pieces = get_all_pieces(board, color)
    opponent_pieces = get_all_pieces(board, getOpponentColor(color))
    player_kings = get_all_kings(board, color)
    opponent_kings = get_all_kings(board, getOpponentColor(color))

    # Calculate player and opponent scores based on pieces and kings
    player_score = len(player_pieces) * piece_weight + len(player_kings) * king_weight
    opponent_score = len(opponent_pieces) * piece_weight + len(opponent_kings) * king_weight

    # Positional Advantage: Add bonus for pieces closer to the king's row
    king_row = 0 if color == "red" else 7
    for piece in player_pieces:
        if piece.pos[0] >= king_row - 2:
            player_score += 2 

    for piece in opponent_pieces:
        if piece.pos[0] <= 2 + king_row:
            opponent_score += 2 

    return player_score - opponent_score

# Function to create a copy of the game board
def createBoardCopy(board):
    from game_logic.tile import Tile
    new_board = []
    for row in board:
        new_row = []
        for tile in row:
            # Create a new tile with the same color, piece, and position
            new_tile = Tile(tile.color, tile.piece, tile.pos)
            new_row.append(new_tile)
        new_board.append(new_row)
    return new_board

# Function to print the game board for debugging purposes
def printBoard(board):
  from ui.colors import black
  for row in board:
    for tile in row:
        if tile.piece:
          if tile.piece.color == black:
              print("B", end = " ") # Print B for black pieces
          else:
              print("R", end = " ") #
        else:
          print("0", end = " ") # Print 0 for empty tiles
    print()