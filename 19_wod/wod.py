#!/usr/bin/env python3
"""
Author : ncapps
Date   : 2020-09-14
Purpose: Create Workout Of (the) Day (WOD)
"""

import argparse
import random
import csv
import io
import re
from pprint import pprint
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='CSV input file of exercises',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    easy = args.easy
    exercises = read_csv(args.file)

    wod = [(name,
            int(random.randint(low, high)/2)
            if easy else random.randint(low, high))
           for name, low, high in random.sample(exercises, k=args.num)]

    print(tabulate(wod, headers=('Exercise', 'Reps')))


# --------------------------------------------------


def read_csv(fh):
    """Read the CSV input"""
    reader = csv.DictReader(fh, delimiter=',')
    reps = re.compile(r'(\d+)-(\d+)')

    return [(rec['exercise'], *map(int, reps.match(rec['reps']).groups()))
            for rec in reader]


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
