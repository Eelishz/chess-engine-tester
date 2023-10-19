import sys
import chess.pgn
import json
from random import randint

def main():
    FILE_NAME = sys.argv[-3]
    N_GAMES = int(sys.argv[-2])
    OUT_FILE = sys.argv[-1]

    pgn = open(FILE_NAME)
    
    data = []

    for i in range(N_GAMES):
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        board = game.board()
        final_position = randint(0, sum(1 for move in game.mainline_moves()))
        for (i, move) in enumerate(game.mainline_moves()):
            if i >= final_position:
                break
            board.push(move)
        
        data.append(board.fen())

    for row in data:
        print(row)

    json_object = json.dumps(data, indent=4)

    with open(OUT_FILE, "w") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    main()