# User Guide for My Data Scientist

## Introduction

"My Data Scientist" is a command-line application designed to simplify data analysis for data scientists and analysts. This guide provides detailed instructions on how to install, use, and navigate the app.

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

To use "My Data Scientist," you need Python 3.x installed on your machine. Follow these steps to set up the application:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/my-data-scientist.git
   cd my-data-scientist

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
python my_data_scientist.py --data path/to/your/data.csv

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

## Feedback and Support

We value your feedback! If you have suggestions, encounter bugs, or need support, please open an issue on our [GitHub repository](https://github.com/yourusername/my-data-scientist/issues).
