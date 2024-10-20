import argparse
import logging
from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_preprocessor import DataPreprocessor
from statistical_analysis import StatisticalAnalysis
from machine_learning import MachineLearning
from visualization import Visualization
from colorama import Fore

# Define the app version
APP_VERSION = "1.1.0"  # Increment version for new features

# Configure logging
logging.basicConfig(level=logging.INFO)

class DataVista:
    def __init__(self):
        self.data = None

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

    def machine_learning(self, target_column, algorithm='linear_regression'):
        ml = MachineLearning(self.data)
        ml.train_model(target_column, algorithm)

    def visualize_data(self, columns, chart_type):
        visualizer = Visualization(self.data)
        visualizer.visualize(columns, chart_type)

def main():
    print(Fore.GREEN + f"\nWelcome to DataVista v{APP_VERSION}!" + Fore.RESET)
    print(Fore.GREEN + "Your companion for data analysis and visualization.\n" + Fore.RESET)

    parser = argparse.ArgumentParser(description="DataVista App")
    parser.add_argument('--data', type=str, help='Path to the CSV file', default='data/walmart_grocery_data.csv')
    args = parser.parse_args()

    app = DataVista()
    
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
        print("6. Exit")
        
        choice = input(Fore.BLUE + "\nChoose an option (1-6): " + Fore.RESET)
        
        if choice == '1':
            app.statistical_analysis()
        elif choice == '2':
            target_column = input(Fore.BLUE + "\nEnter the target column name for machine learning: " + Fore.RESET)
            algorithm = input(Fore.BLUE + "\nChoose an algorithm (linear_regression, decision_tree, svm): " + Fore.RESET)
            app.machine_learning(target_column, algorithm)
        elif choice == '3':
            feature_columns = input(Fore.BLUE + "\nEnter feature column names to visualize (comma-separated): " + Fore.RESET).split(',')
            feature_columns = [col.strip() for col in feature_columns]  # Remove whitespace

            # Validate columns
            valid_columns = [col for col in feature_columns if col in app.data.columns]
            if not valid_columns:
                logging.error(Fore.RED + "No valid columns provided. Please try again." + Fore.RESET)
                continue
            if len(valid_columns) < len(feature_columns):
                logging.warning(Fore.YELLOW + "Some columns were invalid and will be ignored: " + 
                                ", ".join(set(feature_columns) - set(valid_columns)) + Fore.RESET)

            print(Fore.BLUE + "\nChoose a chart type:\n" + Fore.RESET)
            print("1. Histogram")
            print("2. Boxplot")
            print("3. Scatter Plot")
            print("4. Scatter Plot with Linear Regression")
            print("5. Bar Chart")
            print("6. Pie Chart")
            print("7. Correlation Heatmap")
            print("8. Distribution Plot (KDE)")
            chart_choice = input(Fore.BLUE + "\nEnter the chart type (1-8): " + Fore.RESET)
            app.visualize_data(valid_columns, chart_choice)
        elif choice == '4':
            filename = input(Fore.BLUE + "\nEnter filename to save the model: " + Fore.RESET)
            app.machine_learning.save_model(filename)
        elif choice == '5':
            filename = input(Fore.BLUE + "\nEnter filename to load the model: " + Fore.RESET)
            app.machine_learning.load_model(filename)
        elif choice == '6':
            if input(Fore.YELLOW + "\nAre you sure you want to exit? (y/n): " + Fore.RESET).lower() == 'y':
                logging.info(Fore.GREEN + "Thanks for using DataVista. Goodbye!" + Fore.GREEN)
                break
        else:
            logging.error(Fore.RED + "Invalid choice. Please enter a number between 1 and 6." + Fore.RED)

if __name__ == "__main__":
    main()
