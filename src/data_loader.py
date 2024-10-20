import pandas as pd
import logging
from colorama import Fore

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """Load data from a CSV file into a DataFrame."""
        try:
            data = pd.read_csv(self.file_path)
            if data.empty:
                logging.error(Fore.RED + "The loaded data is empty." + Fore.RESET)
            else:
                logging.info(Fore.GREEN + "Data loaded successfully." + Fore.RESET)
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
