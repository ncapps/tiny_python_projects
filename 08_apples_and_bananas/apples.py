#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-07
Purpose: Apples and bananas
"""

import argparse
import os
import io

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel(s) allowed',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices='aeiou')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, 'rt')
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    trans = str.maketrans("aeiouAEIOU", vowel*5 + vowel.upper()*5)

    for line in args.text:
        print(f'{line.translate(trans)}')
    args.text.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
