'''
File name: test_utils_data_preprocessing.oy
    Trading Technical Indicators open source library, unit testing.
    Test cases for the tradingti.utils._data_preprocessing module.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 09.02.2020

Python Version: 3.6
'''

import unittest
import tradingti.utils as ut
import pandas as pd

class TestFillMissingValues(unittest.TestCase):
    
    def test_input_argument_missing(self):
    
        with self.assertRaises(TypeError):
            ut.fillMissingValues()


    def test_input_argument_wrong_type(self):
        
        self.assertEqual(ut.fillMissingValues(1), 1)
            
    
    def test_input_argument_empty_dataframe(self):
        
        df = pd.DataFrame(index = range(10), columns = ['A'], data = None, 
            dtype = float)
        
        pd.testing.assert_frame_equal(ut.fillMissingValues(df) , df) 
            
            
    def test_result_input_sorted(self):

        df = pd.DataFrame(index = range(10), columns = ['A'], 
            data = [None, None, 3., 4., None, None, 7., 8., 9., None])
        
        df_res = pd.DataFrame(index = range(10), columns = ['A'], 
            data = [3., 3., 3., 4., 4., 4., 7., 8., 9., 9.])
        
        pd.testing.assert_frame_equal(ut.fillMissingValues(df) , df_res)

    
    def test_result_input_not_sorted(self):
                                                             
        df = pd.DataFrame(index = [3,4,2,1,5,6,7,9,8, 0], columns = ['A'], 
            data = [None, None, 3., 4., None, None, 7., 8., 9., None])
            
        df_res = pd.DataFrame(index = range(10), columns = ['A'], 
            data = [4., 4., 3., 3., 3., 3., 3., 7., 9., 8.])
        
        pd.testing.assert_frame_equal(ut.fillMissingValues(df) , df_res)
        
    
    def test_result_input_multiple_columns(self):
                                                             
        df = pd.DataFrame(index = range(5), columns = ['A', 'B', 'C'], 
            data = [[None, 0., 0.], [1., None, 1.], [2., None, 2.], 
                [3., 3., None], [4., 4., None]])
            
        df_res = pd.DataFrame(index = range(5), columns = ['A', 'B', 'C'], 
            data = [[1., 0., 0.], [1., 0., 1.], [2., 0., 2.], [3., 3., 2.], 
                [4., 4., 2.]])
        
        pd.testing.assert_frame_equal(ut.fillMissingValues(df) , df_res)
        

if __name__ == '__main__':
    unittest.main()