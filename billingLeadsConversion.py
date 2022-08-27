# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 18:08:06 2022

@author: BEEMO
"""

import re
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import gspread
import df2gspread as d2g



# set up credentials via cloud console
#save file as json in same directory
#import sheets to df module from UniversityModels
#make google sheet a df
#apply EDA


def gsheet_to_df(book,sheet,gspread):
    wb=gspread.open(book)
    ws=wb.worksheet(sheet)
    data=ws.get_all_values()
    headers=data.pop(0)
    df=pd.DataFrame(data,columns=headers)
    return df

sa = gspread.service_account(filename='universitymodelssheetscreds.json')
sheet = sa.open("Leads Billing Conversion")
idgs = '1bXJtdTW9Dqz02MILbaedaEv8AUQ89hKUoW_gO1xOGEw'
leadsandGrits = gsheet_to_df("Leads Billing Conversion", "Data", sa)
leadsandGrits.fillna(0)
worksheet = sheet.worksheet("Data")

print("Rows:", worksheet.row_count)
print("Columns:", worksheet.col_count)

#119 columns, 1514 rows // 922 were DegreeSearch
df = leadsandGrits
df.drop_duplicates(subset=['id', 'primary_contact_primary_phone'] , inplace=True)

