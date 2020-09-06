#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-06
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_text = args.input_text
    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    output = ''.join(jumper.get(a_char, a_char)
                     for a_char in input_text)

    print(f'{output}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
