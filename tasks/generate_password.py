#!/usr/bin/env python
import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-L", "--length", type=int, default=16,
                   help="Length of the output random password")
args = parser.parse_args()
print ( ''.join(random.choice('abcdef' + string.digits) for _ in range(args.length)) )
