'''
File name: _technical_indicator.py
    Momentum technical indicators implementation.
    Implements the following technical indicators:
    - Fast Stochastic Oscillator (FSO class)
    - Slow Stochastic Oscillator (SSO class)
    - Relative Strength Index (RSI class)
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

import pandas as pd
from .._constants import *
from ._technical_indicator import TI
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues


class FSO(TI):
    '''
    Fast Stochastic Oscillator (FSO) Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains the below columns:
            'High', 'Low', 'Close', 'Adj Close'

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
        for c in ['High', 'Low', 'Close', 'Adj Close']:
            if c not in df_data.columns:
                raise(ValueError('Input \'' + c + '\' data are missing for FSO indicator use. '+\
                'Mandatory input data are: \'High\', \'Low\', \'Close\', \'Adj Close\'.'))
            
        # Sort the input data and fill the missing values if any
        df_data = fillMissingValues(df_data)

        # Parent class constructor (all job is done here, parent class provides the public
        # interface for accessing the data of the indicator)
        super().__init__(input_data = df_data['Adj Close'], ti_data = self._calculateIndicator(df_data),
            indicator_name = 'FSO', lines_color = ['cornflowerblue', 'tomato', 'limegreen'], subplots = True)
            
    
    def _calculateIndicator(self, input_data):
        '''
        Calculates the FSO for the given input data.
        
        Fast oscillating %K = 100[(C - L14) / (H14 – L14)]
        Where:
        C = Latest Close
        L14 = Lowest low for the last 14 periods.
        H14 = Highest high for the same 14 periods

        %D =  Three periods simple moving average of %K
    
        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains one or two
                columns depending the requested sma periods.
        '''
        
        fso = pd.DataFrame(index = input_data.index)
        
        # Fast oscillating (%K), initialize the first 13 periods to zero
        K = [0.0]*13

        for i in range(13, len(input_data.index)):

            # Lowest low for the last 14 periods
            L14 = min(input_data.iloc[i-13:i+1, input_data.columns.get_loc('Low')].values)
            
            # Highest high for the last 14 periods
            H14 = max(input_data.iloc[i-13:i+1, input_data.columns.get_loc('High')].values)
            
            K.append(round(100*(input_data.iat[i, input_data.columns.get_loc('Close')] - L14)/(H14 - L14), 2))
        
        fso['%K'] = K
        
        # Moving average of fast oscillating (%D)
        fso = pd.concat([fso, fso.rolling(window = 3, min_periods = 1, center = False,
                win_type = None, on = None, axis = 0, closed = None).mean().round(2)], axis = 1)
        
        fso.columns = ['%K', '%D']
        
        return fso
    
    
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
        
        # A sell signal is given when the oscillator is above the 80 level and 
        # then crosses back below 80.
        if self._ti_data.iat[-2, 0] > 80. and self._ti_data.iat[-1, 0] < 80.:
            return TRADE_SIGNALS['Sell']
        
        # A buy signal is given when the oscillator is below 20 and then crosses back above 20. 
        if self._ti_data.iat[-2, 0] < 20. and self._ti_data.iat[-1, 0] > 20.:
            return TRADE_SIGNALS['Buy']
        
        # A sell signal occurs when a decreasing %K line crosses below the %D line 
        # in the overbought region (%K > 80.) 
        if self._ti_data.iat[-2, 0] - self._ti_data.iat[-1, 0] > 0. and\
           self._ti_data.iat[-1, 0] - self._ti_data.iat[-1, 1] < 0. and\
           self._ti_data.iat[-1, 0] > 80.:
            return TRADE_SIGNALS['Sell']
            
        # A buy signal occurs when an increasing %K line crosses above the %D line in the 
        # oversold region (%K < 20.)
        if self._ti_data.iat[-2, 0] - self._ti_data.iat[-1, 0] < 0. and\
           self._ti_data.iat[-1, 0] - self._ti_data.iat[-1, 1] > 0. and\
           self._ti_data.iat[-1, 0] < 20.:
            return TRADE_SIGNALS['Buy']
        
        return TRADE_SIGNALS['Hold']
        
        
class SSO(TI):
    '''
    Slow Stochastic Oscillator (SSO) Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains the below columns:
            'High', 'Low', 'Close', 'Adj Close'

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
        for c in ['High', 'Low', 'Close', 'Adj Close']:
            if c not in df_data.columns:
                raise(ValueError('Input \'' + c + '\' data are missing for SSO indicator use. '+\
                'Mandatory input data are: \'High\', \'Low\', \'Close\', \'Adj Close\'.'))
            
        # Sort the input data and fill the missing values if any
        df_data = fillMissingValues(df_data)

        # Parent class constructor (all job is done here, parent class provides the public
        # interface for accessing the data of the indicator)
        super().__init__(input_data = df_data['Adj Close'], ti_data = self._calculateIndicator(df_data),
            indicator_name = 'SSO', lines_color = ['cornflowerblue', 'tomato', 'limegreen'], subplots = True)
            
    
    def _calculateIndicator(self, input_data):
        
        '''
        Calculates the SSO for the given input data.
        
        Slow oscillating %K= 100[Sum of the (C - L14) for three periods / 
            Sum of the (H14 – L14) for three periods]

        Where:
        C = Latest Close
        L14 = Lowest low for the last 14 periods
        H14 = Highest high for the same 14 periods
        
        %D =  Three periods simple moving average of %K
    
        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains one or two
                columns depending the requested sma periods.
        '''
        
        sso = pd.DataFrame(index = input_data.index)
        
        # Slow oscillating (%K), initialize the first 13 periods to zero
        K = [0.0]*15

        for i in range(15, len(input_data.index)):

            # Lowest low for the last 14 periods, sum of three periods low
            # Highest high for the last 14 periods, sum of three periods high
            sum_C_L14 = 0
            sum_H14_L14 = 0
            for j in range(3):
                L14 = min(input_data.iloc[i-13-j:i-j+1, input_data.columns.get_loc('Low')].values)
                H14 = max(input_data.iloc[i-13-j:i-j+1, input_data.columns.get_loc('High')].values)
                
                sum_H14_L14 += H14 - L14
                sum_C_L14 += input_data.iat[i-j, input_data.columns.get_loc('Close')] - L14
            
            K.append(round(100*sum_C_L14/sum_H14_L14, 2))
        
        sso['%K'] = K
        
        # Moving average of slow oscillating (%D)
        sso = pd.concat([sso, sso.rolling(window = 3, min_periods = 1, center = False,
                win_type = None, on = None, axis = 0, closed = None).mean().round(2)], axis = 1)
        
        sso.columns = ['%K', '%D']
        
        return sso
    
    
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

        # A sell signal is given when the oscillator is above the 80 level and 
        # then crosses back below 80.
        if self._ti_data.iat[-2, 0] > 80. and self._ti_data.iat[-1, 0] < 80.:
            return TRADE_SIGNALS['Sell']
        
        # A buy signal is given when the oscillator is below 20 and then crosses back above 20. 
        if self._ti_data.iat[-2, 0] < 20. and self._ti_data.iat[-1, 0] > 20.:
            return TRADE_SIGNALS['Buy']
        
        # A sell signal occurs when a decreasing %K line crosses below the %D line 
        # in the overbought region (%K > 80.) 
        if self._ti_data.iat[-2, 0] - self._ti_data.iat[-1, 0] > 0. and\
           self._ti_data.iat[-1, 0] - self._ti_data.iat[-1, 1] < 0. and\
           self._ti_data.iat[-1, 0] > 80.:
            return TRADE_SIGNALS['Sell']
            
        # A buy signal occurs when an increasing %K line crosses above the %D line in the 
        # oversold region (%K < 20.)
        if self._ti_data.iat[-2, 0] - self._ti_data.iat[-1, 0] < 0. and\
           self._ti_data.iat[-1, 0] - self._ti_data.iat[-1, 1] > 0. and\
           self._ti_data.iat[-1, 0] < 20.:
            return TRADE_SIGNALS['Buy']
        
        return TRADE_SIGNALS['Hold']


class RSI(TI):
    '''
    Relative Strength Index (RSI) Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains the following column: 'Adj Close'
            
        look_back (int): Look back days for calculating the averages needed by
            the indicator. Default value is 14.

    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        - TypeError
        - ValueError
        
    '''
    def __init__(self, df_data, look_back = 14):
        
        # Validate the input data, check tradingti.utils._data_validation module
        # for details
        data_validation = validateStockData(df_data)
        if data_validation is not None:
            raise(TypeError(data_validation))
            
        # Validate that all required input data are available
        if 'Adj Close' not in df_data.columns:
            raise(ValueError('Input \'Adj Close\' data are missing for BB ' +\
                'indicator use. Mandatory input data are: \'Adj Close\'.'))
                
        if type(look_back) != int or look_back <= 0 or \
            look_back > len(df_data.index):
            raise(ValueError('\'look_back\' argument should be a positive ' +\
                'integer less than the number of input periods (' +\
                str(len(df_data.index))+ '), but look_back = ' +\
                str(look_back) + '.'))
                
        self._look_back = look_back
            
        # Sort the input data and fill the missing values if any
        df_data = fillMissingValues(df_data)

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)
        super().__init__(input_data = df_data['Adj Close'], 
            ti_data = self._calculateIndicator(df_data),
            indicator_name = 'RSI-' + str(self._look_back), 
            lines_color = ['cornflowerblue', 'tomato'], subplots = True)
            
    
    def _calculateIndicator(self, input_data):
        
        '''
        Calculates the RSI for the given input data.
            
        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.
                
            RSI = 100 – [100 / ( 1 + (Average of Upward Price Change / 
                Average of Downward Price Change ) ) ]

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains one column 'RSI'.
        '''

        rsi = pd.DataFrame(data = None, index = input_data.index, 
            columns = ['RSI'])
    
        # Calculate RSI for each period (first look_back periods are skipped)
        for i in range (self._look_back, len(input_data.index)):
            
            # Initialize for each look_back period
            upward_price_change = 0
            downward_price_change = 0

            # Calculate the total upward and downward changes in the look_back
            # period
            for t in range(i - self._look_back+1, i+1):

                delta = input_data.iat[t, 0] - input_data.iat[t-1, 0]
     
                if delta >= 0.:
                    upward_price_change += delta
                else:
                    downward_price_change -= delta

            # Calculate the averages for upward and downward changes
            upward_average = upward_price_change/self._look_back
            downward_average = downward_price_change/self._look_back
            
            # Set RSI for the day i
            if downward_average == 0.:
                rsi.iat[i, 0] = 100
            else:           
                rsi.iat[i, 0] = 100-(100/(1+(upward_average/downward_average)))
        
        return rsi        

        
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

        # Overbought region
        if self._ti_data.iat[-2, 0] < 70. and self._ti_data.iat[-1, 0] > 70.:
            return TRADE_SIGNALS['Sell']
        
        # Oversold region
        if self._ti_data.iat[-2, 0] > 30. and self._ti_data.iat[-1, 0] < 30.:
            return TRADE_SIGNALS['Buy']
        
        return TRADE_SIGNALS['Hold']
