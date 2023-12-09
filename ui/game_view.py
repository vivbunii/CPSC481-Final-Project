import pygame
from ui.colors import red

# Set the size of the game screen
screenSize = 600
display = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption('Checkers') # Set the caption of the game window


# Calculate the size of each tile and the size of each game piece
tileSize = screenSize // 8 # Divide the screen size by 8 to determine tile size
pieceSize = tileSize // 2 - 5 # Calculate the size of each game piece

# Initialize an empty list to represent the game board
board = list()

# Load and scale images for red and black game pieces and crowns
redPiece = pygame.image.load("./assets/red.png")
redPiece = pygame.transform.scale(redPiece, (tileSize, tileSize))
blackPiece = pygame.image.load("./assets/black.png")
blackPiece = pygame.transform.scale(blackPiece, (tileSize, tileSize))
redCrown = pygame.image.load("./assets/redCrown.png")
redCrown = pygame.transform.scale(redCrown, (tileSize, tileSize))
blackCrown = pygame.image.load("./assets/blackCrown.png")
blackCrown = pygame.transform.scale(blackCrown, (tileSize, tileSize))