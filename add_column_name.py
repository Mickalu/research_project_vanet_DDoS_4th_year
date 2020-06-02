# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:38:44 2020

@author: lucas
"""

import pandas as pd

df = pd.read_csv("KDD_full.csv", sep = ',', header = None)

# Give name to the columns
df.rename(columns={0: 'duration', 1:'protocol_type', 2:'service', 3:'flag', 4:'src_bytes', 5:'dst_bytes ',
                   6:'land', 7:'wrong_fragment', 8:'urgent', 9:'hot', 10:'num_failed_logins', 11:'logged_in',
                   12:'num_compromised', 13:'root_shell ', 14:'su_attempted', 15:'num_root', 16:'num_file_creations',
                   17:'num_shells', 18:'num_access_files', 19:'num_outbound_cmds', 20:'is_hot_login', 21:'is_guest_login',
                   22:'count', 23:'srv_count', 24:'serror_rate', 25:'srv_serror_rate', 26:'rerror_rate', 27:'srv_rerror_rate',
                   28:'same_srv_rate', 29:'diff_srv_rate', 30:'srv_diff_host_rate', 31:'dst_host_count', 32:'dst_host_srv_count',
                   33:'dst_host_same_src_rate', 34:'dst_host_srv_rate', 35:'dst_host_same_srv_port_rate', 36:'dst_host_srv_diff_host_rate',
                   37:'dst_host_serror_rate', 38:'dst_host_srv_serror_rate', 39:'dst_host_rerror_rate', 40:'dst_host_srv_rerror_rate',
                   41:'attack_name'}, inplace=True)

# Save in a new csv file
df.to_csv('KDD_with_name.csv', index=False) 




df_with_column_name = pd.read_csv("KDD_with_name.csv")

# Delete the last column
df_with_column_name.drop(df_with_column_name.columns[-1], axis=1, inplace=True)

# And the useless columns
df_with_column_name.drop(['num_failed_logins','logged_in', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_hot_login', 'is_guest_login'], axis = 1, inplace = True)

list_service_del = ['aol', 'eco_i', 'efs', 'gopher', 'hostnames', 'klogin', 'login', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'nntp', 'pop_2', 'pop_3', 'red_i', 'stmp', 'sunrpc', 'tftp_u', 'uccp', 'uccp_path', 'X11', 'Z39_50']


for service_name in list_service_del:
    df_with_column_name.drop(df_with_column_name[df_with_column_name.service == service_name].index, inplace=True)
print(df_with_column_name.service.unique())
print(df_with_column_name)



