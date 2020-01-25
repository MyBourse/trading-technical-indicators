'''
File name: _data_preprocessing.py
    Data preprocessing methods defined under the tradingti.utils package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

def fillMissingValues(df_data):
    '''
    Fills the missing values of a dataframe by executing first abs
    forward pass and then a backward pass. See details in:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html
    
    Args:
        df_data (pandas.core.frame.DataFrame): The input data.

    Raises:
        -

    Returns:
        pandas.core.frame.DataFrame: The input data with missing
            values filled.
    '''
    
    # Sort dataframe on index ascending
    df_data = df_data.sort_index(ascending = True)
    
    # Fill forward
    df_data.fillna(method = 'ffill', inplace = True)
    
    # Fill backward
    df_data.fillna(method = 'bfill', inplace = True)
    
    return df_data