import pandas as pd
import logging
from colorama import Fore

class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def preprocess_data(self):
        """Preprocess the data by converting date columns and filling missing values."""
        if self.data is not None:
            if 'Date' in self.data.columns:
                self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data.ffill(inplace=True)  # Using forward fill for missing values
            logging.info(Fore.GREEN + "Data preprocessing complete." + Fore.RESET)
        else:
            logging.error(Fore.RED + "No data loaded to preprocess." + Fore.RESET)
        
        return self.data
