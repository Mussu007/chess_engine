"""
This is the main driver file. This is responsible for handling user inputs and displaying current
GameState object.
"""

import pygame as p
from engine import GameState

# Defining global variables
WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Initializing a global dictionary of images. This will be called exactly once in the main
We can adapt later to change skins
"""


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


"""
This will be our main driver for our code.
It will handle user input and updating graphics
"""


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    game_state = GameState()
    load_images()

    # To run the game on loop and once the user quit, flip the table
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            draw_game_state(screen, game_state)
            clock.tick(MAX_FPS)
            p.display.flip()


"""
Responsible for all the graphics for the current game state
We first call the board with the draw_game_state
We draw the board using the draw_board function
We then the draw the pieces with the draw_pieces function
"""


def draw_game_state(screen, game_state):
    draw_board(screen)  # Draws squares on the board
    draw_pieces(screen, game_state.board)  # Draw pieces on top of the square


# Draws the square pieces on the board
def draw_board(screen):
    color_light = p.Color("burlywood1")
    color_dark = p.Color("chocolate4")
    """
    So in a chess board the top left square is always light colored
    So, if we add the co-ordinates, for example, top left will be 0,0
    The light square will always be even and hence the dark square will always be odd
    """

    count_ = 0
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if count_ % 2 == 0:
                p.draw.rect(screen, color_light, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                p.draw.rect(screen, color_dark, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            count_ += 1
        # since there is an even number of squares go back one value
        count_ -= 1


# Draws the pieces on the board using the current game_state.board
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


if __name__ == "__main__":
    main()
