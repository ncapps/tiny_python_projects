#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-15
Purpose: Tic-Tac-Toe
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Play Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='board',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='player',
                        type=str,
                        choices='XO',
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    args = parser.parse_args()

    if bool(args.player) != bool(args.cell):
        parser.error('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if args.player and args.cell and args.board[args.cell-1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = list(args.board)

    if args.player and args.cell:
        board[args.cell - 1] = args.player

    print(format_board(board))
    winner = find_winner(board)
    print(f'{winner} has won!' if winner else 'No winner')


# --------------------------------------------------
def format_board(board):
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
def find_winner(board):
    """Return the winner"""
    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for combo in winning:
        group = [board[i] for i in combo]
        for player in 'XO':
            if all(x == player for x in group):
                return player


# --------------------------------------------------
if __name__ == '__main__':
    main()
