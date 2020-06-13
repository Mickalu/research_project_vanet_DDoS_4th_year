# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:26:30 2020

@author: Thomas
"""

##### LIBRARIES ##############################################################

import csv
import pandas as pd

##### FUNCTIONS ##############################################################
def convert_txt_to_csv():
    with open('KDD.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        
        with open('KDD.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)
    
    
def delete_empty_row():    
    with open('KDD.csv') as input, open('KDD_structured.csv', 'w') as output:
        non_blank = (line for line in input if line.strip())
        output.writelines(non_blank)
  
        
def change_string_int_value(df, colonne):
    for indx, val in enumerate(sorted(df[colonne].unique())):
        df[colonne].replace(to_replace = val, value = indx, inplace = True)


def clean_database():
    """Treatment to organize the database for exploitation"""
    # Open the CSV file
    df = pd.read_csv('KDD_structured.csv', sep = ',', header = None)

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

    # Delete the last column
    df.drop(df.columns[-1], axis=1, inplace=True)

    # And the useless columns
    df.drop(['num_failed_logins','logged_in', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 
             'is_hot_login', 'is_guest_login'], axis = 1, inplace = True)
    
    # List for our attack class 
    dos =  ['neptune', 'teardrop', 'smurf', 'pod', 'back', 'land']
    attack = ['warezclient', 'ipsweep', 'portsweep', 'nmap', 'satan', 'guess_passwd', 'ftp_write', 'multihop', 'rootkit', 
              'buffer_overflow', 'imap', 'warezmaster', 'phf', 'loadmodule', 'spy', 'perl']

    # Replace attack name by class
    df['attack_name'].replace(to_replace = 'normal', value = 0, inplace = True)
    df['attack_name'].replace(to_replace = dos, value = 1, inplace = True)
    df['attack_name'].replace(to_replace = attack, value = 2, inplace = True)
    
    # Change string value in the dataset in int value (for ML)
    change_string_int_value(df, 'protocol_type')
    change_string_int_value(df, 'service')
    change_string_int_value(df, 'flag')
    
    # Save in a new CSV file
    df.to_csv('KDD_clean_database.csv', index=False)


##### MAIN ###################################################################   
convert_txt_to_csv()
delete_empty_row()
clean_database()

df = pd.read_csv('KDD_clean_database.csv')

# Check if we have empty data
print("\nNumber of NaN elements (rows) by columns :\n", df.isnull().sum()) 
# Result : the database is complete
