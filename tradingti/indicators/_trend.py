'''
File name: _technical_indicator.py
    Trend type technical indicators implementation.
    Implements the following technical indicators:
    - Simple Moving Average (SMA class)
    - Exponential Moving Average (EMA class)
    - Moving Average Convergence Divergence (MACD class)
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

import pandas as pd
from ._average_technical_indicator import AverageTI
from ._technical_indicator import TI
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues


class SMA(AverageTI):
    '''
    SMA Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains one column with the Adjusted
            Closed price of a given stock.
                
        sma_periods (object): The sma periods for which the rolling mean of the
            input data should be calculated. Is a list of integers, with one 
            (representing the long term SMA) or two (representing the short term
            and the long term SMA) members at most. Default values are [50, 200]
            50 for the short term and 200 for the long term.

    Attributes:            
        _sma_periods (list of integers): The rolling mean windows.
                                
    Methods:
        _calculateSMA(): Calculates the SMA for the given input data.
        
    Raises:
        -
        
    '''
    def __init__(self, df_data, sma_periods = [50, 200]):

        self._sma_periods = sma_periods
        
        if len(sma_periods) == 1:
            lines_color = ['rosybrown', 'g']
        else:
            lines_color = ['rosybrown', 'g', 'royalblue']
        
        super().__init__(df_data = df_data, calculate_MA = self._calculateSMA,
            indicator_name = 'SMA-' + str(sma_periods), 
            lines_color = lines_color, periods = sma_periods)
        
    
    def _calculateSMA(self, input_data):
        '''
        Calculates the SMA for the given input data.
    
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
    
        sma = pd.DataFrame(index = input_data.index)
        
        # Calculate SMA for each requested rolling window (concat results to a 
        # single dataframe)
        for sma_period in self._sma_periods:
            sma = pd.concat([sma, input_data.rolling(window = sma_period, 
                min_periods = 1, center = False, win_type = None, on = None, 
                axis = 0, closed = None).mean()], axis = 1)
        
        sma.columns = ['SMA-' + str(x) for x in self._sma_periods]
            
        return sma

         
class EMA(AverageTI):
    '''
    EMA Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains one column with the Adjusted
            Closed price of a given stock.
                
        span_periods (object): The span periods from which the decay is 
            calculated. Is a list of integers, with one (representing the long 
            term EMA) or two (representing the short term and the long term EMA)
            members at most. Default values are [26, 200], 26 for the short term
            and 200 for the long term.

    Attributes:
        _span_periods (list of integers): The span periods.
                                
    Methods:
        _calculateEMA(): Calculates the EMA for the given input data.
        
    Raises:
        -
        
    '''
    def __init__(self, df_data, span_periods = [26, 200]):
        
        self._span_periods = span_periods

        if len(span_periods) == 1:
            lines_color = ['rosybrown', 'g']
        else:
            lines_color = ['rosybrown', 'g', 'royalblue']
        
        super().__init__(df_data = df_data, calculate_MA = self._calculateEMA,
            indicator_name = 'EMA-' + str(span_periods),
            lines_color = lines_color, periods = span_periods)
        
    
    def _calculateEMA(self, input_data):
        '''
        Calculates the EMA for the given input data.
    
        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains one or two
                columns depending the requested ema periods.
        '''
    
        ema = pd.DataFrame(index = input_data.index)
        
        # Calculate EMA for each requested span period (concat results to a 
        # single dataframe)
        for span_period in self._span_periods:
            ema = pd.concat([ema, input_data.ewm(span = span_period,
                min_periods = 0, adjust = True, axis = 0).mean()], axis = 1)
        
        ema.columns = ['EMA-' + str(x) for x in self._span_periods]
            
        return ema
        
        
class MACD(TI):
    '''
    Moving Average Convergence Divergence (MACD) Technical Indicator class 
    implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains the below columns:
            'Adj Close'

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
        if 'Adj Close' not in df_data.columns:
            raise(ValueError('Input \'Adj Close\' data are missing for MACD ' +\
                'indicator use. Mandatory input data are: \'Adj Close\'.'))
            
        # Sort the input data and fill the missing values if any
        df_data = fillMissingValues(df_data)

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)
        super().__init__(input_data = df_data['Adj Close'], 
            ti_data = self._calculateIndicator(df_data['Adj Close']),
            indicator_name = 'MACD', lines_color = ['cornflowerblue', 'tomato', 
            'limegreen'], subplots = True)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the MACD for the given input data.
        
        MACD = EMA_26 - EMA_12
        Signal Line = EMA_9
    
        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains two columns, the
                'MACD' and the 'Signal Line'.
        '''
        
        EMA_26 = EMA(input_data.to_frame(), span_periods = [26]).getTiData()
        EMA_26.columns = ['EMA']
        
        EMA_12 = EMA(input_data.to_frame(), span_periods = [12]).getTiData()
        EMA_12.columns = ['EMA']
        
        macd = EMA_12.subtract(EMA_26)
        macd.columns = ['Adj Close'] # For calling EMA below
        
        signal_line = EMA(macd, span_periods = [9]).getTiData()
        
        # Indicator holds the MACD and the Signal Line data
        macd = pd.concat([macd, signal_line], axis = 1)
        macd.columns = ['MACD', 'Signal Line']
        
        return macd  
        
        
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
        
        signal = 0
        
        # MACD crossing above zero is considered bullish, while crossing below 
        # zero is bearish. 
        if self._ti_data.iat[-2, 0] < 0. and self._ti_data.iat[-1, 0] > 0.:
            signal += TRADE_SIGNALS['BUY']
            
        if self._ti_data.iat[-2, 0] > 0. and self._ti_data.iat[-1, 0] < 0.:
            signal += TRADE_SIGNALS['SELL']

        # MACD turns up from below zero it is considered bullish.
        # MACD turns down from above zero it is considered bearish.
        if  self._ti_data.iat[-2, 0] <  self._ti_data.iat[-1, 0] and\
            self._ti_data.iat[-1, 0] < 0.:
            signal += TRADE_SIGNALS['BUY']
        
        if  self._ti_data.iat[-2, 0] >  self._ti_data.iat[-1, 0] and\
            self._ti_data.iat[-1, 0] > 0.:
            signal += TRADE_SIGNALS['SELL']
           
        # When the MACD line crosses from below to above the signal line, the 
        # indicator is considered bullish.
        if self._ti_data.iat[-2, 0] < self._ti_data.iat[-2, 1] and\
           self._ti_data.iat[-1, 0] > self._ti_data.iat[-1, 1]:
           signal += TRADE_SIGNALS['BUY']

        # When the MACD line crosses from above to below the signal line, the 
        # indicator is considered bearish.
        if self._ti_data.iat[-2, 0] > self._ti_data.iat[-2, 1] and\
           self._ti_data.iat[-1, 0] < self._ti_data.iat[-1, 1]:
           signal += TRADE_SIGNALS['SELL']

        # Signal voting
        if signal <= -1:
            signal = TRADE_SIGNALS['BUY']
        elif signal >= 1:
            signal = TRADE_SIGNALS['SELL']
        
        return signal
