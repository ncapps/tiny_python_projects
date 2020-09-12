#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-11
Purpose: Make rhyming "words"
"""

import argparse
import re
import string

CONSONANTS = ''.join(char
                     for char in string.ascii_lowercase
                     if char not in 'aeiou')

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    prefixes = sorted(['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl',
                       'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn',
                       'sp', 'st', 'sw', 'th', 'tr', 'tw', 'thw', 'wh',
                       'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr',
                       'squ', 'str', 'thr', *CONSONANTS])
    start, stem = stemmer(word)

    if stem:
        print('\n'.join(a_prefix + stem
                        for a_prefix in prefixes
                        if a_prefix != start))

    else:
        print(f'Cannot rhyme "{word}"')


# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""
    word = word.lower()
    pattern = (
        f'([{CONSONANTS}]+)?'
        '([aeiou])'
        '(.*)'
    )
    match = re.match(pattern, word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return p1, p2 + p3

    return word, ''

# --------------------------------------------------


def test_stemmer():
    """ Test stemmer """
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
