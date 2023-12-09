import pygame
from ui.game_view import tileSize, display  # Importing necessary modules and variables

# Tile class represents a game tile on the checkers board
class Tile():
    def __init__(self, color, piece, pos):
        self.color = color  # Tile color (black or white)
        self.piece = piece  # Piece (if any) on the tile
        self.pos = pos      # Position of the tile on the screen
        self.rect = pygame.Rect(self.pos.x, self.pos.y, tileSize, tileSize)  # Rectangular area for the tile

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)  # Draw the tile with its color
        if self.piece:  # If there is a piece on the tile
            display.blit(self.piece.icon, self.rect.topleft)  # Draw the piece's icon on the tile

# Function to create a copy of a tile
def createTileCopy(tile):
    return Tile(tile.color, tile.piece, tile.pos)

# Function to find a tile at specified coordinates (x, y) on the board
def findTile(x, y, board):
    for row in board:
        for tile in row:
            if tile.rect.collidepoint(x, y):  # Check if the coordinates are within the tile's rectangular area
                return tile  # Return the tile if found
    return None  # Return None if no tile is found at the specified coordinates

