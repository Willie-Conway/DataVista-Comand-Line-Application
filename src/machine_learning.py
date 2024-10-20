import logging
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from colorama import Fore
import joblib

class MachineLearning:
    def __init__(self, data):
        self.data = data
        self.model = None

    def train_model(self, target_column, algorithm='linear_regression'):
        """Train the specified machine learning model."""
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
        
        # Select the model based on user input
        if algorithm == 'linear_regression':
            self.model = LinearRegression()
        elif algorithm == 'decision_tree':
            self.model = DecisionTreeRegressor()
        elif algorithm == 'svm':
            self.model = SVR()
        else:
            logging.error(Fore.RED + "Invalid algorithm selected." + Fore.RESET)
            return

        # Train the model with error handling
        try:
            self.model.fit(X_train, y_train)
        except ValueError as e:
            logging.error(Fore.RED + f"Error during model training: {e}" + Fore.RESET)
            return

        # Make predictions
        predictions = self.model.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        logging.info(Fore.GREEN + f"Model trained successfully with MSE: {mse:.2f}, R²: {r2:.2f}" + Fore.RESET)

        # Optionally log model coefficients for linear regression
        if algorithm == 'linear_regression':
            logging.info(Fore.GREEN + "Model coefficients: " + str(self.model.coef_) + Fore.RESET)

        # Cross-validation scores
        cv_scores = cross_val_score(self.model, X, y, cv=5)
        logging.info(Fore.GREEN + f"Cross-Validation Scores: {cv_scores}" + Fore.RESET)

    def save_model(self, filename):
        """Save the trained model to a file."""
        if self.model is None:
            logging.error(Fore.RED + "No model trained to save." + Fore.RESET)
            return
        
        try:
            joblib.dump(self.model, filename)
            logging.info(Fore.GREEN + f"Model saved to {filename}." + Fore.RESET)
        except Exception as e:
            logging.error(Fore.RED + f"Error saving model: {e}" + Fore.RESET)

    def load_model(self, filename):
        """Load a model from a file."""
        try:
            self.model = joblib.load(filename)
            logging.info(Fore.GREEN + f"Model loaded from {filename}." + Fore.RESET)
        except FileNotFoundError:
            logging.error(Fore.RED + "Model file not found." + Fore.RESET)
        except Exception as e:
            logging.error(Fore.RED + f"Error loading model: {e}" + Fore.RESET)
