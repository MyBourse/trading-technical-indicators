'''
File name: utils_data_preprocessing.py
    Example code rlated to the tradingti.utils.data_preprocessing
    module.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

import pandas as pd
from tradingti.utils import lineGraph, fillMissingValues
from pandas.plotting import register_matplotlib_converters

# Converters used in parsing the dates from csv
register_matplotlib_converters()

for data_file in ['example_data_missing_1.csv', 'example_data_missing_2.csv', 
    'example_data_missing_3.csv']:
    
    # Read data from csv file. Set the index to the correct column (dates column)
    df = pd.read_csv('./data/' + data_file, parse_dates = True, index_col = 0, 
        date_parser = lambda x: pd.datetime.strptime(x, '%y/%m/%d'))

    # Create a dataframe with original and modified values, for plotting the changes
    df = pd.concat([df, fillMissingValues(df)], axis = 1)
    df.columns=['Before','After']

    graph = lineGraph(data = df, title = 'Fill Missing Values', x_label = 'Date', y_label = 'Value in $')
    graph.savefig('./figures/' + data_file.split('.')[0] + '.png')
    graph.clf()
    
    print('- Graph', './figures/' + data_file.split('.')[0] + '.png', 'saved.')