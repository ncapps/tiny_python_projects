#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-07
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    lookup = {line[0].upper(): line.rstrip()
              for line in args.file}

    for a_letter in args.letter:
        print(lookup.get(a_letter.upper(), f'I do not know "{a_letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
