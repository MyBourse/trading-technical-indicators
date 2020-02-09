'''
File name: _technical_indicator.py
    Trend type technical indicators implementation.
    Implements the following technical indicators:
    - Simple Moving Average (SMA class)
    - Exponential Moving Average (EMA class)
    - Moving Average Convergence Divergence (MACD class)
    - Average Directional Movement Index (ADX class)
    - Directional Movement Index (DMI class)
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 06.02.2020

Python Version: 3.6
'''

import pandas as pd
from .._constants import *
from ._average_technical_indicator import AverageTI
from ._technical_indicator import TI
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues


class SMA(AverageTI):
    '''
    SMA Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. The indicator requires the following stock
            data: 'Adj Close'
                
        sma_periods (object): The sma periods for which the rolling mean of the
            input data should be calculated. Is a list of integers, with one 
            (representing the long term SMA) or two (representing the short term
            and the long term SMA) members at most. Default values are [50, 200]
            50 for the short term and 200 for the long term.
            
    Attributes:
        _sma_periods (object): The sma periods for which the rolling mean of the
            input data should be calculated.
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data, sma_periods = [50, 200]):

        self._sma_periods = sma_periods
        
        if len(sma_periods) == 1:
            lines_color = ['black', 'cornflowerblue']
        else:
            lines_color = ['black', 'cornflowerblue', 'tomato']
        
        super().__init__(df_data = df_data, calculate_MA = 
            self._calculateIndicator, indicator_name = 'SMA-' + \
            str(sma_periods), lines_color = lines_color, periods = sma_periods)
        
    
    def _calculateIndicator(self, input_data):
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
            Index is of type date. The indicator requires the following stock
            data: 'Adj Close'
                
        span_periods (object): The span periods from which the decay is 
            calculated. Is a list of integers, with one (representing the long 
            term EMA) or two (representing the short term and the long term EMA)
            members at most. Default values are [26, 200], 26 for the short term
            and 200 for the long term.

    Attributes:
        _span_periods (object): The span periods from which the decay is 
            calculated.
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data, span_periods = [26, 200]):
        
        self._span_periods = span_periods

        if len(span_periods) == 1:
            lines_color = ['black', 'cornflowerblue']
        else:
            lines_color = ['black', 'cornflowerblue', 'tomato']
        
        super().__init__(df_data = df_data, calculate_MA = 
            self._calculateIndicator, indicator_name = 'EMA-' + \
            str(span_periods), lines_color = lines_color, periods = 
            span_periods)
        
    
    def _calculateIndicator(self, input_data):
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
            Index is of type date. The indicator requires the following stock
            data: 'Adj Close'

    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data):
        
        # Validate and tranform the input data, check tradingti.utils.
        # _data_validation module for more details
        input_data = validateStockData(data = df_data, required_columns = 
            ['Adj Close'], indicator_name = 'MACD')

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)    
        super().__init__(input_data = input_data, 
            ti_data = self._calculateIndicator(input_data),
            indicator_name = 'MACD', plotted_input_columns = ['Adj Close'], 
            y_label = 'MACD | Price', lines_color = ['black', 'cornflowerblue', 
            'tomato'], subplots = True)

        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the MACD technical indicator for the given input data.
    
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
        
        EMA_26 = EMA(input_data, span_periods = [26]).getTiData()
        EMA_26.columns = ['EMA']
        
        EMA_12 = EMA(input_data, span_periods = [12]).getTiData()
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
            tuple (string, integer): The Trading signal. Possible values are 
            ('Hold', 0), ('Buy', -1), ('Sell', 1). See TRADE_SIGNALS package 
            constant.
        '''
        
        signal = 0
        
        # MACD crossing above zero is considered bullish, while crossing below 
        # zero is bearish. 
        if self._ti_data.iat[-2, 0] < 0. and self._ti_data.iat[-1, 0] > 0.:
            signal += TRADE_SIGNALS['Buy']
            
        if self._ti_data.iat[-2, 0] > 0. and self._ti_data.iat[-1, 0] < 0.:
            signal += TRADE_SIGNALS['Sell']

        # MACD turns up from below zero it is considered bullish.
        # MACD turns down from above zero it is considered bearish.
        if  self._ti_data.iat[-2, 0] <  self._ti_data.iat[-1, 0] and\
            self._ti_data.iat[-1, 0] < 0.:
            signal += TRADE_SIGNALS['Buy']
        
        if  self._ti_data.iat[-2, 0] >  self._ti_data.iat[-1, 0] and\
            self._ti_data.iat[-1, 0] > 0.:
            signal += TRADE_SIGNALS['Sell']
           
        # When the MACD line crosses from below to above the signal line, the 
        # indicator is considered bullish.
        if self._ti_data.iat[-2, 0] < self._ti_data.iat[-2, 1] and\
           self._ti_data.iat[-1, 0] > self._ti_data.iat[-1, 1]:
           signal += TRADE_SIGNALS['Buy']

        # When the MACD line crosses from above to below the signal line, the 
        # indicator is considered bearish.
        if self._ti_data.iat[-2, 0] > self._ti_data.iat[-2, 1] and\
           self._ti_data.iat[-1, 0] < self._ti_data.iat[-1, 1]:
           signal += TRADE_SIGNALS['Sell']

        # Signal voting
        if signal <= -1:
            signal = TRADE_SIGNALS['Buy']
        elif signal >= 1:
            signal = TRADE_SIGNALS['Sell']
        
        return (list(TRADE_SIGNALS.keys())[list(TRADE_SIGNALS.values()).
            index(signal)], signal)
  

class DMI(TI):
    '''
    Directional Movement Index (DMI) Technical Indicator class 
    implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. The indicator requires the following stock
            data: 'High', 'Low', 'Close', 'Adj Close'
    
    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data):
        
        # Validate and tranform the input data, check tradingti.utils.
        # _data_validation module for more details
        input_data = validateStockData(data = df_data, required_columns = 
            ['High', 'Low', 'Close', 'Adj Close'], indicator_name = 'DMI')

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)    
        super().__init__(input_data = input_data, 
            ti_data = self._calculateIndicator(input_data),
            indicator_name = 'DMI', plotted_input_columns = ['Adj Close'], 
            y_label = 'DMI | Price', lines_color = ['black', 'limegreen', 'red',
            'cornflowerblue'], alpha_values = [1.0, 1.0, 1.0, 0.2], 
            subplots = True)

        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the DMI technical indicator for the given input data.
    
        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains three columns, the
                'DMI+', 'DMI-' and the 'DX'.
        '''
        
        dmi = pd.DataFrame(index = input_data.index, columns = ['DI+', 'DI-', 
            'DMI+', 'DMI-', 'True Range', 'Smoothed True Range', 'DX'], 
            data = None)
        
        dmi.iloc[0,0:2] = 0.0
        for i in range(1, len(input_data.index)):
            
            dmi.iat[i,4] =  max(input_data.iat[i,0] - input_data.iat[i,1],
                abs(input_data.iat[i,0] - input_data.iat[i-1, 2]),
                abs(input_data.iat[i,1] - input_data.iat[i-1, 2]))
                
            if input_data.iat[i,0] - input_data.iat[i-1,0] > \
                input_data.iat[i-1,1] - input_data.iat[i,1]:
                dmi.iat[i,0] = input_data.iat[i,0] - input_data.iat[i-1,0]
            else:
                dmi.iat[i,0] = 0.0
            
            if input_data.iat[i,0] - input_data.iat[i-1,0] < \
                input_data.iat[i-1,1] - input_data.iat[i,1]:
                dmi.iat[i,1] = input_data.iat[i-1,1] - input_data.iat[i,1]
            else:
                dmi.iat[i,1] = 0.0
                
            if i == 5:
                dmi.iat[i,2] = dmi.iloc[i-5:i,0].sum()
                dmi.iat[i,3] = dmi.iloc[i-5:i,1].sum()
                dmi.iat[i,5] = dmi.iloc[i-5:i,4].sum()
            elif i > 5:
                dmi.iat[i,2] = dmi.iat[i-1,2] - dmi.iat[i-1,2]/5. + dmi.iat[i,0]
                dmi.iat[i,3] = dmi.iat[i-1,3] - dmi.iat[i-1,3]/5. + dmi.iat[i,1]
                dmi.iat[i,5] = dmi.iat[i-1,5] - dmi.iat[i-1,5]/5. + dmi.iat[i,4]
                
        for i in range(5, len(input_data.index)):
            dmi.iat[i,2] = 100*dmi.iat[i,2]/dmi.iat[i,5]
            dmi.iat[i,3] = 100*dmi.iat[i,3]/dmi.iat[i,5]
            dmi.iat[i,6] = 100*(abs(dmi.iat[i,2] - dmi.iat[i,3]))/(dmi.iat[i,2] 
                + dmi.iat[i,3])
        
        return dmi.drop(columns = ['DI+', 'DI-', 'True Range', 
            'Smoothed True Range'])
                  
        
    def getSignal(self):
        '''
        Calculates and returns the signal of the technical indicator.
    
        Args:
            -

        Raises:
            -

        Returns:
            tuple (string, integer): The Trading signal. Possible values are 
            ('Hold', 0), ('Buy', -1), ('Sell', 1). See TRADE_SIGNALS package 
            constant.
        '''
        
        # A buy signal is given when DMI+ crosses above DMI-
        # A sell signal is given when DMI- crosses above DMI+
        if self._ti_data.iat[-2,0] > self._ti_data.iat[-2,1] and \
            self._ti_data.iat[-1,0] < self._ti_data.iat[-1,1]:
            return ('Sell', TRADE_SIGNALS['Sell'])
            
        elif self._ti_data.iat[-2,0] < self._ti_data.iat[-2,1] and \
            self._ti_data.iat[-1,0] > self._ti_data.iat[-1,1]:
            return ('Buy', TRADE_SIGNALS['Buy'])
            
        else:
            return ('Hold', TRADE_SIGNALS['Hold'])


class ADX(TI):
    '''
    Average Directional Movement Index (ADX) Technical Indicator class 
    implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. The indicator requires the following stock
            data: 'High', 'Low', 'Close', 'Adj Close'
            
    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data):
        
        # Validate and tranform the input data, check tradingti.utils.
        # _data_validation module for more details
        input_data = validateStockData(data = df_data, required_columns = 
            ['High', 'Low', 'Close', 'Adj Close'], indicator_name = 'ADX')

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)    
        super().__init__(input_data = input_data, 
            ti_data = self._calculateIndicator(input_data),
            indicator_name = 'ADX', plotted_input_columns = ['Adj Close'], 
            y_label = 'ADX | Price', lines_color = ['black', 'cornflowerblue'],
            subplots = True)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the ADX technical indicator for the given input data.
    
        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains a column, the
                'ADX'.
        '''
        
        adx = DMI(input_data).getTiData()['DX'].to_frame().rolling(window = 5, 
            min_periods = 1, center = False, win_type = None, on = None, 
            axis = 0, closed = None).mean()
        
        adx.columns = ['ADX']
        
        return adx
        
        
    def getSignal(self):
        '''
        Calculates and returns the signal of the technical indicator.
    
        Args:
            -

        Raises:
            -

        Returns:
            tuple (string, integer): The Trading signal. Possible values are 
            ('Hold', 0), ('Buy', -1), ('Sell', 1). See TRADE_SIGNALS package 
            constant.
        '''

        # Price drops and strong trend
        if self._input_data.iat[-3,0] > self._input_data.iat[-2,0] and \
            self._input_data.iat[-2,0] > self._input_data.iat[-1,0] and\
            self._ti_data.iat[-1,0] > 25:
            return ('Sell', TRADE_SIGNALS['Sell'])
            
        # Price raises and strong trend
        elif self._input_data.iat[-3,0] < self._input_data.iat[-2,0] and\
            self._input_data.iat[-2,0] < self._input_data.iat[-1,0] and\
            self._ti_data.iat[-1,0] > 25:
            return ('Buy', TRADE_SIGNALS['Buy'])
            
        else:
            return ('Hold', TRADE_SIGNALS['Hold'])
