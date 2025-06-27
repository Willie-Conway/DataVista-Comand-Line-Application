# data_vista.py
import argparse
import logging
from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_preprocessor import DataPreprocessor
from statistical_analysis import StatisticalAnalysis
from machine_learning import MachineLearning
from visualization import Visualization
from hypothesis_testing import HypothesisTesting
from colorama import Fore

# Define the app version
APP_VERSION = "1.1.0"  # Increment version for new features

# Configure logging
logging.basicConfig(level=logging.INFO)

class DataVista:
    def __init__(self):
        self.data = None
        self.ml = None  # Initialize the MachineLearning class instance

    def load_data(self, file_path):
        loader = DataLoader(file_path)
        self.data = loader.load()

    def clean_data(self):
        cleaner = DataCleaner(self.data)
        self.data = cleaner.clean()

    def preprocess_data(self):
        preprocessor = DataPreprocessor(self.data)
        self.data = preprocessor.preprocess_data()

    def statistical_analysis(self):
        analysis = StatisticalAnalysis(self.data)
        analysis.perform_analysis()

    def machine_learning(self, target_column, algorithm='Linear Regression'):
        try:
            if target_column not in self.data.columns:
                raise KeyError(f"Target column '{target_column}' not found in the dataset.")
            # Handle categorical target for classification
            if self.data[target_column].dtype == 'object' or self.data[target_column].dtype.name == 'category':
                if self.data[target_column].nunique() == 2:
                    self.data[target_column] = self.data[target_column].cat.codes
                else:
                    raise ValueError("Logistic regression requires a binary target variable.")

            self.ml = MachineLearning(self.data)

            # Check if target is numeric
            if self.data[target_column].dtype in ['float64', 'int64']:
                # Regression algorithms (only Linear Regression implemented so far)
                if algorithm == 'Linear Regression':
                    self.ml.linear_regression(target_column)
                elif algorithm == 'Decision Tree':
                    # You need to implement decision tree regression or skip
                    logging.error(Fore.RED + "Decision Tree regression not implemented." + Fore.RESET)
                    return None
                else:
                    logging.error(Fore.RED + "Invalid algorithm selected for regression." + Fore.RESET)
                    return None
            else:
                # For classification, only if target is binary numeric
                if self.data[target_column].nunique() == 2:
                    if algorithm in ['Logistic Regression', 'Decision Tree']:
                        # Convert to expected algorithm string for ML class
                        algo_str = algorithm.lower().replace(' ', '_')
                        self.ml.classification(target_column, algo_str)
                    else:
                        logging.error(Fore.RED + "Invalid algorithm selected for classification." + Fore.RESET)
                        return None
                else:
                    logging.error(Fore.RED + "Unsupported target column type or not binary." + Fore.RESET)
                    return None

            return self.ml.model  # Return the trained model instance

        except KeyError as e:
            logging.error(Fore.RED + str(e) + Fore.RESET)
        except Exception as e:
            logging.error(Fore.RED + f"An error occurred: {str(e)}" + Fore.RESET)
        return None

    def visualize_data(self, columns, chart_type):
        visualizer = Visualization(self.data)
        visualizer.visualize(columns, chart_type)

    def hypothesis_testing(self):
        print(Fore.BLUE + "\nChoose a test:\n" + Fore.RESET)
        print("1. T-Test")
        print("2. Chi-Squared Test\n")
        
        test_type = input(Fore.BLUE + "Enter the number corresponding to your choice: " + Fore.RESET)

        if test_type == '1':
            print(Fore.GREEN + "\nT-Test Selected\n" + Fore.RESET)
            column1 = input(Fore.BLUE + "\nEnter the first numeric column name for T-Test: " + Fore.RESET)
            column2 = input(Fore.BLUE + "\nEnter the second numeric column name for T-Test: " + Fore.RESET)
            alpha = float(input(Fore.BLUE + "\nEnter significance level (default 0.05): " + Fore.RESET) or 0.05)
            tester = HypothesisTesting(self.data)
            tester.t_test(column1, column2, alpha)

        elif test_type == '2':
            print(Fore.GREEN + "\nChi-Squared Test Selected\n" + Fore.RESET)
            column1 = input(Fore.BLUE + "\nEnter the first categorical column name for Chi-Squared Test: " + Fore.RESET)
            column2 = input(Fore.BLUE + "\nEnter the second categorical column name for Chi-Squared Test: " + Fore.RESET)
            alpha = float(input(Fore.BLUE + "\nEnter significance level (default 0.05): " + Fore.RESET) or 0.05)
            tester = HypothesisTesting(self.data)
            tester.chi_squared_test(column1, column2, alpha)

        else:
            logging.error(Fore.RED + "Invalid choice. Please select a valid test type." + Fore.RESET)

def main():
    print(Fore.BLUE + f"\nWelcome to " + Fore.WHITE + "DataVista " + Fore.GREEN + "v" + APP_VERSION + Fore.RESET + "!" + Fore.RESET)
    print(Fore.BLUE + "Your companion for data analysis and visualization.\n" + Fore.RESET)

    parser = argparse.ArgumentParser(description="DataVista App")
    parser.add_argument('--data', type=str, help='Path to the CSV file', default='data/walmart_grocery_data.csv')
    args = parser.parse_args()

    app = DataVista()
    
    try:
        app.load_data(args.data)
        app.clean_data()
        app.preprocess_data()

        while True:
            print(Fore.BLUE + "\nAvailable options:\n" + Fore.RESET)
            print("1. Perform Statistical Analysis")
            print("2. Train Machine Learning Model")
            print("3. Visualize Data")
            print("4. Save Model")
            print("5. Load Model")
            print("6. View Loaded Model")
            print("7. Perform Clustering")
            print("8. Time Series Forecasting")
            print("9. Perform Hypothesis Testing")
            print("10. Exit")
            
            choice = input(Fore.BLUE + "\nChoose an option (1-10): " + Fore.RESET)
            
            if choice == '1':
                app.statistical_analysis()
            elif choice == '2':
                target_column = input(Fore.BLUE + "\nEnter the target column name for machine learning: " + Fore.RESET)
                
                # Algorithm Selection Menu
                print(Fore.BLUE + "\nChoose an algorithm:\n" + Fore.RESET)
                algorithm_options = {
                    "1": "Linear Regression",
                    "2": "Decision Tree",
                    "3": "Logistic Regression"
                }
                
                for key, value in algorithm_options.items():
                    print(f"{key}. {value}")
                    
                algorithm_choice = input(Fore.BLUE + "\nEnter the number corresponding to your choice: " + Fore.RESET)
                
                if algorithm_choice in algorithm_options:
                    algorithm = algorithm_options[algorithm_choice]
                    model = app.machine_learning(target_column, algorithm)
                    if model is None:
                        logging.error(Fore.RED + "Model training failed. Please try again." + Fore.RESET)
                else:
                    logging.error(Fore.RED + "Invalid choice. Please select a valid algorithm." + Fore.RESET)
            elif choice == '3':
                feature_columns = input(Fore.BLUE + "\nEnter feature column names to visualize (comma-separated): " + Fore.RESET).split(',')
                feature_columns = [col.strip() for col in feature_columns]

                # Validate columns
                valid_columns = [col for col in feature_columns if col in app.data.columns]
                if not valid_columns:
                    logging.error(Fore.RED + "No valid columns provided. Please try again." + Fore.RESET)
                    continue

                # Chart Type Selection
                print(Fore.BLUE + "\nChoose a chart type:\n" + Fore.RESET)
                chart_options = {
                    "1": "Histogram",
                    "2": "Boxplot",
                    "3": "Scatter Plot",
                    "4": "Scatter Plot with Linear Regression",
                    "5": "Bar Chart",
                    "6": "Pie Chart",
                    "7": "Correlation Heatmap",
                    "8": "Distribution Plot (KDE)"
                }
                for key, value in chart_options.items():
                    print(f"{key}. {value}")
                    
                chart_choice = input(Fore.BLUE + "\nEnter the chart type (1-8): " + Fore.RESET)
                app.visualize_data(valid_columns, chart_choice)
            elif choice == '4':
                if app.ml is None or app.ml.model is None:
                    logging.error(Fore.RED + "No model trained to save." + Fore.RESET)
                else:
                    filename = input(Fore.BLUE + "\nEnter filename to save the model: " + Fore.RESET)
                    app.ml.save_model(filename)
            elif choice == '5':
                filename = input(Fore.BLUE + "\nEnter filename to load the model: " + Fore.RESET)
                app.ml.load_model(filename)
            elif choice == '6':
                app.ml.view_model()
            elif choice == '7':
                try:
                    n_clusters = int(input(Fore.BLUE + "\nEnter the number of clusters for K-means: " + Fore.RESET))
                    clusters = app.ml.clustering(n_clusters)
                    print(Fore.GREEN + f"Clusters formed: {clusters}" + Fore.RESET)
                except ValueError:
                    logging.error(Fore.RED + "Please enter a valid integer for the number of clusters." + Fore.RESET)
            elif choice == '8':
                target_column = input(Fore.BLUE + "\nEnter the target column for time series forecasting: " + Fore.RESET)
                order = input(Fore.BLUE + "Enter ARIMA order as three integers (p, d, q) separated by space: " + Fore.RESET).split()
                try:
                    order = tuple(map(int, order))
                    forecast = app.ml.time_series(target_column, order)
                    print(Fore.GREEN + f"Forecast: {forecast}" + Fore.RESET)
                except ValueError:
                    logging.error(Fore.RED + "Invalid ARIMA order format. Please enter three integers." + Fore.RESET)
            elif choice == '9':
                app.hypothesis_testing()
            elif choice == '10':
                if input(Fore.YELLOW + "\nAre you sure you want to exit? (y/n): " + Fore.RESET).lower() == 'y':
                    logging.info(Fore.BLUE + "Thanks for using " + Fore.WHITE + "DataVista" + "." + Fore.RESET + Fore.BLUE + " Goodbye!" + Fore.RESET)
                    break
            else:
                logging.error(Fore.RED + "Invalid choice. Please enter a number between 1 and 10." + Fore.RED)

    except Exception as e:
        logging.error(Fore.RED + f"An error occurred: {str(e)}" + Fore.RESET)

if __name__ == "__main__":
    main()
