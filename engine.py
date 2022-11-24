"""
This file is responsible for storing all the information about the current state of a chess game.
It will also be responsible for determining valid moves at the current state.
It will also keep moves log.
"""


class GameState:
    def __init__(self):
        """
        The board is a 8x8 2 dimension list
        Each element of the list has two characters
        The first element represents the color 'b' for black and 'w' for white
        The second element represents the type Pawn, Bishop, Rook, Knight(N), King and Queen
        The '--' are empty spaces

        """
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.white_to_move = True
        self.log_moves = []

    def makeMove(self, move):
        self.board[move.start_row][move.start_column] = "--"
        self.board[move.end_row][move.end_column] = move.piece_moved
        self.log_moves.append(move)  # Log the move
        self.white_to_move = not self.white_to_move


class Move:
    # mapping our board to match the chess board notation
    ranks_to_rows = {'1': 7, '2': 6, '3': 5, '4': 4,
                     '5': 3, '6': 2, '7': 0}
    rows_to_rank = {
        v: k
        for k, v in ranks_to_rows.items()
    }
    files_to_columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                        'e': 4, 'f': 5, 'g': 6, 'h': 7}

    columns_to_files = {
        v: k
        for k, v in files_to_columns.items()
    }

    # So we make this class to make moves
    # It starts with a start quare and then the player plays and then the end square
    # We also pass board to check the validity of the move
    # We now have all the records of a player's move in one place
    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_column = start_square[1]
        self.end_row = end_square[0]
        self.end_column = end_square[1]
        self.piece_moved = board[self.start_row][self.start_column]
        self.piece_captured = board[self.end_row][self.end_column]

    def get_chess_notations(self):
        return self.get_rank_files(self.start_row, self.start_column) + self.get_rank_files(self.end_row,
                                                                                            self.end_column)

    def get_rank_files(self, rows, columns):
        return self.columns_to_files[columns] + self.rows_to_rank[rows]
