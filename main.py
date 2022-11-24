"""
This is the main driver file. This is responsible for handling user inputs and displaying current
GameState object.
"""

import pygame as p
from engine import GameState
from engine import Move

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

    # This will keep track of last click of the user
    # This is above the for loops as we are going to use this tuple to store data (row and column)
    # No square is selected initially
    square_selected = ()

    # This will keep track of where the player has clicked
    # This will have two tuples stored. Eg: [(6, 4), (4, 4)]

    player_click = []

    # To run the game on loop and once the user quit, flip the table
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # We click the piece and it moves
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                # (x,y) location of the mouse
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE

                # To check if the user has clicked the same square twice
                # If they do select the same square, we empty the tuple i.e. deselects
                # Also reset the player_clicks
                if square_selected == (row, col):
                    square_selected = ()
                    player_click = []
                else:
                    square_selected = (row, col)
                    player_click.append(square_selected)  # Append both first and second clicks

                if len(player_click) == 2:
                    move = Move(player_click[0], player_click[1], game_state.board)
                    print(move.get_chess_notations())  # Debugging purposes
                    game_state.makeMove(move)
                    square_selected = ()  # reset the user clicks
                    player_click = []

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
