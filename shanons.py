#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:12:43 2019

@author: william Keilsohn
"""
# Import packages:
import math

# Insert Data:
data = [4, 1, 8, 4, 16, 1]

# Calculate Relative Abundance:
relative_Abun = data[:]
total = sum(relative_Abun)
relative_Abun = [i / total for i in relative_Abun]

# Calculate Natural logs
ln_relative = [math.log(j) for j in relative_Abun]

# Calculate Rel_Ab. X ln Rel_Ab:
ln_multiple = []
for x in range(len(data)):
    val = ln_relative[x] * relative_Abun[x]
    ln_multiple.append(val)

# Find diversity index:
Div_ind = (-1) * sum(ln_multiple)

# Produce Species Evenness:
even = Div_ind / math.log(len(data))

# Print results:
print(str(even))

