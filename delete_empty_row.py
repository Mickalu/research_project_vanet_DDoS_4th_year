# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:16:03 2020

@author: lucas
"""

with open('KDD.csv') as input, open('demo005.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)