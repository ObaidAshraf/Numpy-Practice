import numpy as np

chess_board = np.ones(64, dtype='i').reshape(8, 8)
chess_board[::2, 1::2] = 0
chess_board[1::2, ::2] = 0
print(chess_board)
