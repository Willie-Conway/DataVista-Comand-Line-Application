import pandas as pd
import logging
from colorama import Fore

class DataCleaner:
    def __init__(self, data):
        self.data = data

    def clean(self):
        """Clean the dataset by removing duplicates and handling missing values."""
        if self.data is None:
            logging.error(Fore.RED + "No data loaded to clean." + Fore.RESET)
            return None
        
        initial_shape = self.data.shape
        self.data.drop_duplicates(inplace=True)
        logging.info(Fore.GREEN + f"Removed duplicates: {initial_shape[0]} -> {self.data.shape[0]} rows." + Fore.RESET)
        
        logging.info(Fore.YELLOW + "Current missing values:\n" + Fore.RESET)
        for col, count in self.data.isnull().sum().items():
            logging.info(Fore.GREEN + f"{col}: {count}" + Fore.RESET)

        total_rows_initial = self.data.shape[0]
        total_rows_filled = 0

        while True:
            print(Fore.BLUE + "\nChoose an action for handling missing values:\n" + Fore.RESET)
            print("1. Remove rows with missing values")
            print("2. Fill missing values")
            print("3. Skip to the next step")
            
            action = input(Fore.BLUE + "\nEnter your choice (1, 2, or 3): " + Fore.RESET)
            if action == '1':
                confirm = input(Fore.YELLOW + "\nAre you sure you want to remove rows with missing values? (y/n): " + Fore.RESET)
                if confirm.lower() == 'y\n2':
                    self.data.dropna(inplace=True)
                    logging.info(Fore.GREEN + "Removed rows with missing values." + Fore.RESET)
                break
            elif action == '2':
                fill_option = input(Fore.BLUE + "Choose a filling method:\n1. Fill with mean\n2. Fill with mode\n3. Forward fill\n4. Backward fill\n5. Interpolate\n" + Fore.RESET)
                for col in self.data.columns:
                    if self.data[col].isnull().sum() > 0:  # Check if there are missing values
                        if fill_option == '1':  # Fill with mean
                            fill_value = self.data[col].mean()
                            self.data[col].fillna(fill_value, inplace=True)
                        elif fill_option == '2':  # Fill with mode
                            fill_value = self.data[col].mode()[0]
                            self.data[col].fillna(fill_value, inplace=True)
                        elif fill_option == '3':  # Forward fill
                            self.data[col].fillna(method='ffill', inplace=True)
                        elif fill_option == '4':  # Backward fill
                            self.data[col].fillna(method='bfill', inplace=True)
                        elif fill_option == '5':  # Interpolate
                            self.data[col].interpolate(inplace=True)
                        total_rows_filled += self.data[col].isnull().sum()  # Track how many were filled
                logging.info(Fore.GREEN + f"Filled missing values using method {fill_option}." + Fore.RESET)
                break
            elif action == '3':
                logging.info(Fore.YELLOW + "Skipping missing value handling." + Fore.RESET)
                break
            else:
                logging.error(Fore.RED + "Invalid action for missing values." + Fore.RESET)
        
        # Summary of changes made
        total_rows_final = self.data.shape[0]
        logging.info(Fore.GREEN + f"Cleaning summary:\n\nInitial rows: {total_rows_initial}\nFinal rows: {total_rows_final}\nRows removed: {total_rows_initial - total_rows_final}\nRows filled: {total_rows_filled}" + Fore.RESET)

        return self.data
