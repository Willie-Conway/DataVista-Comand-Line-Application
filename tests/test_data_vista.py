# test_data_vista.py
import sys
import os
from unittest.mock import patch
import unittest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_vista import DataVista


class TestDataVista(unittest.TestCase):
    def setUp(self):
        self.app = DataVista()
        self.app.load_data('data/test_data_with_duplicates.csv')  # Ensure this file exists for testing

    def test_load_data(self):
        self.assertIsNotNone(self.app.data)
        self.assertTrue(isinstance(self.app.data, pd.DataFrame))

    @patch('builtins.input', side_effect=[
        '3',  # Choose to skip missing value handling
        '2',  # Do not scale features
        '2',  # Keep outliers
    ])
    def test_preprocess_data(self, mock_input):
        self.app.preprocess_data()
        self.assertFalse(self.app.data.isnull().values.any())

    @patch('builtins.input', side_effect=[
        '3'  # Skip missing value handling during clean_data
    ])
    def test_clean_data(self, mock_input):
        original_shape = self.app.data.shape
        self.app.clean_data()
        # Cleaning might remove rows, so expect less rows after cleaning
        self.assertLessEqual(self.app.data.shape[0], original_shape[0])

    @patch('builtins.input', side_effect=[
        '3',  # Skip missing value handling (preprocess_data)
        '2',  # Do not scale features
        '2',  # Keep outliers
        '3'   # Skip missing value handling (clean_data)
    ])
    def test_train_model(self, mock_input):
        target_column = 'Weekly_Sales'
        self.app.clean_data()
        self.app.preprocess_data()
        self.app.machine_learning(target_column, algorithm='linear_regression')
        self.assertIsNotNone(self.app.ml)
        self.assertIsNotNone(self.app.ml.model)

    @patch('builtins.input', side_effect=[
        'n',  # Do not name x-axis and y-axis
        'n',  # Do not add title to the chart
        '',   # Use default color palette (empty input)
    ])
    def test_visualization(self, mock_input):
        column_to_visualize = ['Store']  # Make sure this column exists
        chart_type = '1'  # Histogram
        self.app.visualize_data(column_to_visualize, chart_type)

    @patch('builtins.input', side_effect=[
        '3',  # Skip missing value handling (preprocess_data)
        '2',  # Do not scale features
        '2',  # Keep outliers
        '3'   # Skip missing value handling (clean_data)
    ])
    def test_save_load_model(self, mock_input):
        target_column = 'Weekly_Sales'
        self.app.clean_data()
        self.app.preprocess_data()
        self.app.machine_learning(target_column, algorithm='linear_regression')

        # Save the model
        self.app.ml.save_model('test_model.pkl')
        self.assertTrue(os.path.exists('test_model.pkl'))

        # Load the model
        self.app.ml.load_model('test_model.pkl')
        self.assertIsNotNone(self.app.ml.model)

        # Cleanup
        if os.path.exists('test_model.pkl'):
            os.remove('test_model.pkl')


if __name__ == '__main__':
    unittest.main()
