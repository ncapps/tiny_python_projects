#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-15
Purpose: Password maker
"""

import argparse
import random
import re
import string

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    # First generate all passwords so that randomness can be tested
    passwords = [''.join(word for word in random.sample(words, args.num_words))
                 for _ in range(args.num)]

    if args.l33t:
        passwords = map(l33t, passwords)

    print('\n'.join(passwords))


# --------------------------------------------------
def clean(word):
    """Removes punctuation"""
    return re.sub('[^A-Za-z]', '', word)

# --------------------------------------------------


def ransom(word):
    """Randomly choose upper or lowercase letters"""

    return ''.join(char.upper() if random.choice([0, 1]) else char.lower()
                   for char in word)


# --------------------------------------------------
def l33t(word):
    """Return a l33ted word"""
    l33ter = {
        'a': '@',
        'A': '4',
        'O': '0',
        't': '+',
        'E': '3',
        'I': '1',
        'S': '5'
    }

    return ''.join(l33ter.get(a_char, a_char)
                   for a_char in ransom(word)) + random.choice(string.punctuation)


# --------------------------------------------------
if __name__ == '__main__':
    main()
