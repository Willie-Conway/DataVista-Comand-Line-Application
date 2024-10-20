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
        logging.info(f"Removed duplicates: {initial_shape[0]} -> {self.data.shape[0]} rows.")
        
        logging.info(Fore.YELLOW + "Current missing values:\n" + Fore.RESET)
        for col, count in self.data.isnull().sum().items():
            logging.info(f"{col}: {count}")
        
        # Create a structured prompt for handling missing values
        while True:
            print(Fore.BLUE + "\nChoose an action for handling missing values:\n" + Fore.RESET)
            print("1. Remove rows with missing values")
            print("2. Fill missing values")
            print("3. Skip to the next step")
            
            action = input(Fore.BLUE + "\nEnter your choice (1, 2, or 3): " + Fore.RESET)
            if action == '1':
                self.data.dropna(inplace=True)
                logging.info(Fore.GREEN + "Removed rows with missing values." + Fore.RESET)
                break
            elif action == '2':
                fill_value = input(Fore.BLUE + "Enter the value to fill missing values (e.g., 0 or 'mean'): " + Fore.RESET)
                if fill_value.lower() == 'mean':
                    self.data.fillna(self.data.mean(), inplace=True)
                else:
                    try:
                        fill_value = float(fill_value)
                        self.data.fillna(fill_value, inplace=True)
                    except ValueError:
                        logging.error(Fore.RED + "Invalid fill value entered. Please enter a numeric value or 'mean'." + Fore.RESET)
                        continue
                logging.info("Filled missing values.")
                break
            elif action == '3':
                logging.info(Fore.YELLOW + "Skipping missing value handling." + Fore.RESET)
                break
            else:
                logging.error(Fore.RED + "Invalid action for missing values." + Fore.RESET)
        
        return self.data
