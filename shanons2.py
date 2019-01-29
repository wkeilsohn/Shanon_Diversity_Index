#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:34:48 2019

@author: william keilsohn
"""

# Import Packages:
from math import log

# Collect user data:
data = []
val1 = int(input('How many individuals are there of the first species?: '))
data.append(val1)
print('\n')

# Ask about additional data:
def answerChecker(string):
    if string in ['Y', 'y', 'yes', 'Yes', 'YES']:
        return True
    else:
        return False

collect_data = True

while collect_data == True:
    quest_user = input('Is there any more species/groups?: ')
    if answerChecker(quest_user) == True:
        val2 = int(input('Please enter the number of individuals: '))
        data.append(val2)
        print('\n')
        print('Thank you')
        print('\n')
        continue
    else:
        print('\n')
        break

# Calculate the diversity index:
def shan(lst):
    total = sum(lst)
    rel = [i / total for i in lst]
    ln_rel = [log(j) for j in rel]
    ln_mult = []
    for x in range(len(lst)):
        val = ln_rel[x] * rel[x]
        ln_mult.append(val)
    Div_ind = (-1) * sum(ln_mult)
    even = Div_ind / log(len(lst))
    return even, Div_ind

# Return the user request:
print('The Shanon\'s diversity index for the provided sample is: ', end = '')
print(str(shan(data)[1]), 'and an evenness of', shan(data)[0])
    