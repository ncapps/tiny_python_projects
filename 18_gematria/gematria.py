#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-14
Purpose: Gematria
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, 'rt').read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(' '.join(word2num(word)
                       for word in line.split()))


# --------------------------------------------------
def word2num(word):
    """Returns numeric value for word"""
    word = re.sub('[^A-Za-z0-9]', '', word)
    return str(sum(ord(char) for char in word))


# --------------------------------------------------
def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
