'''
File name: _technical_indicator.py
    Volume technical indicators implementation.
    Implements the following technical indicators:
    - On Balance Volume (OBV class)
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 06.02.2020

Python Version: 3.6
'''

import pandas as pd
from ._technical_indicator import TI
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues
from .._constants import *


class OBV(TI):
    '''
    On Balance Volume (OBV) Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains the below columns:
            'Volume', 'Adj Close'
            
    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        - TypeError
        - ValueError
        
    '''
    def __init__(self, df_data):
        
        # Validate the input data, check tradingti.utils._data_validation module
        # for details
        data_validation = validateStockData(df_data)
        if data_validation is not None:
            raise(TypeError(data_validation))
            
        # Validate that all required input data are available
        if 'Volume' not in df_data.columns:
            raise(ValueError('Input \'Volume\' data are missing for OBV '    +\
                'indicator use. Mandatory input data are: \'Volume\'.'))
        elif 'Adj Close' not in df_data.columns:
            raise(ValueError('Input \'Adj Close\' data are missing for OBV ' +\
                'indicator use. Mandatory input data are: \'Adj Close\'.'))

        # Sort the input data and fill the missing values if any
        self._input_data = fillMissingValues(df_data)[['Volume', 'Adj Close']]

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)
        super().__init__(input_data = df_data['Adj Close'].to_frame(), 
            ti_data = self._calculateIndicator(self._input_data),
            indicator_name = 'OBV', lines_color = ['black', 'limegreen'], 
            subplots = True)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the OBV for the given input data.

        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains one column, the
                'OBV'.
        '''
        
        obv = pd.DataFrame(index = input_data.index, columns = ['OBV'], 
            data = None)
        
        obv.iat[0, 0] = 0.0
        for i in range(1, len(input_data.index)):

            # Today's close is greater than yesterday's close
            if input_data.iat[i, 1] > input_data.iat[i-1, 1]:
                obv.iat[i, 0] = obv.iat[i-1, 0] + input_data.iat[i, 0]
                
            # Today's close is less than yesterday's close
            elif input_data.iat[i, 1] < input_data.iat[i-1, 1]:
                obv.iat[i, 0] = obv.iat[i-1, 0] - input_data.iat[i, 0]
                
            # Today's close is equal than yesterday's close
            elif input_data.iat[i, 1] == input_data.iat[i-1, 1]:
                obv.iat[i, 0] = obv.iat[i-1, 0]
            
        return obv
        
        
    def getSignal(self):
        '''
        Calculates and returns the signal of the technical indicator.
    
        Args:
            -

        Raises:
            -

        Returns:
            integer: The Trading signal. Possible values are {'Hold': 0, 
                'Buy': -1, 'Sell': 1}. See TRADE_SIGNALS package constant.
        '''

        if self._ti_data.iat[-3, 0] > self._ti_data.iat[-2, 0] and\
            self._ti_data.iat[-2, 0] > self._ti_data.iat[-1, 0]:
            return TRADE_SIGNALS['Sell']
            
        elif self._ti_data.iat[-3, 0] < self._ti_data.iat[-2, 0] and\
            self._ti_data.iat[-2, 0] < self._ti_data.iat[-1, 0]:
            return TRADE_SIGNALS['Buy']
            
        else:
            return TRADE_SIGNALS['Hold']