#!/usr/bin/env python
"""reducer.py"""

import sys

global_mean = 0
global_counter = 0
global_var = 0

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    counter, mean, var = [int(x) for x in line.split()]

    new_counter = counter + global_counter
    new_mean = (counter * mean + global_counter * global_mean) / (counter + global_counter)
    new_var = ((counter * var + global_counter * global_var) / (counter + global_counter) +
               counter * global_counter * ((mean - global_mean) / (counter + global_counter)) ** 2)

    global_counter = new_counter
    global_mean = new_mean
    global_var = new_var

print(f'{global_mean} {global_var}')
