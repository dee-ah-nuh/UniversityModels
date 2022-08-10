# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:35:26 2022

@author: BEEMO
"""
import re
import numpy as np
import pandas as pd
import csv

#separate into dataframes
#sum the column values 
#finally append those column values to a new dataframe with new name 



df = pd.read_csv("C:/Users/BEEMO/Downloads/James Madison Data.csv")

df2020=df.loc[:,['2020' in i for i in df.columns]]
df2019=df.loc[:,['2019' in i for i in df.columns]]
df2018=df.loc[:,['2018' in i for i in df.columns]]
df2017= df.loc[:,['2017' in i for i in df.columns]]
df2016= df.loc[:,['2016' in i for i in df.columns]]
df2015= df.loc[:,['2015' in i for i in df.columns]]
df2014= df.loc[:,['2014' in i for i in df.columns]]
df2013= df.loc[:,['2013' in i for i in df.columns]]
df2012= df.loc[:,['2012' in i for i in df.columns]]
df2011= df.loc[:,['2011' in i for i in df.columns]]
df2010= df.loc[:,['2010' in i for i in df.columns]]
df2009= df.loc[:,['2009' in i for i in df.columns]]
df2008= df.loc[:,['2008' in i for i in df.columns]]
df2007= df.loc[:,['2007' in i for i in df.columns]]
df2006= df.loc[:,['2006' in i for i in df.columns]]
df2005= df.loc[:,['2005' in i for i in df.columns]]
df2004= df.loc[:,['2004' in i for i in df.columns]]
df2003= df.loc[:,['2003' in i for i in df.columns]]
df2002= df.loc[:,['2002' in i for i in df.columns]]
df2001= df.loc[:,['2001' in i for i in df.columns]]

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

# =============================================================================
# pd
# Total Enrollment (undergrad + grad)		  19,038 
# Undergrad enrollment - Full Time		  12,150 
# Undergrad enrollment - Part Time 		  3,159 
# Graduate Enrollment 		  2,743 
# First-Time Freshman Enrollment 		  3,021 
# New Transfer Enrollment (Fall)		  1,100 
# 
# =============================================================================
universityModelFinal = pd.DataFrame({"2020":[totalEnrollment2020 , undergraduateFullTime2020, undergraduatePartTime2020, graduateEnrollment2020, firstTimeFreshmen2020, newTransfer2020],
                         "2019":[totalEnrollment2020 , undergraduateFullTime2020, undergraduatePartTime2020, graduateEnrollment2020, firstTimeFreshmen2020, newTransfer2020]})



































