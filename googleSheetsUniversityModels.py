# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:03:45 2022

@author: BEEMO
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:35:26 2022

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

#separate into dataframes
#sum the column values 
#finally append those column values to a new dataframe with new name 

def df_to_sheet(wbname,sheetname,df,gspread,*arg):
    #Open shet
    df=df.fillna('')
    wb=gspread.open(wbname)
    #Open tab
    ws=wb.worksheet(sheetname)
    if arg:
        if arg[0]==1:
            ws.clear()
        if arg[0]==2:
            ws.append_rows(df.values.tolist())
            return
    #Write the values
    ws.update([df.columns.values.tolist()] + df.values.tolist())


def gsheet_to_df(book,sheet,gspread):
    wb=gspread.open(book)
    ws=wb.worksheet(sheet)
    data=ws.get_all_values()
    headers=data.pop(0)
    df=pd.DataFrame(data,columns=headers)
    return df

sa = gspread.service_account(filename='universitymodelssheetscreds.json')
sheet = sa.open("University-Model")
idgs = '12s2slCTbXxj8n3Fszowloh3A7c85JRKqgCHrwTlRJwQ'

universityData = gsheet_to_df("University-Model", "UniversityData", sa)
universityData.fillna(0)
worksheet = sheet.worksheet('UniversityData')
print("Rows:", worksheet.row_count)
print("Columns:", worksheet.col_count)

df = universityData
df = df.fillna(0)


df2020=df.loc[:,['2020' in i for i in df.columns]]
df2020.astype(int)
df2019=df.loc[:,['2019' in i for i in df.columns]]
df2019.astype(int)
df2018=df.loc[:,['2018' in i for i in df.columns]]
df2018.astype(int)
df2017= df.loc[:,['2017' in i for i in df.columns]]
df2017.astype(int)
df2016= df.loc[:,['2016' in i for i in df.columns]]
df2016.astype(int)
df2015= df.loc[:,['2015' in i for i in df.columns]]
df2015.astype(int)
df2014= df.loc[:,['2014' in i for i in df.columns]]
df2014.astype(int)
df2013= df.loc[:,['2013' in i for i in df.columns]]
df2013.astype(int)
df2012= df.loc[:,['2012' in i for i in df.columns]]
df2012.astype(int)
df2011= df.loc[:,['2011' in i for i in df.columns]]
df2011.astype(int)
df2010= df.loc[:,['2010' in i for i in df.columns]]
df2010.astype(int)
df2009= df.loc[:,['2009' in i for i in df.columns]]
df2009.astype(int)
df2008= df.loc[:,['2008' in i for i in df.columns]]
df2008.astype(int)
df2007= df.loc[:,['2007' in i for i in df.columns]]
df2007.astype(int)
df2006= df.loc[:,['2006' in i for i in df.columns]]
df2006.astype(int)


# =============================================================================
# df2005= df.loc[:,['2005' in i for i in df.columns]]
# df2005.replace({'': 0}.astype(int)
# df2004= df.loc[:,['2004' in i for i in df.columns]]
# df2004.astype(int)
# df2003= df.loc[:,['2003' in i for i in df.columns]]
# df2003.astype(int)
# df2002= df.loc[:,['2002' in i for i in df.columns]]
# df2002.astype(int)
# df2001= df.loc[:,['2001' in i for i in df.columns]]
# df2001.astype(int)
# =============================================================================

# =============================================================================
# 
#    Colunm Name :  Full time total (EF2020  All students  Undergraduate total)
#    Column Contents :  [18420]
#    Colunm Name :  Part time total (EF2020  All students  Undergraduate total)
#    Column Contents :  [1307]
#    Colunm Name :  Full time total (EF2020  All students  Graduate and First professional)
#    Column Contents :  [1094]
#    Colunm Name :  Part time total (EF2020  All students  Graduate and First professional)
#    Column Contents :  [773]
#    Colunm Name :  Full time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)
#    Column Contents :  [606]
#    Colunm Name :  Part time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)
#    Column Contents :  [87]
#    Colunm Name :  Full time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)
#    Column Contents :  [4479]
#    Colunm Name :  Part time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)
# 
# =============================================================================#
undergraduateFullTime2020 = df2020['Full time total (EF2020  All students  Undergraduate total)']
undergraduatePartTime2020 = df2020['Part time total (EF2020  All students  Undergraduate total)']
graduateEnrollment2020 = df2020['Full time total (EF2020  All students  Graduate and First professional)'] + df2020['Part time total (EF2020  All students  Graduate and First professional)']
firstTimeFreshmen2020 = df2020['Full time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2020 ['Part time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)']
newTransfer2020 = df2020['Part time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2020['Full time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
totalEnrollment2020 = df2020['Full time total (EF2020  All students  Undergraduate total)'] + graduateEnrollment2020

#2020
# undergraduateFullTime2020 = df2020['Full time total (EF2020  All students  Undergraduate total)'].astype(int)
# undergraduatePartTime2020 = df2020['Part time total (EF2020  All students  Undergraduate total)'].astype(int)
# graduateEnrollment2020 = df2020['Full time total (EF2020  All students  Graduate and First professional)'].astype(int) + df2020['Part time total (EF2020  All students  Graduate and First professional)'].astype(int)
# firstTimeFreshmen2020 = df2020['Full time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)'].astype(int) + df2020 ['Part time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)'].astype(int)
# newTransfer2020 = df2020['Part time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'].astype(int) + df2020['Full time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'].astype(int)
# totalEnrollment2020 = df2020['Full time total (EF2020  All students  Undergraduate total)'].astype(int) + graduateEnrollment2020


# #2019
# undergraduateFullTime2019 = df2019['Full time total (EF2019_RV  All students  Undergraduate total)']
# undergraduatePartTime2019 = df2019['Part time total (EF2019_RV  All students  Undergraduate total)']
# graduateEnrollment2019 = df2019['Full time total (EF2019_RV  All students  Graduate and First professional)'] + df2019['Part time total (EF2019_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2019 = df2019['Full time total (EF2019_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2019 ['Part time total (EF2019_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2019 = df2019['Part time total (EF2019_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2019['Full time total (EF2019_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2019 = df2019['Full time total (EF2019_RV  All students  Undergraduate total)'] + graduateEnrollment2020

# #2018
# undergraduateFullTime2018 = df2018['Full time total (EF2018_RV  All students  Undergraduate total)']
# undergraduatePartTime2018 = df2018['Part time total (EF2018_RV  All students  Undergraduate total)']
# graduateEnrollment2018 = df2018['Full time total (EF2018_RV  All students  Graduate and First professional)'] + df2018['Part time total (EF2018_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2018 = df2018['Full time total (EF2018_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2018 ['Part time total (EF2018_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2018 = df2018['Part time total (EF2018_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2018['Full time total (EF2018_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2018 = df2018['Full time total (EF2018_RV  All students  Undergraduate total)'] + graduateEnrollment2018

# #2017
# undergraduateFullTime2017 = df2017['Full time total (EF2017_RV  All students  Undergraduate total)']
# undergraduatePartTime2017 = df2017['Part time total (EF2017_RV  All students  Undergraduate total)']
# graduateEnrollment2017 = df2017['Full time total (EF2017_RV  All students  Graduate and First professional)'] + df2017['Part time total (EF2017_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2017 = df2017['Full time total (EF2017_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2017 ['Part time total (EF2017_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2017 = df2017['Part time total (EF2017_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2017['Full time total (EF2017_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2017 = df2017['Full time total (EF2017_RV  All students  Undergraduate total)'] + graduateEnrollment2017

# #2016
# undergraduateFullTime2016 = df2016['Full time total (EF2016_RV  All students  Undergraduate total)']
# undergraduatePartTime2016 = df2016['Part time total (EF2016_RV  All students  Undergraduate total)']
# graduateEnrollment2016 = df2016['Full time total (EF2016_RV  All students  Graduate and First professional)'] + df2016['Part time total (EF2016_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2016 = df2016['Full time total (EF2016_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2016 ['Part time total (EF2016_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2016 = df2016['Part time total (EF2016_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2016['Full time total (EF2016_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2016 = df2016['Full time total (EF2016_RV  All students  Undergraduate total)'] + graduateEnrollment2016


# #2015
# undergraduateFullTime2015 = df2015['Full time total (EF2015_RV  All students  Undergraduate total)']
# undergraduatePartTime2015 = df2015['Part time total (EF2015_RV  All students  Undergraduate total)']
# graduateEnrollment2015 = df2015['Full time total (EF2015_RV  All students  Graduate and First professional)'] + df2015['Part time total (EF2015_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2015 = df2015['Full time total (EF2015_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2015 ['Part time total (EF2015_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2015 = df2015['Part time total (EF2015_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2015['Full time total (EF2015_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2015 = df2015['Full time total (EF2015_RV  All students  Undergraduate total)'] + graduateEnrollment2015

# #2014
# undergraduateFullTime2014 = df2014['Full time total (EF2014_RV  All students  Undergraduate total)']
# undergraduatePartTime2014 = df2014['Part time total (EF2014_RV  All students  Undergraduate total)']
# graduateEnrollment2014 = df2014['Full time total (EF2014_RV  All students  Graduate and First professional)'] + df2014['Part time total (EF2014_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2014 = df2014['Full time total (EF2014_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2014 ['Part time total (EF2014_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2014 = df2014['Part time total (EF2014_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2014['Full time total (EF2014_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2014 = df2014['Full time total (EF2014_RV  All students  Undergraduate total)'] + graduateEnrollment2014

# #2013
# undergraduateFullTime2013 = df2013['Full time total (EF2013_RV  All students  Undergraduate total)']
# undergraduatePartTime2013 = df2013['Part time total (EF2013_RV  All students  Undergraduate total)']
# graduateEnrollment2013 = df2013['Full time total (EF2013_RV  All students  Graduate and First professional)'] + df2013['Part time total (EF2013_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2013 = df2013['Full time total (EF2013_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2013['Part time total (EF2013_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2013 = df2013['Part time total (EF2013_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2013['Full time total (EF2013_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2013 = df2013['Full time total (EF2013_RV  All students  Undergraduate total)'] + graduateEnrollment2013

# #2012
# undergraduateFullTime2012 = df2012['Full time total (EF2012_RV  All students  Undergraduate total)']
# undergraduatePartTime2012 = df2012['Part time total (EF2012_RV  All students  Undergraduate total)']
# graduateEnrollment2012 = df2012['Full time total (EF2012_RV  All students  Graduate and First professional)'] + df2012['Part time total (EF2012_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2012 = df2012['Full time total (EF2012_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2012 ['Part time total (EF2012_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2012 = df2012['Part time total (EF2012_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2012['Full time total (EF2012_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2012 = df2012['Full time total (EF2012_RV  All students  Undergraduate total)'] + graduateEnrollment2012

# #2011
# undergraduateFullTime2011 = df2011['Full time total (EF2011_RV  All students  Undergraduate total)']
# undergraduatePartTime2011 = df2011['Part time total (EF2011_RV  All students  Undergraduate total)']
# graduateEnrollment2011 = df2011['Full time total (EF2011_RV  All students  Graduate and First professional)'] + df2011['Part time total (EF2011_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2011 = df2011['Full time total (EF2011_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2011 ['Part time total (EF2011_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2011 = df2011['Part time total (EF2011_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2011['Full time total (EF2011_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2011 = df2011['Full time total (EF2011_RV  All students  Undergraduate total)'] + graduateEnrollment2011

# #2010
# undergraduateFullTime2010 = df2010['Full time total (EF2010_RV  All students  Undergraduate total)']
# undergraduatePartTime2010= df2010['Part time total (EF2010_RV  All students  Undergraduate total)']
# graduateEnrollment2010 = df2010['Full time total (EF2010_RV  All students  Graduate and First professional)'] + df2010['Part time total (EF2010_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2010 = df2010['Full time total (EF2010_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2010 ['Part time total (EF2010_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2010 = df2010['Part time total (EF2010_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2010['Full time total (EF2010_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2010 = df2010['Full time total (EF2010_RV  All students  Undergraduate total)'] + graduateEnrollment2010

# #2009
# undergraduateFullTime2009 = df2009['Full time total (EF2009_RV  All students  Undergraduate total)']
# undergraduatePartTime2009 = df2009['Part time total (EF2009_RV  All students  Undergraduate total)']
# graduateEnrollment2009 = df2009['Full time total (EF2009_RV  All students  Graduate and First professional)'] + df2009['Part time total (EF2009_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2009 = df2009['Full time total (EF2009_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2009 ['Part time total (EF2009_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2009 = df2009['Part time total (EF2009_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2009['Full time total (EF2009_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2009 = df2009['Full time total (EF2009_RV  All students  Undergraduate total)'] + graduateEnrollment2009

# #2008
# undergraduateFullTime2008 = df2008['Full time total (EF2008_RV  All students  Undergraduate total)']
# undergraduatePartTime2008 = df2008['Part time total (EF2008_RV  All students  Undergraduate total)']
# graduateEnrollment2008 = df2008['Full time total (EF2008_RV  All students  Graduate and First professional)'] + df2008['Part time total (EF2008_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2008 = df2008['Full time total (EF2008_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2008 ['Part time total (EF2008_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2008 = df2008['Part time total (EF2008_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2008['Full time total (EF2008_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2008 = df2008['Full time total (EF2008_RV  All students  Undergraduate total)'] + graduateEnrollment2008

# #2007
# undergraduateFullTime2007 = df2007['Full time total (EF2007_RV  All students  Undergraduate total)']
# undergraduatePartTime2007 = df2007['Part time total (EF2007_RV  All students  Undergraduate total)']
# graduateEnrollment2007 = df2007['Full time total (EF2007_RV  All students  Graduate and First professional)'] + df2007['Part time total (EF2007_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2007 = df2007['Full time total (EF2007_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2007['Part time total (EF2007_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2007 = df2007['Part time total (EF2007_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2007['Full time total (EF2007_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2007 = df2007['Full time total (EF2007_RV  All students  Undergraduate total)'] + graduateEnrollment2007

# #2006
# undergraduateFullTime2006 = df2006['Full time total (EF2006_RV  All students  Undergraduate total)']
# undergraduatePartTime2006 = df2006['Part time total (EF2006_RV  All students  Undergraduate total)']
# graduateEnrollment2006 = df2006['Full time total (EF2006_RV  All students  Graduate and First professional)'] + df2006['Part time total (EF2006_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2006 = df2006['Full time total (EF2006_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2006['Part time total (EF2006_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2006 = df2006['Part time total (EF2006_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2006['Full time total (EF2006_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2006 = df2006['Full time total (EF2006_RV  All students  Undergraduate total)'] + graduateEnrollment2006

# #2005
# undergraduateFullTime2005 = df2005['Full time total (EF2005_RV  All students  Undergraduate total)']
# undergraduatePartTime2005 = df2005['Part time total (EF2005_RV  All students  Undergraduate total)']
# graduateEnrollment2005 = df2005['Full time total (EF2005_RV  All students  Graduate and First professional)'] + df2005['Part time total (EF2005_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2005 = df2005['Full time total (EF2005_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2005 ['Part time total (EF2005_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2005 = df2005['Part time total (EF2005_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2005['Full time total (EF2005_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2005 = df2005['Full time total (EF2005_RV  All students  Undergraduate total)'] + graduateEnrollment2005

# #2004
# undergraduateFullTime2004 = df2004['Full time total (EF2004_RV  All students  Undergraduate total)']
# undergraduatePartTime2004= df2004['Part time total (EF2004_RV  All students  Undergraduate total)']
# graduateEnrollment2004 = df2004['Full time total (EF2004_RV  All students  Graduate and First professional)'] + df2004['Part time total (EF2004_RV  All students  Graduate and First professional)']
# firstTimeFreshmen2004 = df2004['Full time total (EF2004_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2004['Part time total (EF2004_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2004 = df2004['Part time total (EF2004_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2004['Full time total (EF2004_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2004 = df2004['Full time total (EF2004_RV  All students  Undergraduate total)'] + graduateEnrollment2004

# #2003
# undergraduateFullTime2003 = df2003['Full time total (EF2003  All students  Undergraduate total)']
# undergraduatePartTime2003 = df2003['Part time total (EF2003  All students  Undergraduate total)']
# graduateEnrollment2003 = df2003['Full time total (EF2003  All students  Graduate and First professional)'] + df2003['Part time total (EF2003  All students  Graduate and First professional)']
# firstTimeFreshmen2003 = df2003['Full time total (EF2003  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2003['Part time total (EF2003  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2003 = df2003['Part time total (EF2003  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2003['Full time total (EF2003  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2003 = df2003['Full time total (EF2003  All students  Undergraduate total)'] + graduateEnrollment2003

# #2002
# undergraduateFullTime2002 = df2002['Full time total (EF2002  All students  Undergraduate total)']
# undergraduatePartTime2002 = df2002['Part time total (EF2002  All students  Undergraduate total)']
# graduateEnrollment2002 = df2002['Full time total (EF2002  All students  Graduate and First professional)'] + df2002['Part time total (EF2002  All students  Graduate and First professional)']
# firstTimeFreshmen2002 = df2002['Full time total (EF2002  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2002['Part time total (EF2002  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2002 = df2002['Part time total (EF2002  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2002['Full time total (EF2002  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2002 = df2002['Full time total (EF2002  All students  Undergraduate total)'] + graduateEnrollment2002

# #2001
# undergraduateFullTime2001 = df2001['Full time total (EF2001  All students  Undergraduate total)']
# undergraduatePartTime2001 = df2001['Part time total (EF2001  All students  Undergraduate total)']
# graduateEnrollment2001 = df2001['Full time total (EF2001  All students  Graduate and First professional)'] + df2001['Part time total (EF2001  All students  Graduate and First professional)']
# firstTimeFreshmen2001 = df2001['Full time total (EF2001  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2001['Part time total (EF2001  All students  Undergraduate  Degree/certificate-seeking  First-time)']
# newTransfer2001 = df2001['Part time total (EF2001  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2001['Full time total (EF2001  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
# totalEnrollment2001 = df2001['Full time total (EF2001  All students  Undergraduate total)'] + graduateEnrollment2001

# # =============================================================================
# # DATAFRAME
# #
# #
# #
# # Total Enrollment (undergrad + grad)	     NUMBER
# # Undergrad enrollment - Full Time		     NUMBER 
# # Undergrad enrollment - Part Time 		     NUMBER 
# # Graduate Enrollment 		                 NUMBER
# # First-Time Freshman Enrollment 		     NUMBER
# # New Transfer Enrollment (Fall)		     NUMBER
# # 
# # =============================================================================


universityModelFinal = pd.DataFrame({
                         "2020":[totalEnrollment2020, undergraduateFullTime2020, undergraduatePartTime2020, graduateEnrollment2020, firstTimeFreshmen2020, newTransfer2020]})
#                           "2019":[totalEnrollment2019 , undergraduateFullTime2019, undergraduatePartTime2019, graduateEnrollment2019, firstTimeFreshmen2019, newTransfer2019],
#                           "2018":[totalEnrollment2018 , undergraduateFullTime2018, undergraduatePartTime2018, graduateEnrollment2018, firstTimeFreshmen2018, newTransfer2018],
#                           "2017":[totalEnrollment2017 , undergraduateFullTime2017, undergraduatePartTime2017, graduateEnrollment2017, firstTimeFreshmen2017, newTransfer2017],
#                           "2016":[totalEnrollment2016 , undergraduateFullTime2016, undergraduatePartTime2016, graduateEnrollment2016, firstTimeFreshmen2016, newTransfer2016],
#                           "2015":[totalEnrollment2015 , undergraduateFullTime2015, undergraduatePartTime2015, graduateEnrollment2015, firstTimeFreshmen2015, newTransfer2015],
#                           "2014":[totalEnrollment2014 , undergraduateFullTime2014, undergraduatePartTime2014, graduateEnrollment2014, firstTimeFreshmen2014, newTransfer2014],
#                           "2013":[totalEnrollment2013 , undergraduateFullTime2013, undergraduatePartTime2013, graduateEnrollment2013, firstTimeFreshmen2013, newTransfer2013],
#                           "2012":[totalEnrollment2012 , undergraduateFullTime2012, undergraduatePartTime2012, graduateEnrollment2012, firstTimeFreshmen2012, newTransfer2012],
#                             "2011":[totalEnrollment2011 , undergraduateFullTime2011, undergraduatePartTime2011, graduateEnrollment2011, firstTimeFreshmen2011, newTransfer2011],
#                             "2010":[totalEnrollment2010 , undergraduateFullTime2010, undergraduatePartTime2010, graduateEnrollment2010, firstTimeFreshmen2010, newTransfer2010],
#                             "2009":[totalEnrollment2009 , undergraduateFullTime2009, undergraduatePartTime2009, graduateEnrollment2009, firstTimeFreshmen2009, newTransfer2009],
#                             "2008":[totalEnrollment2008 , undergraduateFullTime2008, undergraduatePartTime2008, graduateEnrollment2008, firstTimeFreshmen2008, newTransfer2008],
#                             "2007":[totalEnrollment2007 , undergraduateFullTime2007, undergraduatePartTime2007, graduateEnrollment2007, firstTimeFreshmen2007, newTransfer2007],
#                             "2006":[totalEnrollment2006 , undergraduateFullTime2006, undergraduatePartTime2006, graduateEnrollment2006, firstTimeFreshmen2006, newTransfer2006],
#                             "2005":[totalEnrollment2005 , undergraduateFullTime2005, undergraduatePartTime2005, graduateEnrollment2005, firstTimeFreshmen2005, newTransfer2005],
#                             "2004":[totalEnrollment2004 , undergraduateFullTime2004, undergraduatePartTime2004, graduateEnrollment2004, firstTimeFreshmen2004, newTransfer2004],
#                             "2003":[totalEnrollment2003 , undergraduateFullTime2003, undergraduatePartTime2003, graduateEnrollment2003, firstTimeFreshmen2003, newTransfer2003],
#                             "2002":[totalEnrollment2002 , undergraduateFullTime2002, undergraduatePartTime2002, graduateEnrollment2002, firstTimeFreshmen2002, newTransfer2002],
#                             "2001":[totalEnrollment2001 , undergraduateFullTime2001, undergraduatePartTime2001, graduateEnrollment2001, firstTimeFreshmen2001, newTransfer2001]}).astype(float)

      

