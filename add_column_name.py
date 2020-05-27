# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:38:44 2020

@author: lucas
"""

import pandas as pd

df = pd.read_csv("KDD_full.csv", sep = ',', header = None)

df.rename(columns={0: 'duration', 1: 'protocol_type', 2: 'service', 3: 'src_bytes', 4: 'dst_bytes ', 5:'flag', 6:'land', 7: 'wrong_fragment', 8:'urgent', 9:'hot', 10:'num_failed_logins', 11:'logged_in', 12:'num_compromised', 13:'root_shell ', 14:'su_attempted', 15:'num_root', 16:'num_file_creations', 17:'num_shells', 18:'num_access_files', 19:'num_outbound_cmds', 20:'is_hot_login', 21:'is_guest_login', 22:'count', 23:'serror_rate', 24:'rerror_rate', 25:'same_srv_rate', 26:'diff_srv_rate', 27:'srv_count', 28:'srv_serror_rate', 29:'srv_rerror_rate', 30: 'srv_diff_host_rate'}, inplace=True)


df.to_csv('KDD_with_name.csv', index=False) # save to new csv file




df_with_column_name = pd.read_csv("KDD_with_name.csv")


df_with_column_name.drop(['num_failed_logins','logged_in', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_hot_login', 'is_guest_login'], axis = 1, inplace = True)

list_service_del = ['eco_i', 'klogin', 'red_i', 'aol', 'uucp', 'stmp', 'gopher']


for service_name in list_service_del:
    df_with_column_name.drop(df_with_column_name[df_with_column_name.service == service_name].index, inplace=True)
print(df_with_column_name.service.unique())



