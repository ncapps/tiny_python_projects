#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-15
Purpose: Interactive Tic-Tac-Toe
"""

import argparse
import re
from typing import List, NamedTuple, Optional


# --------------------------------------------------
class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None

# --------------------------------------------------


def main() -> None:
    """Make a jazz noise here"""

    state = State()

    while True:
        #  Print a special sequence that most terminals will interpret
        # as a command to clear the screen.
        print("\033[H\033[J")
        print(format_board(state.board))

        if state.error:
            print(state.error)
        elif state.winner:
            print(f'{state.winner} has won!')
            break
    
        state = get_move(state)

        if state.quit:
            print('You lose, loser!')
            break
        elif state.draw:
            print("All right, we'll call it a draw")
            break


# --------------------------------------------------
def get_move(state: State) -> State:
    """Get the player's move"""
    player = state.player
    cell = input(f'Player {state.player}, what is your move? [q to quit]:')

    if cell == 'q':
        return state._replace(quit=True)

    if not re.search(r'^[1-9]{1}$', cell):
        return state._replace(error=f'Invalid cell "{cell}", please use 1-9')

    cell_num = int(cell)
    if state.board[cell_num - 1] in 'XO':
        return state._replace(error=f'Cell "{cell}" already taken')

    board = state.board
    board[cell_num - 1] = player
    return state._replace(board=board,
                          player='O' if state.player == 'X' else 'X',
                          winner=find_winner(board),
                          draw='.' not in board,
                          error=None)


# --------------------------------------------------
def format_board(board: List[str]) -> str:
    """Format the board"""

    bar = '-------------'
    cells = [str(index) if cell == '.' else cell
             for index, cell in enumerate(board, start=1)]
    template = '| {} | {} | {} |'
    return '\n'.join([
        bar,
        template.format(*cells[:3]),
        bar,
        template.format(*cells[3:6]),
        bar,
        template.format(*cells[6:]),
        bar
    ])


# --------------------------------------------------
def find_winner(board: List[str]) -> str:
    """Return the winner"""
    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for combo in winning:
        group = [board[i] for i in combo]
        for player in 'XO':
            if all(x == player for x in group):
                return player

    return ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
