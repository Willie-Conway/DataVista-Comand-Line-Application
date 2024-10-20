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
APP_VERSION = "1.0.0"

# Configure logging
logging.basicConfig(level=logging.INFO)

class MyDataScientist:
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

    def machine_learning(self, target_column):
        ml = MachineLearning(self.data)
        ml.train_model(target_column)

    def visualize_data(self, column, chart_type):
        visualizer = Visualization(self.data)
        visualizer.visualize(column, chart_type)

def main():
    print(Fore.GREEN + f"\nWelcome to My Data Scientist v{APP_VERSION}!" + Fore.RESET)
    print(Fore.GREEN + "Your companion for data analysis and visualization.\n" + Fore.RESET)

    parser = argparse.ArgumentParser(description="My Data Scientist App")
    parser.add_argument('--data', type=str, help='Path to the CSV file', default='data/walmart_grocery_data.csv')
    args = parser.parse_args()

    app = MyDataScientist()
    
    app.load_data(args.data)
    app.clean_data()
    app.preprocess_data()

    while True:
        print(Fore.BLUE + "\nAvailable options:\n" + Fore.RESET)
        print("1. Perform Statistical Analysis")
        print("2. Train Machine Learning Model")
        print("3. Visualize Data")
        print("4. Exit")
        
        choice = input(Fore.BLUE + "\nChoose an option (1-4): " + Fore.RESET)
        
        if choice == '1':
            app.statistical_analysis()
        elif choice == '2':
            target_column = input(Fore.BLUE + "\nEnter the target column name for machine learning: " + Fore.RESET)
            app.machine_learning(target_column)
        elif choice == '3':
            feature_column = input(Fore.BLUE + "\nEnter a feature column name to visualize: " + Fore.RESET)
            print(Fore.BLUE + "\nChoose a chart type:\n" + Fore.RESET)
            print("1. Histogram")
            print("2. Boxplot")
            print("3. Scatter Plot")
            print("4. Scatter Plot with Linear Regression")
            print("5. Bar Chart")
            print("6. Pie Chart")
            print("7. Correlation Heatmap")
            chart_choice = input(Fore.BLUE + "\nEnter the chart type (1-7): " + Fore.RESET)
            app.visualize_data(feature_column, chart_choice)
        elif choice == '4':
            if input(Fore.YELLOW + "\nAre you sure you want to exit? (y/n): " + Fore.RESET).lower() == 'y':
                logging.info(Fore.GREEN + "Thanks for using My Data Scientist. Goodbye!" + Fore.GREEN)
                break
        else:
            logging.error(Fore.RED + "Invalid choice. Please enter a number between 1 and 4." + Fore.RED)

if __name__ == "__main__":
    main()
