#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:36:57 2020

@author: rid
"""

import numpy as np
import matplotlib.pyplot as plt

def frequency(column):
    freq = {}
    for i in column:
        freq[str(i)] = freq.get(str(i), 0) + 1
        
    return freq

# pie chart
def do_pie(data):
    patches, texts = plt.pie(data.values(), shadow=True, startangle=90)
    plt.legend(patches, data.keys(), loc='best')
    plt.axis('equal')
    plt.show()

# bar chart (horizontal)
def do_barh(data, data_name="Data"):
    y_pos = np.arange(len(data.values()))
    
    plt.barh(y_pos, data.values(), align='center', alpha=0.5)
    plt.yticks(y_pos, data.keys())
    plt.ylabel(data_name)
    plt.title(data_name + ' frequency')
    
    plt.show()
    

def do_bar(data, data_name="Data"):
    x_pos = np.arange(len(data.values()))
    
    plt.bar(x_pos, data.values(), align='center', alpha=0.5)
    plt.xticks(x_pos, data.keys())
    plt.xlabel(data_name)
    plt.title(data_name + ' frequency')
    plt.xticks(rotation='vertical')
    plt.show()
    
# linear chart
def do_line(data):
    data.plot()
    
def do_linear(data):
    plt.plot(data, '-')
    plt.ylabel(data.name)
    plt.xlabel(data.index.name)
    plt.xticks(rotation='vertical')
    plt.show()

# making a box plot
def do_box(data): 
    plt.boxplot(data)
    plt.title(data.name)
    plt.show() 

# scatter with index
def do_scatter_one(data):
    plt.plot(data, '.')
    plt.ylabel(data.name)
    plt.xlabel(data.index.name)
    plt.xticks(rotation='vertical')
    plt.show()

#scatter chart for two variables
def do_scatter_two(x, y, title = 'Scatter plot'):
    plt.scatter(x, y, alpha=0.5)
    plt.title(title)
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.show()

def do_two_bar(top, bottom):
    plt.bar(range(len(bottom)), bottom)
    plt.bar(range(len(top)), top, bottom=bottom)
    plt.legend([top.name, bottom.name])
    
    plt.show()

# The main MAGIC function
def magic_viz(df):
    
    for i in df:
        if (df[i].dtypes == 'object'):
            # do some magic
            # 12
            freq = frequency(df[i])
            if (len(freq) < 13):
                do_pie(freq)
            else:
                if (len(freq) > 25):
                    do_bar(freq, i)
                else:
                    do_barh(freq, i)
        else:
            # do another magic
            ind = df.index[len(df.index) // 2]
            freq = frequency(df[i][ind])
            if (len(freq) < 2):
                # do
                do_linear(df[i])
                
            elif (len(freq) < 8):
                do_scatter_one(df[i])
            else:
                do_box(df[i])
                
                
    