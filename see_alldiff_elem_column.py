# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:24:23 2020

@author: lucas
"""


import pandas as pd

FILE_NAME = "KDD_full.csv"

df = pd.read_csv(FILE_NAME)#KDD_full n'a pas de ligne vide

print(df.columns, "\n")

print

for i in df.columns:
    print("\n", i, " : ", df[i].dtypes)
    
print("\n tcp[2] : ", df['tcp'].unique())
print("\n ftp_data[3]", df['ftp_data'].unique(), len(df['ftp_data'].unique()))
print("\n SF[4]", df['SF'].unique(),len( df['SF'].unique() ))
print("\n normal[avd]", df['normal'].unique(), len(df['normal'].unique()))

