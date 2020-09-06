#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-06
Purpose: Howler
"""

import argparse
import os

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    input_text = args.text
    outfile = args.outfile

    if os.path.isfile(input_text):
        with open(input_text, 'rt') as in_fh:
            output_text = [one_line.upper()
                           for one_line in in_fh]
    else:
        output_text = [input_text.upper()]

    if outfile:
        with open(outfile, 'wt') as out_fh:
            for one_line in output_text:
                out_fh.write(one_line)
    else:
        for one_line in output_text:
            print(f'{one_line}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
