'''
File name: _data_validation.py
    Data validation methods implementation defined under the 
    tradingti.utils package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

import pandas.core as pc
from pandas.api.types import is_numeric_dtype


def validateDataframe(data):
    '''
    Validates that the data argument is a pandas data frame and that its index
    is date type.
    
    Args:
        data (object): Input object to be validated.

    Raises:
        -

    Returns:
        string or None: A message string if the validation fails, otherwise
            None.
    '''

    # Validate that the data argumnet is a pandas dataframe object
    if not isinstance(data, pc.frame.DataFrame):
        return 'The \'data\' argument of the \'lineGraph\' method should ' +\
            'be of type pandas.core.frame.DataFrame but it is of type '    +\
            str(type(data)) + '.'

    # Validate that the index of the pandas dataframe is a date
    if not isinstance(data.index, pc.indexes.datetimes.DatetimeIndex):
        return 'The index of the \'data\' dataframe argument of the '        +\
            '\'lineGraph\' method should be of type '                        +\
            'pandas.core.indexes.datetimes.DatetimeIndex but it is of type ' +\
            str(type(data.index)) + '.'
    
    return None
    
    
def validateStockData(data):
    '''
    Validates that the data argument is a pandas data frame, that its index
    is of type date, that it is not empty and that it holds just one column
    of type numeric.
    
    Args:
        data (object): Input object to be validated.

    Raises:
        -

    Returns:
        string or None: A message string if the validation fails, otherwise
            None.
    '''

    dataframe_validation_result = validateDataframe(data)
    if dataframe_validation_result is not None:
        return dataframe_validation_result

    # Validate that the data frame is not empty
    if data.empty:
        return 'The input data cannot be empty. data_len = ' + str(len(data.index)) + '.'
   
    # Validate that the data frame holds a single column of numeric type (price)
    if len(data.columns) != 1 or not is_numeric_dtype(data[data.columns[0]]):
        return 'The input data frame must hold a single column of numeric type. ' +\
            'columns_number = ' + str(len(data.columns)) + ', is_numeric = '      +\
            str(is_numeric_dtype(data[data.columns[0]])) + '.'
            