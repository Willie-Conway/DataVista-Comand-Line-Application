import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from colorama import Fore

class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def preprocess_data(self):
        """Preprocess the data by converting date columns and filling missing values."""
        if self.data is not None:
            if 'Date' in self.data.columns:
                self.data['Date'] = pd.to_datetime(self.data['Date'])
            
            # Handle missing values
            self.handle_missing_values()

            # Feature engineering
            self.remove_outliers()
            self.scale_features()
            self.encode_categorical_variables()

            logging.info(Fore.GREEN + "Data preprocessing complete." + Fore.RESET)
        else:
            logging.error(Fore.RED + "No data loaded to preprocess." + Fore.RESET)
        
        return self.data

    def handle_missing_values(self):
        """Handle missing values based on user input."""
        for col in self.data.columns:
            if self.data[col].isnull().sum() > 0:
                print(Fore.BLUE + f"\nColumn '{col}' has missing values. Choose a fill method:\n" + Fore.RESET)
                print("1. Mean")
                print("2. Median")
                print("3. Mode")
                print("4. Specific Value")
                print("5. Skip")
                
                action = input(Fore.BLUE + "Enter your choice (1-5): " + Fore.RESET)
                if action == '1':
                    self.data[col].fillna(self.data[col].mean(), inplace=True)
                elif action == '2':
                    self.data[col].fillna(self.data[col].median(), inplace=True)
                elif action == '3':
                    self.data[col].fillna(self.data[col].mode()[0], inplace=True)
                elif action == '4':
                    fill_value = input(Fore.BLUE + "Enter the specific value to fill: " + Fore.RESET)
                    self.data[col].fillna(fill_value, inplace=True)
                elif action == '5':
                    logging.info(Fore.YELLOW + f"Skipping filling for column '{col}'." + Fore.RESET)

    def remove_outliers(self):
        """Remove outliers from numerical columns."""
        for col in self.data.select_dtypes(include=['float64', 'int64']).columns:
            if self.data[col].isnull().sum() == 0:  # Only process columns without missing values
                Q1 = self.data[col].quantile(0.25)
                Q3 = self.data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                initial_shape = self.data.shape
                self.data = self.data[(self.data[col] >= lower_bound) & (self.data[col] <= upper_bound)]
                logging.info(f"Removed outliers from '{col}': {initial_shape[0]} -> {self.data.shape[0]} rows.")

    def scale_features(self):
        """Scale numerical features using StandardScaler."""
        numerical_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        scaler = StandardScaler()
        self.data[numerical_cols] = scaler.fit_transform(self.data[numerical_cols])
        logging.info(Fore.GREEN + "Features scaled successfully." + Fore.RESET)

    def encode_categorical_variables(self):
        """Encode categorical variables using OneHotEncoder."""
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            encoder = OneHotEncoder(drop='first', sparse_output=False)  # Updated argument
            encoded_features = encoder.fit_transform(self.data[categorical_cols])
            encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))
            self.data = self.data.drop(categorical_cols, axis=1)
            self.data = pd.concat([self.data, encoded_df], axis=1)
            logging.info(Fore.GREEN + "Categorical variables encoded successfully." + Fore.RESET)
