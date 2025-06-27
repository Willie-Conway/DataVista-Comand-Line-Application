import pandas as pd
import logging
from colorama import Fore

class DataCleaner:
    def __init__(self, data):
        self.data = data

    def clean(self, strategy=None, fill_method=None):
        """Clean the dataset by removing duplicates and handling missing values.

        Args:
            strategy (str): 'remove', 'fill', or 'skip'. If None, prompt interactively.
            fill_method (str): Required if strategy is 'fill'. One of:
                'mean', 'mode', 'ffill', 'bfill', 'interpolate'.
        """
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

        if strategy is None:
            print(Fore.BLUE + "\nChoose an action for handling missing values:\n" + Fore.RESET)
            print("1. Remove rows with missing values")
            print("2. Fill missing values")
            print("3. Skip to the next step")
            action = input(Fore.BLUE + "\nEnter your choice (1, 2, or 3): " + Fore.RESET).strip()

            if action == '1':
                confirm = input(Fore.YELLOW + "\nAre you sure you want to remove rows with missing values? (y/n): " + Fore.RESET)
                strategy = 'remove' if confirm.lower() == 'y' else 'skip'
            elif action == '2':
                strategy = 'fill'
                print("Choose a filling method:")
                print("1. Fill with mean")
                print("2. Fill with mode")
                print("3. Forward fill")
                print("4. Backward fill")
                print("5. Interpolate")
                method_choice = input(Fore.BLUE + "Enter method number: " + Fore.RESET).strip()
                fill_method = {'1': 'mean', '2': 'mode', '3': 'ffill', '4': 'bfill', '5': 'interpolate'}.get(method_choice)
            elif action == '3':
                strategy = 'skip'
            else:
                logging.error(Fore.RED + "Invalid input. Skipping missing value handling." + Fore.RESET)
                strategy = 'skip'

        # Apply strategy
        if strategy == 'remove':
            self.data.dropna(inplace=True)
            logging.info(Fore.GREEN + "Removed rows with missing values." + Fore.RESET)
        elif strategy == 'fill':
            if not fill_method:
                logging.error(Fore.RED + "Fill method not specified." + Fore.RESET)
            else:
                for col in self.data.columns:
                    if self.data[col].isnull().sum() > 0:
                        if fill_method == 'mean':
                            self.data[col].fillna(self.data[col].mean(), inplace=True)
                        elif fill_method == 'mode':
                            self.data[col].fillna(self.data[col].mode()[0], inplace=True)
                        elif fill_method == 'ffill':
                            self.data[col].fillna(method='ffill', inplace=True)
                        elif fill_method == 'bfill':
                            self.data[col].fillna(method='bfill', inplace=True)
                        elif fill_method == 'interpolate':
                            self.data[col].interpolate(inplace=True)
                        total_rows_filled += self.data[col].isnull().sum()
                logging.info(Fore.GREEN + f"Filled missing values using method '{fill_method}'." + Fore.RESET)
        elif strategy == 'skip':
            logging.info(Fore.YELLOW + "Skipping missing value handling." + Fore.RESET)

        total_rows_final = self.data.shape[0]
        logging.info(Fore.GREEN + f"Cleaning summary:\n\nInitial rows: {total_rows_initial}\nFinal rows: {total_rows_final}\nRows removed: {total_rows_initial - total_rows_final}\nRows filled: {total_rows_filled}" + Fore.RESET)

        return self.data
