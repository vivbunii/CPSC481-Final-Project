from ui.game_view import tileSize, board
from ui.colors import red, black

def checkingKinging(piece, targetTile):
    if piece.color == red:
        if targetTile.pos.y == 0:
            piece.makeKing()
    elif piece.color == black:
        if targetTile.pos.y == tileSize * 7:
            piece.makeKing()

# Function to check if a move from sourceTile to targetTile is a valid drop area
def isValidDropArea(sourceTile, targetTile):
  if sourceTile is None or targetTile is None:
    return False
  dx = targetTile.pos.x - sourceTile.pos.x # Calculate horizontal distance
  dy = targetTile.pos.y - sourceTile.pos.y # Calculate vertical distance
  piece = sourceTile.piece
  if piece is None or targetTile.piece is not None:
    return False
  if piece.king:
    if abs(dx) == tileSize * 2 and abs(dy) == tileSize * 2:
      midY = (targetTile.pos.x + sourceTile.pos.x) // 2
      midX = (targetTile.pos.y + sourceTile.pos.y) // 2
      midTile = board[int(midX // tileSize)][int(midY // tileSize)]
      if midTile and midTile.piece and midTile.piece.color == getOpponentColor(piece.color):
        midTile.piece = None # Capture the opponent's piece
        return True
    else:
      return abs(dx) == tileSize and abs(dy) == tileSize
  if piece.color == red:
    if dy < 0:
      if abs(dx) == tileSize * 2 and abs(dy) == tileSize * 2:
        midY = (targetTile.pos.x + sourceTile.pos.x) // 2
        midX = (targetTile.pos.y + sourceTile.pos.y) // 2
        midTile = board[int(midX // tileSize)][int(midY // tileSize)]
        if midTile and midTile.piece and midTile.piece.color == black:
          midTile.piece = None
          return True
      else:
        return abs(dx) == tileSize and abs(dy) == tileSize
  if piece.color == black:
    if dy > 0:
      if abs(dx) == tileSize * 2 and abs(dy) == tileSize * 2:
        midY = (targetTile.pos.x + sourceTile.pos.x) // 2
        midX = (targetTile.pos.y + sourceTile.pos.y) // 2
        midTile = board[int(midX // tileSize)][int(midY // tileSize)]
        if midTile and midTile.piece and midTile.piece.color == red:
          midTile.piece = None
          return True
      else:
        return abs(dx) == tileSize and abs(dy) == tileSize
  return False

# Function to check if a player has won the game
def checkWin(playerColor, board):
  opponentColor = getOpponentColor(playerColor)
  for row in board:
    for tile in row:
      if tile.piece and tile.piece.color == opponentColor:
        return None # The opponent still has pieces, so the game continues
  return playerColor  # The player has won if there are no opponent pieces left


# Function to check if a player has any legal moves left
def hasLegalMoves(playerColor, board):
  for row in board:
    for tile in row:
      if tile.piece and tile.piece.color == playerColor:
        if canMove(tile, board):
                 return True  # The player has at least one legal move
    return False  # The player has no legal moves left

def canMove(sourceTile, board):
  from game_logic.tile import findTile
  dx = [tileSize, -tileSize]
  dy = [tileSize, -tileSize]
  
  for dxi in dx:
    for dyi in dy:
      newX = sourceTile.pos.x + dxi
      newY = sourceTile.pos.y + dyi
      targetTile = findTile(newX, newY, board)
      if isValidDropArea(sourceTile, targetTile):
        return True
  return False

# Function to check if the game is in a stalemate (a draw)
def isStalemate(playerColor, board):
  return not hasLegalMoves(playerColor, board)

# Function to get the opponent's color based on the player's color
def getOpponentColor(playerColor):
  return red if playerColor == black else black

# Function to get all possible moves for a player on the current board
def get_all_possible_moves(board, color):
    from game_logic.piece import get_all_pieces, get_piece_moves, simulate_move
    from game_logic.board import createBoardCopy
    # Generates all legal moves for the given player.
    moves = []
    for piece in get_all_pieces(board, color):
        valid_moves = get_piece_moves(board, piece.pos)
        for move in valid_moves:
            temp_board = createBoardCopy(board)
            temp_piece = temp_board[move[0][0]][move[0][1]].piece
            new_board = simulate_move(temp_piece, board, move)
            moves.append(new_board)
    return moves

def game_over(board):
    # Checks if the game is over.
    # Returns True if a player has no pieces left or cannot make any legal moves.
    black_has_pieces, red_has_pieces = False, False
    black_can_move, red_can_move = False, False

    for row in board:
        for tile in row:
            if tile.piece:
                if tile.piece.color == black:
                    black_has_pieces = True
                    if canMove(tile, board):
                        black_can_move = True
                else:
                    red_has_pieces = True
                    if canMove(tile, board):
                        red_can_move = True

    return not (black_has_pieces and black_can_move) or not (red_has_pieces and red_can_move)