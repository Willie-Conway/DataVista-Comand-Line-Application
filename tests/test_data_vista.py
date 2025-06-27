# test_data_vista.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import pandas as pd
# from src.data_vista import DataVista
from data_vista import DataVista


class TestDataVista(unittest.TestCase):
    def setUp(self):
        self.app = DataVista()
        self.app.load_data('data/test_data_with_duplicates.csv')  # Ensure you have the sample data available

    def test_load_data(self):
        self.assertIsNotNone(self.app.data)
        self.assertTrue(isinstance(self.app.data, pd.DataFrame))

    def test_preprocess_data(self):
        self.app.preprocess_data()
        self.assertFalse(self.app.data.isnull().values.any())

    def test_clean_data(self):
        original_shape = self.app.data.shape
        self.app.clean_data()
        self.assertLess(self.app.data.shape[0], original_shape[0])  # Expecting some rows to be removed

    def test_train_model(self):
        # Assuming 'Weekly_Sales' is the target column in your sample data
        target_column = 'Weekly_Sales'
        self.app.clean_data()
        self.app.preprocess_data()
        result = self.app.machine_learning(target_column, algorithm='linear_regression')  # Update to include algorithm
        self.assertIsNotNone(result)

    def test_visualization(self):
        # Assuming you have a column 'Store' to visualize
        column_to_visualize = 'Store'
        chart_type = '1'  # Histogram
        self.app.visualize_data(column_to_visualize, chart_type)

    def test_save_load_model(self):
        target_column = 'Weekly_Sales'
        self.app.clean_data()
        self.app.preprocess_data()
        self.app.machine_learning(target_column, algorithm='linear_regression')
        
        # Test saving the model
        self.app.machine_learning.save_model('test_model.pkl')  # Ensure the save_model method is implemented
        self.assertTrue(os.path.exists('test_model.pkl'))
        
        # Test loading the model
        loaded_model = self.app.machine_learning.load_model('test_model.pkl')  # Ensure the load_model method is implemented
        self.assertIsNotNone(loaded_model)

if __name__ == '__main__':
    unittest.main()
