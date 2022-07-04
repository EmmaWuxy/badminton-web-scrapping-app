import os
import pandas as pd

def generate_excel(df, file_name):
    ''' Generate an excel file in current working directory'''
    try:
        df.to_excel(file_name)
    except PermissionError:
        print('Permission error when trying to write to output.xls... It might be caused by ' + file_name + 'open on your desktop.')
    else:
        print('Work done successfully. Please view {} for results.'.format(os.getcwd() + '\\' + file_name))
