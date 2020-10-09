#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:27:39 2020

@author: rid
"""

import pandas as pd
import KN311Petrov2 as p
from datetime import datetime

def magic_parser(csv_file_name):
    # Donwload to dataFrame
    df = pd.read_csv(csv_file_name, delimiter=";")
    
    print(df.head())
    
    # Set index field
    df['day/month'] = [datetime.strftime(datetime.strptime(d + ' 2019', '%d.%b %Y'), '%d.%m.%Y') for d in df['day/month']]

    df = df.set_index('day/month')
    
    # Convert to right type columns and do something with time
    df['Time'] = [datetime.strftime(datetime.strptime(t, '%I:%M %p'), '%H:%M') for t in df['Time']]
    
    df['Humidity'] = [h.replace('%', '') for h in df['Humidity']]
    df['Humidity'] = df['Humidity'].astype('int64')
    
    df['Wind Speed'] = [i.replace(' mph', '') for i in df['Wind Speed']]
    df['Wind Speed'] = df['Wind Speed'].astype('int64')
    
    df['Wind Gust'] = [i.replace(' mph ', '') for i in df['Wind Gust']]
    df['Wind Gust'] = df['Wind Gust'].astype('int64')
    
    df['Pressure'] = [i.replace(',', '.') for i in df['Pressure']]
    df['Pressure'] = df['Pressure'].astype('float64')
    
    print(df.head())
    
    return df


p.magic_viz(magic_parser('DATABASE.csv'))