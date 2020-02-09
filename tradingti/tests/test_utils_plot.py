'''
File name: test_utils_plot.py
    Trading Technical Indicators open source library, unit testing.
    Test cases for the tradingti.utils._plot module.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 09.02.2020

Python Version: 3.6
'''

import unittest
import tradingti.utils as ut
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class TestLinesGraph(unittest.TestCase):
    
    def test_input_argument_missing(self):
    
        with self.assertRaises(TypeError):
            ut.linesGraph()


    def test_input_argument_wrong_type(self):
        
        with self.assertRaises(TypeError):
            ut.linesGraph(1)
            
            
    def test_input_argument_index_wrong_type(self):
        
        df = pd.DataFrame(index = range(3), columns = ['A1', 'A2'], 
            data = [[1,1], [2,2], [3,3]])

        with self.assertRaises(TypeError):
            ut.linesGraph(df)
            
            
    def test_input_argument_two_dfs(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertIsNotNone(ut.linesGraph([df, df]))
            
    
    def test_input_argument_three_dfs(self):
        
        df = pd.DataFrame(index = range(3), columns = ['A1', 'A2'], 
            data = [[1,1], [2,2], [3,3]])

        with self.assertRaises(TypeError):
            ut.linesGraph([df, df, df])
            
    
    def test_input_argument_title(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertEqual(ut.linesGraph(df, title = 'test title').gca().
            get_title(), 'test title')
        
        
    def test_input_argument_x_label(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertEqual(ut.linesGraph(df, x_label = 'test x label').gca().
            get_xlabel(), 'test x label')
        
        
    def test_input_argument_y_label(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])
        
        self.assertEqual(ut.linesGraph(df, y_label = 'test y label').gca().
            get_ylabel(), '')
            
        # Check if possible to verify text
        
        
    def test_input_argument_lines_color(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertIsNotNone(ut.linesGraph([df, df], lines_color = ['blue', 
            'red']))
        
        
    def test_input_argument_lines_width(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertIsNotNone(ut.linesGraph([df, df], lines_width = [1, 0.5]))
        
        
    def test_input_argument_lines_style(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertIsNotNone(ut.linesGraph([df, df], lines_style = ['-', '-.']))
        
        
    def test_input_argument_alpha_values(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertIsNotNone(ut.linesGraph([df, df], alpha_values = [0.5, 1]))
    
    
    def test_input_argument_areas(self):
        
        df = pd.DataFrame(index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', 
            '2018-01-03']), columns = ['A1', 'A2'], data = [[1,1], [2,2], 
            [3,3]])

        self.assertIsNotNone(ut.linesGraph([df, df], areas = 
            [{'x': ['2018-01-01', '2018-01-02'], 'y1': [1.,1.], 'y2': [3., 3.], 
            'color': 'red'}])) 

if __name__ == '__main__':
    unittest.main()