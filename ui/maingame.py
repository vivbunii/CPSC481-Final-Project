# This code initializes the Pygame framework, sets up the game, handles user input, and contains the main game loop. 

import sys, os, copy
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION
from ui.game_view import board, display, screenSize, pieceSize
from game_logic.board import populateBoard, printBoard, createBoardCopy
from game_logic.tile import createTileCopy
from algorithm.ai_utils import checkingKinging, isValidDropArea, getOpponentColor, checkWin, isStalemate
from algorithm.minimax import minimax
from ui.colors import white, black, red, colors
import pygame

# Initialize Pygame
pygame.init()

# Initialize game-related variables and fonts
selectedPiece = None
sourceTile = None
copyTile = None
targetTile = None
selectedPiecePos = pygame.Vector2(0, 0)
selectedPieceOffset = pygame.Vector2(-pieceSize // 2, -pieceSize // 2)
pygame.font.init()
currentPlayerColor = red
chessFont = pygame.sysfont.SysFont('dejavuserif', 36)

# Populate the game board with initial pieces and tiles
populateBoard()

# Print initial debugging information
print("Selected Piece:", selectedPiece)
print("Source Tile:", copyTile.pos if copyTile else None)
print("Target Tile:", targetTile.pos if targetTile else None)

printBoard(board)

# Main game loop
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
      os.system('clear')
      pos = pygame.mouse.get_pos()
      for row in board:
        for tile in row:
          if tile.rect.collidepoint(pos):
            if not selectedPiece:
              if tile.piece and tile.piece.color == currentPlayerColor:
                sourceTile = tile
                copyTile = createTileCopy(tile)
                tile.piece = None
                selectedPiece = copyTile.piece
                selectedPiecePos = pygame.Vector2(
                  pos[0] - selectedPieceOffset.x,
                  pos[1] - selectedPieceOffset.y
                )
            else:
              targetTile = tile
              if isValidDropArea(copyTile, targetTile):
                targetTile.piece = selectedPiece
                checkingKinging(selectedPiece, targetTile)
                print("Selected Piece:", selectedPiece)
                print("Source Tile:", copyTile.pos if copyTile else None)
                print("Target Tile:", targetTile.pos if targetTile else None)
                print("Piece moved successfully!")
                targetTile = None
                selectedPiece = None  
                copyTile.piece = None
                winner = checkWin(currentPlayerColor, board)
                if winner:
                    text = f"{colors[currentPlayerColor]} wins!"
                    textRender = chessFont.render(text, True, white)
                    textRect = textRender.get_rect(center = (screenSize // 2, screenSize // 2))
                    display.blit(textRender, textRect)
                    pygame.display.flip()
                    pygame.time.wait(5000)
                    pygame.quit()
                    sys.exit()
                currentPlayerColor = getOpponentColor(currentPlayerColor)
                if isStalemate(currentPlayerColor, board):
                  text = "Stalemate! The game is a draw."
                  textRender = chessFont.render(text, True, white)
                  textRect = textRender.get_rect(center = (screenSize // 2, screenSize // 2))
                  display.blit(textRender, textRect)
                  pygame.display.flip()
                  pygame.time.wait(5000)
                  pygame.quit()
                  sys.exit()
                if currentPlayerColor == black:
                    new_board = createBoardCopy(board)
                    value, new_board = minimax(new_board, 5, True, currentPlayerColor)
                    if new_board:
                      board = new_board
                    currentPlayerColor = getOpponentColor(currentPlayerColor)
                # printBoard(board)
              else:
                sourceTile.piece = selectedPiece
                print("Invalid move. Piece returned to its source.")
              selectedPiece = None
              copyTile = None
      print("Selected Piece:", selectedPiece)
      print("Source Tile:", copyTile.pos if copyTile else None)
      print("Target Tile:", targetTile.pos if targetTile else None)
    elif event.type == MOUSEMOTION:
      if selectedPiece:
          pos = pygame.mouse.get_pos()
          selectedPiecePos = pygame.Vector2(
            pos[0] - selectedPieceOffset.x,
            pos[1] - selectedPieceOffset.y
          )
  for row in board:
    for tile in row:
      tile.draw()
  if selectedPiece:
    display.blit(selectedPiece.icon, selectedPiecePos + selectedPieceOffset * 3)
  pygame.display.update()