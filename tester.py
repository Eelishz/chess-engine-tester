import chess
from chess.engine import SimpleEngine
import sys
import os
import json
from tqdm import tqdm

def load_positions(path: str) -> list[chess.Board]:
    file = open(path)
    games = json.load(file)
    return [chess.Board(fen=fen) for fen in games]
    
def main():
    POSITIONS = load_positions(sys.argv[-1])
    A_ENGINE_PATH = sys.argv[-3]
    B_ENGINE_PATH = sys.argv[-2]

    a_engine = SimpleEngine.popen_uci(A_ENGINE_PATH)
    b_engine = SimpleEngine.popen_uci(B_ENGINE_PATH)

    wins = 0
    draws = 0
    losses = 0

    for board in tqdm(POSITIONS):
        a_team = board.turn
        turn = True
        try:
            while not board.is_game_over():
                if turn:
                    result = a_engine.play(board, chess.engine.Limit(time=0.1))
                    board.push(result.move)
                else:
                    result = b_engine.play(board, chess.engine.Limit(time=0.1))
                    board.push(result.move)
                turn != turn
            outcome = board.outcome()
        except Exception as e:
            continue
        if outcome.winner is None:
            draws += 1
        elif outcome.winner == a_team:
            wins += 1
        else:
            losses += 1
        
    print(wins, draws, losses)

if __name__ == '__main__':
    main()