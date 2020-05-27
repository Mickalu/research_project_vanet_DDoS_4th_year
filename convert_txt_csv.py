# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:54:05 2020

@author: lucas
"""

import csv

with open("KDD.txt", 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    
    with open('KDD.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
