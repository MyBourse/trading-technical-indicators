'''
File name: _data_validation.py
    Data validation methods implementation, defined under the 
    tradingti.utils package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 08.02.2020

Python Version: 3.6
'''

import pandas.core as pc
from pandas.api.types import is_numeric_dtype
from _data_preprocessing import fillMissingValues


def validateDataframe(data):
    '''
    Validates that the data argument is a pandas data frame and that its index
    is of date type.
    
    Args:
        data (object): Input object to be validated.

    Raises:
        TypeError

    Returns:
        -
    '''

    # Validate that the data argumnet is a pandas dataframe object
    if not isinstance(data, pc.frame.DataFrame):
        raise TypeError('The argument should be of type pandas.core.frame.' +\
            'DataFrame but it is of type ' + str(type(data)) + '.')

    # Validate that the index of the pandas dataframe is a date
    if not isinstance(data.index, pc.indexes.datetimes.DatetimeIndex):
        raise TypeError('The index of the dataframe argument should be of ' +\
            'type pandas.core.indexes.datetimes.DatetimeIndex but it is of '+\
            'type ' + str(type(data.index)) + '.')
    

def validateStockData(data, required_columns, indicator_name):
    '''
    Validates that the data argument is a pandas data frame, that its index
    is of type date, that it is not empty and that it contains the 
    required columns (required_columns argument). It returns back the data frame
    with only the required columns, sorted on the date index and with missing
    values filled. It raises an exception in case the validation fails.

    Args:
        data (object): Input object to be validated.
        
        required_columns (list of strings): The columns which should contained
            in the data frame (data object).
            
        indicator_name (string): The name of the indicator. To be used in case
            an exception is raised.
        
    Raises:
        TypeError
        ValueError

    Returns:
        pandas.core.frame.DataFrame: The input data frame containing only the 
            required columns, sorted and with missing values filled. The data 
            frame is ready to be used from the technical indicator class without
            any further processing.
    '''
    
    # Validate the type of the input arguments
    validateDataframe(data)
    
    if type(required_columns) != list:
        raise TypeError('The argument required_columns should be a list ' +\
            'but it is of type ' + str(type(required_columns)) + '.')

    # Validate that the data frame is not empty
    if data.empty:
        raise ValueError('The input data cannot be empty. data_len = ' +\
            str(len(data.index)) + '.')
   
    # Validate that the data frame holds columns of numeric type and that all
    # the required columns are contained.
    for column in data.columns:
        if not is_numeric_dtype(data[column]):
            raise ValueError('The input data frame must hold columns of ' +\
                'numeric type. column = ' + column + ', is_numeric = '    +\
                str(is_numeric_dtype(data[column])) + '.')
                
    for column in required_columns:
        # Check that required_columns are strings
        if type(column) != str:
            raise TypeError('Required columns list should contain strings ' +\
                'but column = ' + str(column) + ' it is of type '           +\
                str(type(column)) + '.')
            
        elif column not in data.columns:
            raise ValueError('Required column ' + column + ' for the ' +\
                'technical indicator ' + indicator_name + ' was not '  +\
                'found in the data frame.')
    
    # Remove not required columns
    for column in data.columns:
        if column not in required_columns:
            data = data.drop(columns = column)
    
    return fillMissingValues(data)