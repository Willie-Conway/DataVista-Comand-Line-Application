# Dissecting the DataCleaner: A Code Walkthrough

## Table of Contents
1. [Purpose of the File](#purpose-of-the-file)
2. [Code Overview](#code-overview)
3. [Walkthrough Breakdown](#walkthrough-breakdown)
   - [Imports](#imports)
   - [Class Definition](#class-definition)
   - [Initialization (`__init__` method)](#initialization-__init__-method)
   - [Cleaning Method (`clean` method)](#cleaning-method-clean-method)
   - [Interactive User Input Loop](#interactive-user-input-loop)
   - [Filling Missing Values](#filling-missing-values)
   - [Final Summary](#final-summary)
   - [Return Value](#return-value)

## Purpose of the File

The purpose of this file is to provide a comprehensive class, `DataCleaner`, designed to simplify the process of cleaning datasets in Python using the pandas library. The `DataCleaner` class offers methods to:

1. **Remove Duplicates**: Automatically identify and remove duplicate rows from the dataset.
2. **Handle Missing Values**: Provide interactive options for managing missing data, including:
   - Removing rows with missing values.
   - Filling missing values using various strategies (mean, mode, forward fill, backward fill, or interpolation).
3. **Logging**: Maintain a detailed log of all actions taken during the cleaning process, ensuring transparency and ease of debugging.

This file serves as a practical tool for data scientists and analysts who need to prepare their data for analysis or modeling, helping to ensure data quality and integrity.

 ## Code Overview

 ```python
import pandas as pd
import logging
from colorama import Fore

class DataCleaner:
    def __init__(self, data):
        """
        Initialize the DataCleaner class with a dataset.

        Parameters:
        data (pd.DataFrame): The dataset to be cleaned.
        """
        self.data = data  # Store the dataset as an instance variable

    def clean(self):
        """
        Clean the dataset by removing duplicates and handling missing values.
        This method will interactively guide the user through cleaning options.
        """
        # Check if data is None, log an error if so
        if self.data is None:
            logging.error(Fore.RED + "No data loaded to clean." + Fore.RESET)
            return None  # Exit the method if no data is provided
        
        # Store the initial shape of the dataset for reference (number of rows and columns)
        initial_shape = self.data.shape
        
        # Remove duplicate rows from the dataset and log the change
        self.data.drop_duplicates(inplace=True)
        logging.info(Fore.GREEN + f"Removed duplicates: {initial_shape[0]} -> {self.data.shape[0]} rows." + Fore.RESET)
        
        # Display the current count of missing values in each column
        logging.info(Fore.YELLOW + "Current missing values:\n" + Fore.RESET)
        for col, count in self.data.isnull().sum().items():
            logging.info(Fore.GREEN + f"{col}: {count}" + Fore.RESET)  # Log the count of missing values per column

        # Initialize variables to track the number of rows before and after cleaning
        total_rows_initial = self.data.shape[0]
        total_rows_filled = 0  # Track how many rows were filled

        # Interactive loop for user to choose how to handle missing values
        while True:
            print(Fore.BLUE + "\nChoose an action for handling missing values:\n" + Fore.RESET)
            print("1. Remove rows with missing values")
            print("2. Fill missing values")
            print("3. Skip to the next step")
            
            # Get user input for the chosen action
            action = input(Fore.BLUE + "\nEnter your choice (1, 2, or 3): " + Fore.RESET)
            if action == '1':
                # Confirm removal of rows with missing values
                confirm = input(Fore.YELLOW + "\nAre you sure you want to remove rows with missing values? (y/n): " + Fore.RESET)
                if confirm.lower() == 'y':
                    self.data.dropna(inplace=True)  # Drop rows with any missing values
                    logging.info(Fore.GREEN + "Removed rows with missing values." + Fore.RESET)
                break  # Exit the loop after performing the action
            elif action == '2':
                # Present options for filling missing values
                fill_option = input(Fore.BLUE + "Choose a filling method:\n1. Fill with mean\n2. Fill with mode\n3. Forward fill\n4. Backward fill\n5. Interpolate\n" + Fore.RESET)
                
                # Iterate over each column to fill missing values based on user's choice
                for col in self.data.columns:
                    if self.data[col].isnull().sum() > 0:  # Only process columns that have missing values
                        if fill_option == '1':  # Fill missing values with the mean
                            fill_value = self.data[col].mean()
                            self.data[col].fillna(fill_value, inplace=True)
                        elif fill_option == '2':  # Fill missing values with the mode
                            fill_value = self.data[col].mode()[0]
                            self.data[col].fillna(fill_value, inplace=True)
                        elif fill_option == '3':  # Forward fill missing values
                            self.data[col].fillna(method='ffill', inplace=True)
                        elif fill_option == '4':  # Backward fill missing values
                            self.data[col].fillna(method='bfill', inplace=True)
                        elif fill_option == '5':  # Interpolate missing values
                            self.data[col].interpolate(inplace=True)
                        # Track how many rows were filled
                        total_rows_filled += self.data[col].isnull().sum()  
                logging.info(Fore.GREEN + f"Filled missing values using method {fill_option}." + Fore.RESET)
                break  # Exit the loop after the action is performed
            elif action == '3':
                logging.info(Fore.YELLOW + "Skipping missing value handling." + Fore.RESET)
                break  # Exit the loop, skipping any handling of missing values
            else:
                logging.error(Fore.RED + "Invalid action for missing values." + Fore.RESET)
        
        # Summarize the changes made to the dataset after cleaning
        total_rows_final = self.data.shape[0]
        logging.info(Fore.GREEN + f"Cleaning summary:\n\nInitial rows: {total_rows_initial}\nFinal rows: {total_rows_final}\nRows removed: {total_rows_initial - total_rows_final}\nRows filled: {total_rows_filled}" + Fore.RESET)

        return self.data  # Return the cleaned dataset

```
## Walkthrough Breakdown

### Imports:
- **pandas** is imported for data manipulation.
- **logging** is used for logging information and errors.
- **colorama** is used for colored terminal output to enhance readability.

### Class Definition:
- **DataCleaner** is defined to encapsulate data cleaning functionalities.

### Initialization (`__init__` method):
- The class is initialized with a dataset, which is stored as an instance variable.

### Cleaning Method (`clean` method):
- **Data Existence Check**: Verifies if the dataset is loaded. Logs an error if not.
- **Initial Shape Logging**: Records the shape of the dataset before any cleaning occurs.
- **Duplicate Removal**: Identifies and removes duplicate rows, logging the change.
- **Missing Values Check**: Counts and logs the number of missing values in each column.
  
### Interactive User Input Loop:
- Prompts the user for how to handle missing values.
- Options to remove rows, fill missing values, or skip handling.
- Each option leads to specific actions based on user input.

### Filling Missing Values:
- Depending on the chosen filling method, missing values are filled accordingly. The number of filled values is tracked.

### Final Summary:
- After all actions, it logs a summary of the initial and final number of rows, including how many were removed or filled.

### Return Value:
- The cleaned dataset is returned for further analysis or use.

