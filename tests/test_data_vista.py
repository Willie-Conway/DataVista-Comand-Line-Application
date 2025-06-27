# test_data_vista.py
import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import pandas as pd
from data_vista import DataVista


class TestDataVista(unittest.TestCase):
    def setUp(self):
        self.app = DataVista()
        self.app.load_data('data/test_data_with_duplicates.csv')  # Ensure this file exists for testing

    def test_load_data(self):
        self.assertIsNotNone(self.app.data)
        self.assertTrue(isinstance(self.app.data, pd.DataFrame))

    @patch('builtins.input', side_effect=['3'])  # Skip missing value handling or adjust as needed
    def test_preprocess_data(self, mock_input):
        self.app.preprocess_data()
        self.assertFalse(self.app.data.isnull().values.any())

    @patch('builtins.input', side_effect=['3'])  # Skip cleaning input prompts
    def test_clean_data(self, mock_input):
        original_shape = self.app.data.shape
        self.app.clean_data()
        self.assertLess(self.app.data.shape[0], original_shape[0])  # Expect rows removed after cleaning

    @patch('builtins.input', side_effect=['3'])  # Skip inputs during clean and preprocess
    def test_train_model(self, mock_input):
        target_column = 'Weekly_Sales'
        self.app.clean_data()
        self.app.preprocess_data()
        result = self.app.machine_learning(target_column, algorithm='linear_regression')
        self.assertIsNotNone(result)

    @patch('builtins.input', side_effect=['n'])  # Mock input for axis naming prompt in visualization
    def test_visualization(self, mock_input):
        # Assuming you have a column 'Store' to visualize
        column_to_visualize = ['Store']  # should be a list if your visualize_data expects list
        chart_type = '1'  # Histogram
        self.app.visualize_data(column_to_visualize, chart_type)

    @patch('builtins.input', side_effect=['3'])  # Skip inputs during clean and preprocess
    def test_save_load_model(self, mock_input):
        target_column = 'Weekly_Sales'
        self.app.clean_data()
        self.app.preprocess_data()
        self.app.machine_learning(target_column, algorithm='linear_regression')

        # Save the model (assuming method exists)
        self.app.ml.save_model('test_model.pkl')
        self.assertTrue(os.path.exists('test_model.pkl'))

        # Load the model (assuming method exists)
        loaded_model = self.app.ml.load_model('test_model.pkl')
        self.assertIsNotNone(loaded_model)

        # Clean up saved model file
        if os.path.exists('test_model.pkl'):
            os.remove('test_model.pkl')


if __name__ == '__main__':
    unittest.main()
