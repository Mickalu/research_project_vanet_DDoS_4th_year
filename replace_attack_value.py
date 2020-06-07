# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:46:12 2020

@author: lucas
"""


import pandas as pd

df = pd.read_csv("KDD_with_name.csv")

DDoS =  ['neptune', 'teardrop', 'smurf', 'pod', 'back', 'land']
attack = ['warezclient', 'ipsweep', 'portsweep', 'nmap', 'satan', 'guess_passwd', 'ftp_write', 'multihop', 'rootkit', 'buffer_overflow', 'imap', 'warezmaster', 'phf', 'loadmodule', 'spy', 'perl']


df['attack_name'].replace(to_replace = DDoS, value = 'DDoS', inplace = True)
df['attack_name'].replace(to_replace = attack, value = 'attack', inplace = True)

df.to_csv('KDD_attack_name_change.csv', index=False) 

