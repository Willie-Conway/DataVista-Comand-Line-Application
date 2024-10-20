import unittest
import pandas as pd
from my_data_scientist import MyDataScientist

class TestMyDataScientist(unittest.TestCase):
    def setUp(self):
        self.app = MyDataScientist()
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
        self.app.machine_learning(target_column)

    def test_visualization(self):
        # Assuming you have a column 'Store' to visualize
        column_to_visualize = 'Store'
        chart_type = '1'  # Histogram
        self.app.visualize_data(column_to_visualize, chart_type)

if __name__ == '__main__':
    unittest.main()
