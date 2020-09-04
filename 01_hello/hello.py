#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-04
Purpose: Say hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        default='World')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    name = args.name
    print(f'Hello, {name}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
