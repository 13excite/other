#!/usr/bin/python

import os
import re
import subprocess as sp
import time
file = './data/test'
REGEXP = 'Testing'

def tailer(file, regexp):
    fp = open(file, 'r')
    while True:
        new = fp.readline()
        if re.search(regexp, new):
            print(new)
        else:
            time.sleep(0.5)

def main():
    tailer(file, REGEXP)

if __name__ == '__main__':
    main()
