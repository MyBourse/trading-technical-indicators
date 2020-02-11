'''
File name: test_indicators_ema.py
    Trading Technical Indicators open source library, unit testing.
    Test cases for the EMA technical indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 10.02.2020

Python Version: 3.6
'''

import unittest
from tradingti.indicators import EMA

import matplotlib
import pandas as pd

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

date_parser = lambda x: pd.to_datetime(x, format = '%y/%m/%d')

# DataFrames definition
empty_data = pd.DataFrame(index = pd.DatetimeIndex([]), columns = ['Adj Close'], 
    data = None)

wrong_data_type = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', 
    '2018-01-02']), columns = ['Adj Close'], data = ['hi', 'there'])

missing_data = pd.read_csv('./tradingti/tests/data/missing_data.csv', 
    parse_dates = ['Date'], index_col = 0, date_parser = date_parser)
    
missing_data_filled = pd.read_csv('./tradingti/tests/data/missing_data_filled.csv', 
    parse_dates = ['Date'], index_col = 0, date_parser = date_parser)
    
full_data = pd.read_csv('./tradingti/tests/data/full_data.csv', 
    parse_dates = ['Date'], index_col = 0, date_parser = date_parser)


class TestEMA(unittest.TestCase):

    # Validate data input argument
    
    def test_data_missing(self):
    
        with self.assertRaises(TypeError):
            EMA()
            
    
    def test_data_wrong_type(self):
    
        with self.assertRaises(TypeError):
            EMA(1)


    def test_data_wrong_index_type(self):
    
        with self.assertRaises(TypeError):
            EMA(pd.DataFrame(index = [0], columns = ['A'], data = [1]))

    
    def test_data_required_columns_missing(self):
    
        with self.assertRaises(ValueError):
            EMA(pd.DataFrame(full_data.drop(columns = ['Adj Close'])))
            
            
    def test_data_empty(self):
    
        with self.assertRaises(ValueError):
            EMA(empty_data)
            
    
    def test_data_values_wrong_type(self):
    
        with self.assertRaises(ValueError):
            EMA(wrong_data_type)
            
    # Validate sma_periods input argument
    
    def test_sma_periods_single_value(self):
        
        EMA(full_data, 10)
        
    
    def test_sma_periods_empty(self):
        
        with self.assertRaises(ValueError):
            EMA(full_data, [])
    
    
    def test_sma_periods_invalid_value(self):
    
        with self.assertRaises(ValueError):
            EMA(full_data, ['hi'])
        
        
    def test_sma_periods_more_than_data(self):
    
        with self.assertRaises(ValueError):
            EMA(missing_data_filled, [50, 200])
    
    
    def test_one_input_period(self):
        
        EMA(full_data, [10])
    
    
    def test_two_input_periods(self):
        
        EMA(full_data, [10, 20])
    
    
    def test_three_input_periods(self):
        
        with self.assertRaises(ValueError):
            EMA(full_data, [10, 20, 30])
    
    # Validate indicator creation
    
    def test_validate_stock_data_missing_values(self):

        pd.testing.assert_frame_equal(EMA(missing_data, [10])._input_data, 
            missing_data_filled['Adj Close'].to_frame().sort_index(ascending = True))
            
            
    def test_validate_stock_data_full_values(self):

        pd.testing.assert_frame_equal(EMA(full_data, [10])._input_data, 
            full_data['Adj Close'].to_frame().sort_index(ascending = True))

    
    # Validate API
    
    def test_getTiPlot(self):
        
        self.assertEqual(EMA(full_data, [10]).getTiPlot(), matplotlib.pyplot)
        
        
    def test_getTiData(self):
        
        expected_result = full_data['Adj Close'].to_frame().\
            sort_index(ascending = True).ewm(span = 10, 
            min_periods = 1).mean()
            
        expected_result.columns = ['EMA-10']
        
        pd.testing.assert_frame_equal(EMA(full_data, [10]).getTiData(),
            expected_result)


    def test_getTiValue_specific(self):
        
        expected_result = full_data['Adj Close'].to_frame().\
            sort_index(ascending = True).ewm(span = 10, 
            min_periods = 1).mean()
            
        expected_result.columns = ['EMA-10']

        self.assertEqual(EMA(full_data, [10]).getTiValue('2012-07-05'), 
            expected_result.loc['2012-07-05', 'EMA-10'])


    def test_getTiValue_latest(self):
        
        expected_result = full_data['Adj Close'].to_frame().\
            sort_index(ascending = True).ewm(span = 10, 
            min_periods = 1).mean()
            
        expected_result.columns = ['EMA-10']
            
        self.assertEqual(EMA(full_data, [10]).getTiValue(), 
            expected_result.loc['2012-09-12', 'EMA-10'])
    
    
    def test_getSignal(self):
        
        self.assertIn(EMA(full_data, [10]).getSignal(), 
            [('Buy', -1), ('Hold', 0), ('Sell', 1)])
        

if __name__ == '__main__':
    unittest.main()