# DataVista

![DataVista](https://tinypic.host/images/2024/10/20/DataVista.png)

## Overview

**DataVista** is a Python application designed to assist data analysts and scientists in making informed decisions using existing data. The app integrates functionalities for data loading, cleaning, preprocessing, statistical analysis, machine learning, and visualization, making it a comprehensive tool for data analysis.

## Features

### Core Features

- **Data Loading**:

  - Load data from a CSV file into a pandas DataFrame.
- **Data Cleaning**:

  - Remove duplicate rows.
  - Handle missing values by either removing them or filling them with specified values or the mean.
- **Data Preprocessing**:

  - Convert date columns to datetime format.
  - Forward-fill missing values in the dataset.
- **Data Splitting**:

  - Split the dataset into training and testing sets based on a specified target column.

### Data Wrangling

- Perform data cleaning to ensure data integrity and quality.

### Statistical Analysis

- Provide a statistical summary of numerical columns, including mean, median, mode, range, sample size, standard deviation, and confidence intervals.
- Conduct normality tests on specified columns.

### Machine Learning

- Train a simple linear regression model using numeric columns as features and a user-defined target column.
- Evaluate the model's performance using R² score.

### Visualization Options

1. **Distribution Plot**:

   - Visualize the distribution of a specified numeric column.
2. **Bar Chart**:

   - Create a bar chart for categorical data.
3. **Box Plot**:

   - Visualize the distribution of a numerical column grouped by a categorical column.
4. **Scatter Plot**:

   - Create a scatter plot to visualize the relationship between two numeric columns.
5. **Scatter Plot with Linear Regression**:

   - Generate a scatter plot that includes a linear regression line.
6. **Histogram**:

   - Display a histogram for the distribution of a specified numeric column.
7. **Pie Chart**:

   - Create a pie chart for a specified categorical column.

### User Interaction

- **Command-Line Interface**:

  - Allow users to input choices for visualization types and target columns interactively.
- **Logging**:

  - Provide logging for successful operations, warnings, and errors for better debugging and user awareness.

### Error Handling

- Handle various errors, such as:
  - File not found.
  - Empty datasets.
  - Invalid column names for visualizations.

### Default Settings

- Load a default dataset if no file path is provided.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `numpy`, `colorama`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Willie-Conway/DataVista.git
   cd DataVista
   ```

## Requirements

Make sure you have Python 3 installed. Install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your CSV file in the  `data/`  directory.
2. Run the app:

```bash
python src/data_vista.py
```

3. Follow the prompts to load data, preprocess, split, and  visualize.

### Running the App with a Specific File

To run the app with a specific CSV file, you can specify the file path in the command line when you execute the script. For example:

```
python src/data_vista.py --data data/your_specific_file.csv

```

## Testing

To run the tests, use:

```
python -m unittest discover -s tests

```

## Sample Unit Tests

You can create a `tests/test_data_vista.py` file with the following content:

```
# test_data_vista.py
import os
import unittest
import pandas as pd
from src.data_vista import DataVista

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

```

## Example Dataset

The app includes a sample  dataset located as `data/sample_data.csv` for testing.

### Running the App

1. **Install Requirements**:
   Make sure you have Python and pip installed. Navigate to your project directory and run:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**: Execute the app by running:

```bash
python src/data_vista.py
```

3. **Follow Prompts** : Follow the on-screen prompts to load your dataset, preprocess it, and visualize the data.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

### Summary of Sections

* **Title and Image** : The app title and a sample visualization.
* **Overview** : Brief description of the app's purpose and functionality.
* **Features** : Detailed list of key functionalities organized into sections.
* **Getting Started** : Prerequisites and installation instructions.
* **Usage** : Guidance on running the app and how to specify a dataset.
* **Testing** : Instructions for running unit tests and a sample test code.
* **Example Dataset** : Information about the provided sample dataset.
* **License** : Licensing terms for the project.

### Conclusion

"DataVista" is a comprehensive tool designed to empower data analysts and scientists in their quest to derive meaningful insights from data. By integrating essential features such as data loading, cleaning, statistical analysis, machine learning, and diverse visualization options, the app simplifies the complexities of data analysis.

With a user-friendly interface and robust functionality, it enables users to make informed decisions quickly and effectively. As data continues to play a crucial role in shaping business strategies and outcomes, "DataVista" equips professionals with the tools they need to navigate the data landscape confidently.

Whether you're a seasoned data scientist or just starting your journey, this app serves as a valuable companion, transforming your data challenges into actionable insights. Embrace the power of data with "DataVista" and unlock the potential of your data today!
