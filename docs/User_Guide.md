# User Guide for DataVista
![DataVista User Guide](https://tinypic.host/images/2024/10/21/DataVistaUserGuide.png)

## Introduction

**DataVista** is a command-line application designed to simplify data analysis for data scientists and analysts. This guide provides detailed instructions on how to install, use, and navigate the app.

## Project Structure

```python
DataVista/
│
├── .github/
│   └── workflows/
│       └── ci.yml                     # Continuous integration configuration file
│
├── data/
│   ├── market_research.csv             # Dataset for market research analysis
│   ├── sample_data.csv                 # Sample dataset for testing
│   ├── test_data_with_duplicates.csv    # Dataset specifically for testing data cleaning
│   └── walmart_grocery_data.csv        # Grocery data for analysis
│
├── docs/
│   └── User_Guide.md                   # User guide documentation
│
├── extra/
│   └── image/
│       ├── DataVistaLogo.png           # Logo images for the application
│       ├── DataVistaLogo2.png
│       └── DataVistaLogo3.png
│
├── src/
│   ├── data_cleaner.py                 # Module for data cleaning
│   ├── data_loader.py                   # Module for loading data
│   ├── data_preprocessor.py             # Module for preprocessing data
│   ├── data_vista.py                    # Main application file
│   ├── machine_learning.py              # Module for machine learning tasks
│   ├── statistical_analysis.py           # Module for statistical analysis
│   └── visualization.py                  # Module for data visualization
│
├── tests/
│   └── test_data_vista.py               # Unit tests for the DataVista application
│
├── CODE_OF_CONDUCT.md                   # Guidelines for community behavior
├── CONTRIBUTING.md                       # Instructions for contributing to the project
├── LICENSE                               # License information for the project
├── README.md                             # Overview of the project
├── Summary.md                            # Summary of the project or key features
├── data_vista_info.sh                   # Script for additional info or setup
└── requirements.txt                     # List of required Python packages


```

# DataVista File Descriptions

## .github/workflows/ci.yml
Contains configuration for continuous integration, automating tests or builds when code changes are pushed.

## data/
Holds various datasets, including test data, which are essential for both application testing and user analysis.

## docs/User_Guide.md
Contains user instructions and guides for using DataVista effectively.

## extra/image/
Includes logo images for branding or visual identity.

## src/
Contains all the source code files that make up the application.

## tests/
Contains tests to ensure the application behaves as expected, promoting code reliability.

## CODE_OF_CONDUCT.md
Sets expectations for community behavior and interaction.

## CONTRIBUTING.md
Provides guidelines for contributing to the project, encouraging collaboration.

## LICENSE
Details the legal permissions and restrictions for using and distributing the software.

## README.md
A crucial file that introduces the project, explaining its purpose, features, and how to get started.

## Summary.md
Summarizes the project, possibly highlighting key features or changes.

## data_vista_info.sh
A shell script, possibly for setting up or providing additional information about the project.

## requirements.txt
Lists the dependencies required to run the application, facilitating easy setup.


## Table of Contents

1. [Installation]()
2. [Getting Started]()
3. [Loading Data]()
4. [Preprocessing Data]()
5. [Splitting Data]()
6. [Data Visualization]()
7. [Error Handling]()
8. [Feedback and Support]()

## Installation

To use "DataVista," you need Python 3.x installed on your machine. Follow these steps to set up the application:

1. Clone the repository:

   ```
   git clone https://github.com/Willie-Conway/DataVista.git
   cd DataVista

   ```
2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

   ```
3. Install the required packages:

   ```
   pip install -r requirements.txt

   ```

## Getting Started

Run the application using the following command:

```
python src/data_vista.py --data path/to/your/data.csv

```

Replace `path/to/your/data.csv` with the path to your dataset.

## Loading Data

1. The app will prompt you to enter the path to your CSV file.
2. If the file is successfully loaded, you will see a confirmation message. If there’s an error, appropriate error messages will guide you.

## Preprocessing Data

Once the data is loaded, you can preprocess it:

1. The app automatically handles missing values and converts date columns to datetime format.
2. You will receive a notification upon completion of the preprocessing step.

## Splitting Data

You will be prompted to enter the target column name for splitting the data:

1. Enter the name of the target variable (e.g., `Weekly_Sales`).
2. The app will split the data into training and testing sets, and you will receive a confirmation message.

## Data Visualization

After splitting the data, you can choose from several visualization options:

1. **Distribution Plot**
2. **Bar Chart**
3. **Box Plot**
4. **Scatter Plot**
5. **Scatter Plot with Linear Regression**
6. **Histogram**
7. **Pie Chart**

Enter the corresponding number for your choice, and the app will generate the selected visualization.

## Error Handling

The app is designed to provide user-friendly error messages. If you encounter issues such as missing files or invalid column names, follow the guidance in the error messages to resolve them.

## Data Flow Overview

1. **Loading Data** :

* User provides a CSV file path.
* `load_data()` reads the file and populates `self.data`.

1. **Cleaning Data** :

* `clean_data()` processes `self.data` to remove duplicates and handle missing values.

1. **Preprocessing Data** :

* `preprocess_data()` formats the data for analysis (e.g., date conversion).

1. **Statistical Analysis** :

* User selects a column for analysis.
* `statistical_analysis()` computes and logs various statistics.

1. **Machine Learning** :

* User specifies a target column.
* `machine_learning()` trains a model and logs the performance.

1. **Data Visualization** :

* User selects a visualization type and column.
* `visualize_data()` generates and displays the chart.


## Feedback and Support

We value your feedback! If you have suggestions, encounter bugs, or need support, please open an issue on our [GitHub repository](https://github.com/Willie-Conway/DataVista/issues).
