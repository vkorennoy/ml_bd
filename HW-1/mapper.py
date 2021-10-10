#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
elements = []
counter = 0

for line in sys.stdin:
    counter += 1
    elements.append(int(line))

if counter > 1:
    mean = sum(elements) / counter
    var = sum([(x - mean) ** 2 for x in elements]) / (counter - 1)
else:
    mean = 0
    var = 0

print(f'{counter} {mean} {var}')
