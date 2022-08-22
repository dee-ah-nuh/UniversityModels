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


# def gsheet_to_df(book,sheet,gspread):
#     wb=gspread.open(book)
#     ws=wb.worksheet(sheet)
#     data=ws.get_all_values()
#     headers=data.pop(0)
#     df=pd.DataFrame(data,columns=headers)
#     return df

# sa = gspread.service_account(filename='universitymodelssheetscreds.json')
# sheet = sa.open("Leads Billing Conversion")
# idgs = '1bXJtdTW9Dqz02MILbaedaEv8AUQ89hKUoW_gO1xOGEw'
# leadsandGrits = gsheet_to_df("Leads Billing Conversion", "Leads&Grits", sa)
# leadsandGrits.fillna(0)
# worksheet = sheet.worksheet("Leads&Grits")
# print("Rows:", worksheet.row_count)
# print("Columns:", worksheet.col_count)


billingdf= pd.read_csv("C:/Users/BEEMO/Downloads/Operation Graduate leads 2022-08-22 23-34 (1).csv")
