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

#2020
undergraduateFullTime2020 = df2020['Full time total (EF2020  All students  Undergraduate total)']
undergraduatePartTime2020 = df2020['Part time total (EF2020  All students  Undergraduate total)']
graduateEnrollment2020 = df2020['Full time total (EF2020  All students  Graduate and First professional)'] + df2020['Part time total (EF2020  All students  Graduate and First professional)']
firstTimeFreshmen2020 = df2020['Full time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2020 ['Part time total (EF2020  All students  Undergraduate  Degree/certificate-seeking  First-time)']
newTransfer2020 = df2020['Part time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2020['Full time total (EF2020  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
totalEnrollment2020 = df2020['Full time total (EF2020  All students  Undergraduate total)'] + graduateEnrollment2020


#2019
undergraduateFullTime2019 = df2019['Full time total (EF2019_RV  All students  Undergraduate total)']
undergraduatePartTime2019 = df2019['Part time total (EF2019_RV  All students  Undergraduate total)']
graduateEnrollment2019 = df2019['Full time total (EF2019_RV  All students  Graduate and First professional)'] + df2019['Part time total (EF2019_RV  All students  Graduate and First professional)']
firstTimeFreshmen2019 = df2019['Full time total (EF2019_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2019 ['Part time total (EF2019_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
newTransfer2019 = df2019['Part time total (EF2019_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2019['Full time total (EF2019_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
totalEnrollment2019 = df2019['Full time total (EF2019_RV  All students  Undergraduate total)'] + graduateEnrollment2020

#2018
undergraduateFullTime2018 = df2018['Full time total (EF2018_RV  All students  Undergraduate total)']
undergraduatePartTime2018 = df2018['Part time total (EF2018_RV  All students  Undergraduate total)']
graduateEnrollment2018 = df2018['Full time total (EF2018_RV  All students  Graduate and First professional)'] + df2018['Part time total (EF2018_RV  All students  Graduate and First professional)']
firstTimeFreshmen2018 = df2018['Full time total (EF2018_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2018 ['Part time total (EF2018_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
newTransfer2018 = df2018['Part time total (EF2018_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2018['Full time total (EF2018_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
totalEnrollment2018 = df2018['Full time total (EF2018_RV  All students  Undergraduate total)'] + graduateEnrollment2018

#2017
undergraduateFullTime2017 = df2017['Full time total (EF2017_RV  All students  Undergraduate total)']
undergraduatePartTime2017 = df2017['Part time total (EF2017_RV  All students  Undergraduate total)']
graduateEnrollment2017 = df2017['Full time total (EF2017_RV  All students  Graduate and First professional)'] + df2017['Part time total (EF2017_RV  All students  Graduate and First professional)']
firstTimeFreshmen2017 = df2017['Full time total (EF2017_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2017 ['Part time total (EF2017_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
newTransfer2017 = df2017['Part time total (EF2017_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2017['Full time total (EF2017_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
totalEnrollment2017 = df2017['Full time total (EF2017_RV  All students  Undergraduate total)'] + graduateEnrollment2017

#2016
undergraduateFullTime2016 = df2016['Full time total (EF2016_RV  All students  Undergraduate total)']
undergraduatePartTime2016 = df2016['Part time total (EF2016_RV  All students  Undergraduate total)']
graduateEnrollment2016 = df2016['Full time total (EF2016_RV  All students  Graduate and First professional)'] + df2016['Part time total (EF2016_RV  All students  Graduate and First professional)']
firstTimeFreshmen2016 = df2016['Full time total (EF2016_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)'] + df2016 ['Part time total (EF2016_RV  All students  Undergraduate  Degree/certificate-seeking  First-time)']
newTransfer2016 = df2016['Part time total (EF2016_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)'] + df2016['Full time total (EF2016_RV  All students  Undergraduate  Other degree/certificate-seeking  Transfer-ins)']
totalEnrollment2016 = df2016['Full time total (EF2016_RV  All students  Undergraduate total)'] + graduateEnrollment2016



# =============================================================================
# DATAFRAME
#
#
#
# Total Enrollment (undergrad + grad)	     NUMBER
# Undergrad enrollment - Full Time		     NUMBER 
# Undergrad enrollment - Part Time 		     NUMBER 
# Graduate Enrollment 		                 NUMBER
# First-Time Freshman Enrollment 		     NUMBER
# New Transfer Enrollment (Fall)		     NUMBER
# 
# =============================================================================


universityModelFinal = pd.DataFrame({
                        "2020":[totalEnrollment2020 , undergraduateFullTime2020, undergraduatePartTime2020, graduateEnrollment2020, firstTimeFreshmen2020, newTransfer2020],
                         "2019":[totalEnrollment2019 , undergraduateFullTime2019, undergraduatePartTime2019, graduateEnrollment2019, firstTimeFreshmen2019, newTransfer2019],
                         "2018":[totalEnrollment2018 , undergraduateFullTime2018, undergraduatePartTime2018, graduateEnrollment2018, firstTimeFreshmen2018, newTransfer2018],
                         "2017":[totalEnrollment2017 , undergraduateFullTime2017, undergraduatePartTime2017, graduateEnrollment2017, firstTimeFreshmen2017, newTransfer2017]})



































