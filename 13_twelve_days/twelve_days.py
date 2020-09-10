#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-10
Purpose: Twelve Days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()
    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = (verse(day) for day in range(1, args.num + 1))
    print("\n\n".join(verses), file=args.outfile)


# ---------------------------------------------------
def verse(day):
    """Create a version"""   
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
               'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts = ['partridge in a pear tree',
             'Two turtle doves',
             'Three French hens',
             'Four calling birds',
             'Five gold rings',
             'Six geese a laying',
             'Seven swans a swimming',
             'Eight maids a milking',
             'Nine ladies dancing',
             'Ten lords a leaping',
             'Eleven pipers piping',
             'Twelve drummers drumming']
    partridge = 'A' if day == 1 else 'And a'
    
    return '\n'.join([
        f'On the {ordinal[day-1]} day of Christmas,',
        f'My true love gave to me,',
        *[f'{gifts[index-1]},' for index in range(day, 1, -1)],
        f'{partridge} {gifts[0]}.'
    ])


# ---------------------------------------------------
def test_verse():
    """verse unit tests"""
    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
