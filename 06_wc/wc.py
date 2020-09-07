#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-07
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        help='Input file(s)',
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_words, total_bytes = 0, 0, 0
    for fh in args.files:
        num_lines, num_words, num_bytes = 0, 0, 0
        for one_line in fh:
            num_lines += 1
            num_words += len(one_line.split())
            num_bytes += len(one_line)
            
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
        
    if len(args.files) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


        # --------------------------------------------------
if __name__ == '__main__':
    main()
