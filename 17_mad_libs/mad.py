#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-13
Purpose: Mad Libs
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        nargs='*',
                        type=str,
                        default=None)

    return parser.parse_args()


# -------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()
    blanks = re.findall('(<([^<>]+)>)', text)

    if not blanks:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    for placeholder, pos in blanks:
        article = 'an' if pos[0].lower() in 'aeiou' else 'a'
        a_word = inputs.pop(0) if inputs else input(
            f'Give me {article} {pos}: ')
        text = re.sub(placeholder, a_word, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
