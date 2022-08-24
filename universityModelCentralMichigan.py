# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:35:33 2022

@author: DianaValladares
"""

import re
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt


centralmich = pd.read_csv(open('central mich.csv'))

df = centralmich[centralmich.columns.drop(list(centralmich.filter(regex='Graduate')))]


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



alluniversities = pd.read_csv(open('Michigan Public Schools.csv'))
michschools = alluniversities[alluniversities.columns.drop(list(alluniversities.filter(regex='Graduate')))]
michschools.to_csv("Michicgan Public Schools.csv")
michschools.columns.split("EF20")

plt.plot(michschools['Institution Name'], michschools['Grand total (EF2020  All students  Undergraduate total'])


