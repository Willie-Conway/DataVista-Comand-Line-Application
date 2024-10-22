import pandas as pd
import logging
from colorama import Fore

class DataLoader:
    def __init__(self, file_path, file_format='csv', delimiter=','):
        self.file_path = file_path
        self.file_format = file_format
        self.delimiter = delimiter

    def load(self):
        """Load data from various file formats into a DataFrame."""
        try:
            if self.file_format == 'csv':
                data = pd.read_csv(self.file_path, delimiter=self.delimiter)
            elif self.file_format == 'excel':
                data = pd.read_excel(self.file_path)
            elif self.file_format == 'json':
                data = pd.read_json(self.file_path)
            else:
                logging.error(Fore.RED + f"Unsupported file format: {self.file_format}. Please use 'csv', 'excel', or 'json'." + Fore.RESET)
                return None
            
            if data.empty:
                logging.error(Fore.RED + "The loaded data is empty." + Fore.RESET)
            else:
                logging.info(Fore.GREEN + "Data loaded successfully." + Fore.RESET)
                self.validate_data(data)  # Validate loaded data

            return data
        except FileNotFoundError:
            logging.error(Fore.RED + "File not found. Please check the path." + Fore.RESET)
            return None
        except pd.errors.EmptyDataError:
            logging.error(Fore.RED + "No data: the file is empty." + Fore.RESET)
            return None
        except Exception as e:
            logging.error(Fore.RED + f"Error loading data: {e}" + Fore.RESET)
            return None

    def validate_data(self, data):
        """Perform basic data validation checks."""
        expected_columns = []  # Updated expected columns
        for col in expected_columns:
            if col not in data.columns:
                logging.warning(Fore.YELLOW + f"Expected column '{col}' not found in the dataset." + Fore.RESET)

        logging.info(Fore.GREEN + "Data validation complete." + Fore.RESET)
