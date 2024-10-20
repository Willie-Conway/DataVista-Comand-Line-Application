import logging
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from colorama import Fore

class MachineLearning:
    def __init__(self, data):
        self.data = data

    def train_model(self, target_column):
        if self.data is None:
            logging.error(Fore.RED + "No data loaded for machine learning." + Fore.RESET)
            return
        
        if target_column not in self.data.columns:
            logging.error(Fore.RED + "Target column not found in the dataset." + Fore.RESET)
            return
        
        # Prepare features and target
        feature_columns = self.data.columns.difference([target_column])
        X = self.data[feature_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
        y = self.data[target_column]

        # Drop datetime columns
        datetime_columns = X.select_dtypes(include=['datetime64']).columns
        X.drop(columns=datetime_columns, inplace=True)

        # Handle missing values
        X.fillna(X.mean(), inplace=True)
        y.fillna(y.mean(), inplace=True)

        # Align features and target
        X, y = X.align(y, join='inner', axis=0)

        # Convert categorical variables to numeric
        X = pd.get_dummies(X, drop_first=True)

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        model = LinearRegression()

        try:
            model.fit(X_train, y_train)
        except Exception as e:
            logging.error(Fore.RED + f"Error during model training: {e}" + Fore.RESET)
            return

        # Make predictions
        predictions = model.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        logging.info(Fore.GREEN + f"Model trained successfully with MSE: {mse:.2f}, R²: {r2:.2f}" + Fore.RESET)

        # Optionally log model coefficients
        logging.info(Fore.GREEN + "Model coefficients: " + str(model.coef_) + Fore.RESET)

        # Cross-validation scores
        cv_scores = cross_val_score(model, X, y, cv=5)
        logging.info(Fore.GREEN + f"Cross-Validation Scores: {cv_scores}" + Fore.RESET)
