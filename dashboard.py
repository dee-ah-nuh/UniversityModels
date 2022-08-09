# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 10:07:19 2022

@author: Diana Valladares
"""

import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import os 
username=os.getlogin()

filepath= (f'C:/Users/{username}/')
app = dash.Dash(__name__)


df = pd.read_csv(filepath + "Documents/GitHub/Python-Projects/KPI 2022 Goals .csv")
df.dropna(axis = 1, how = 'all', inplace=True)
df['Total Transfers '] =df['Total Transfers '].replace({"215 so far": 215})
df['Total Applications'] = df['Total Applications'].replace({'25 so far':25})
df['Workable Total Transfers  (MQL)'] =df['Workable Total Transfers  (MQL)'].replace({"161 so far": 161})
df['Total Applications  (UQL)'] =df['Total Applications  (UQL)'].replace({"25 so far": 25})

fig = px.scatter(df, x='Total Transfers ', y= 'Year 2022 Month', log_x=True, size='Total Transfer Conversion % ', color='Workable Total Transfer Conversion % ')

app.layout = html.Div([dcc.Graph(id="Operation Graduate KPI", figure=fig)])

fig.show()
