# machine_learning.py
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.cluster import KMeans
from statsmodels.tsa.arima.model import ARIMA
from colorama import Fore
import joblib

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LinearRegressionModel:
    def __init__(self, data):
        self.data = data
        self.model = LinearRegression()

    def train(self, target_column):
        # Separate features and target
        X = self.data.drop(columns=[target_column])
        y = self.data[target_column]

        # Convert DateTime columns to numeric
        for col in X.select_dtypes(include=['datetime64']).columns:
            X[col] = X[col].astype('int64') // 10**9  # Convert to seconds since epoch
        
        # Drop non-numeric columns
        X = X.select_dtypes(include=['float64', 'int64'])

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        logging.info(Fore.GREEN + f'Model trained with MSE: {mse}, R^2: {r2}' + Fore.RESET)

    def predict(self, X):
        return self.model.predict(X)


class ClassificationModels:
    def __init__(self, data):
        self.data = data
        self.model = None

    def train(self, target_column, algorithm='logistic_regression'):
        # Prepare features and target
        feature_columns = self.data.columns.difference([target_column])
        X = self.data[feature_columns].copy()
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
        if algorithm == 'logistic_regression':
            self.model = LogisticRegression()
        elif algorithm == 'decision_tree':
            self.model = DecisionTreeClassifier()
        else:
            logging.error(Fore.RED + "Invalid algorithm selected." + Fore.RESET)
            return

        # Train the model
        try:
            self.model.fit(X_train, y_train)
        except ValueError as e:
            logging.error(Fore.RED + f"Error during model training: {e}" + Fore.RESET)
            return

        # Evaluate the model
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        logging.info(Fore.GREEN + f"Model trained successfully with accuracy: {accuracy:.2f}" + Fore.RESET)


class ClusterAnalysis:
    def __init__(self, data):
        self.data = data

    def kmeans_clustering(self, n_clusters):
        """Perform K-means clustering."""
        X = self.data.select_dtypes(include=[float, int]).fillna(0)  # Select numeric columns and handle NaNs
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(X)

        logging.info(Fore.GREEN + f"K-Means clustering performed with {n_clusters} clusters." + Fore.RESET)
        return clusters


class TimeSeriesAnalysis:
    def __init__(self, data):
        self.data = data

    def forecast(self, target_column, order=(1, 1, 1)):
        """Forecast time series data using ARIMA."""
        if target_column not in self.data.columns:
            logging.error(Fore.RED + "Target column not found for time series forecasting." + Fore.RESET)
            return

        ts_data = self.data[target_column].dropna()
        model = ARIMA(ts_data, order=order)
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=5)  # Forecast next 5 time steps
        logging.info(Fore.GREEN + f"Time series forecast for {target_column}: {forecast}" + Fore.RESET)
        return forecast


class MachineLearning:
    def __init__(self, data):
        self.data = data
        self.model = None

    def linear_regression(self, target_column):
        lr_model = LinearRegressionModel(self.data)
        lr_model.train(target_column)
        self.model = lr_model.model  # Store the trained model

    def classification(self, target_column, algorithm='logistic_regression'):
        clf_model = ClassificationModels(self.data)
        clf_model.train(target_column, algorithm)
        self.model = clf_model.model  # Store the trained model

    def clustering(self, n_clusters):
        cluster_model = ClusterAnalysis(self.data)
        return cluster_model.kmeans_clustering(n_clusters)

    def time_series(self, target_column, order=(1, 1, 1)):
        ts_model = TimeSeriesAnalysis(self.data)
        return ts_model.forecast(target_column, order)

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

    def view_model(self):
        """View details of the loaded model."""
        if self.model is None:
            logging.error(Fore.RED + "No model loaded." + Fore.RESET)
            return
        
        logging.info(Fore.GREEN + f"Model type: {type(self.model)}" + Fore.RESET)
        logging.info(Fore.GREEN + f"Model parameters: {self.model.get_params()}" + Fore.RESET)

        if hasattr(self.model, 'coef_'):
            logging.info(Fore.GREEN + f"Coefficients: {self.model.coef_}" + Fore.RESET)
        elif hasattr(self.model, 'feature_importances_'):
            logging.info(Fore.GREEN + f"Feature importances: {self.model.feature_importances_}" + Fore.RESET)
