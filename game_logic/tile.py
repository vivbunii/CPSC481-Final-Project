import pygame
from ui.game_view import tileSize, display

# Define the Tile class
class Tile():
  def __init__(self, color, piece, pos):
    self.color = color  # Color of the tile (e.g., black or white)
    self.piece = piece  # Piece on the tile (if any)
    self.pos = pos      # Position of the tile (x, y)
    self.rect = pygame.Rect(self.pos.x, self.pos.y, tileSize, tileSize)
  def draw(self):
    # Draw the tile as a colored rectangle
    pygame.draw.rect(display, self.color, self.rect)
    if self.piece:
      # If there is a piece on the tile, draw the piece's icon
      display.blit(self.piece.icon, self.rect.topleft)

# Create a copy of a Tile object
def createTileCopy(tile):
  return Tile(tile.color, tile.piece, tile.pos)

# Find a tile on the game board based on its coordinates (x, y)
def findTile(x, y, board):
  for row in board:
    for tile in row:
      if tile.rect.collidepoint(x, y):
        return tile
  return None # Return None if no tile is found at the specified coordinates