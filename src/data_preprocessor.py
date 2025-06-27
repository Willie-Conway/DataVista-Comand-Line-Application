import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler
from colorama import Fore

class DataPreprocessor:
    def __init__(self, data, scale_choice=None, outlier_choice=None, fill_methods=None):
        """
        Args:
            data (pd.DataFrame): The input dataset.
            scale_choice (str, optional): '1' to scale features, '2' to skip scaling.
            outlier_choice (str, optional): '1' to remove outliers, '2' to keep.
            fill_methods (dict, optional): Dict mapping column names to fill strategy codes ('1'-'5').
        """
        self.original_data = data.copy()  # Keep a copy of the original data
        self.data = data
        self.scale_features_flag = self.ask_scale_option(scale_choice)
        self.remove_outliers_flag = self.ask_remove_outliers_option(outlier_choice)
        self.fill_methods = fill_methods or {}

    def ask_scale_option(self, choice=None):
        """Ask the user if they want to scale the data or not."""
        if choice:
            return choice == '1'
        print(Fore.BLUE + "\nChoose an option for scaling features:\n" + Fore.RESET)
        print("1. Scale features")
        print("2. Do not scale features")
        choice = input(Fore.BLUE + "\nEnter your choice (1 or 2): " + Fore.RESET).strip()
        return choice == '1'

    def ask_remove_outliers_option(self, choice=None):
        """Ask the user if they want to remove outliers or keep them."""
        if choice:
            return choice == '1'
        print(Fore.BLUE + "\nChoose an option for handling outliers:\n" + Fore.RESET)
        print("1. Remove outliers")
        print("2. Keep outliers")
        choice = input(Fore.BLUE + "\nEnter your choice (1 or 2): " + Fore.RESET).strip()
        return choice == '1'

    def preprocess_data(self):
        """Preprocess the data by converting date columns, filling missing values, removing outliers, and scaling features."""
        if self.data is not None:
            self.convert_date_columns()
            self.handle_missing_values()
            if self.remove_outliers_flag:
                self.remove_outliers()  # Only remove outliers if the flag is set
            self.scale_features()  # Optional scaling based on user choice
            logging.info(Fore.GREEN + "Data preprocessing complete." + Fore.RESET)
        else:
            logging.error(Fore.RED + "No data loaded to preprocess." + Fore.RESET)

        return self.data

    def convert_date_columns(self):
        """Convert object columns that represent dates into datetime."""
        date_cols = self.data.select_dtypes(include=['object']).columns.tolist()
        for col in date_cols:
            if self.is_date(col):
                self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
                logging.info(Fore.GREEN + f"Converted '{col}' to datetime." + Fore.RESET)

    def is_date(self, column):
        """Check if a column can be converted to datetime."""
        date_keywords = ['date', 'timestamp', 'time']
        return any(keyword in column.lower() for keyword in date_keywords)

    def handle_missing_values(self):
        """Handle missing values based on user input or preset fill_methods."""
        for col in self.data.columns:
            if self.data[col].isnull().sum() > 0:
                strategy = self.fill_methods.get(col)
                if not strategy:
                    # Interactive prompt only if no preset strategy
                    print(Fore.BLUE + f"\nColumn '{col}' has missing values. Choose a fill method:\n" + Fore.RESET)
                    print("1. Mean")
                    print("2. Median")
                    print("3. Mode")
                    print("4. Specific Value")
                    print("5. Skip")
                    strategy = input(Fore.BLUE + "Enter your choice (1-5): " + Fore.RESET).strip()

                if strategy == '1':
                    self.data[col].fillna(self.data[col].mean(), inplace=True)
                    logging.info(Fore.GREEN + f"Filled missing values in '{col}' with mean." + Fore.RESET)
                elif strategy == '2':
                    self.data[col].fillna(self.data[col].median(), inplace=True)
                    logging.info(Fore.GREEN + f"Filled missing values in '{col}' with median." + Fore.RESET)
                elif strategy == '3':
                    self.data[col].fillna(self.data[col].mode()[0], inplace=True)
                    logging.info(Fore.GREEN + f"Filled missing values in '{col}' with mode." + Fore.RESET)
                elif strategy == '4':
                    if col in self.fill_methods:
                        fill_value = self.fill_methods.get(f"{col}_value", None)
                    else:
                        fill_value = input(Fore.BLUE + "Enter the specific value to fill: " + Fore.RESET)
                    self.data[col].fillna(fill_value, inplace=True)
                    logging.info(Fore.GREEN + f"Filled missing values in '{col}' with specific value." + Fore.RESET)
                elif strategy == '5':
                    logging.info(Fore.YELLOW + f"Skipping filling for column '{col}'." + Fore.RESET)
                else:
                    logging.warning(Fore.YELLOW + f"Invalid fill method for column '{col}', skipping." + Fore.RESET)

    def remove_outliers(self):
        """Remove outliers from numerical columns using the IQR method."""
        for col in self.data.select_dtypes(include=['float64', 'int64']).columns:
            if self.data[col].isnull().sum() == 0:
                Q1 = self.data[col].quantile(0.25)
                Q3 = self.data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                initial_shape = self.data.shape
                self.data = self.data[(self.data[col] >= lower_bound) & (self.data[col] <= upper_bound)]
                logging.info(Fore.GREEN + f"Removed outliers from '{col}': {initial_shape[0]} -> {self.data.shape[0]} rows." + Fore.RESET)

    def scale_features(self):
        """Scale numerical features using StandardScaler, if the flag is set."""
        if self.scale_features_flag:
            numerical_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
            scaler = StandardScaler()
            self.data[numerical_cols] = scaler.fit_transform(self.data[numerical_cols])
            logging.info(Fore.GREEN + "Features scaled successfully." + Fore.RESET)
        else:
            self.data = self.original_data.copy()  # Restore original data
            logging.info(Fore.YELLOW + "Skipping feature scaling. Original data retained." + Fore.RESET)

# Example usage:
# if __name__ == "__main__":
#     data = pd.read_csv('your_file.csv')
#     # For interactive mode (no arguments)
#     preprocessor = DataPreprocessor(data)
#     processed_data = preprocessor.preprocess_data()
#
#     # For automated / testing mode:
#     # preprocessor = DataPreprocessor(
#     #     data,
#     #     scale_choice='1',
#     #     outlier_choice='2',
#     #     fill_methods={'ColumnName': '1', 'AnotherColumn': '3'}
#     # )
#     # processed_data = preprocessor.preprocess_data()
