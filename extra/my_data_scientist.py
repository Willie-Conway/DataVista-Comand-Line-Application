import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import argparse
import numpy as np
from scipy import stats

# Configure logging to display information
logging.basicConfig(level=logging.INFO)

# ANSI color codes
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Define the app version
APP_VERSION = "1.0.0"

class DataVista:
    def __init__(self):
        """Initialize the DataVista class."""
        self.data = None  # Placeholder for loaded data

    # Loading the Data
    def load_data(self, file_path):
        """Load data from a CSV file into a DataFrame."""
        try:
            self.data = pd.read_csv(file_path)
            if self.data.empty:
                logging.error(RED + "The loaded data is empty." + RESET)
            else:
                logging.info(GREEN + "Data loaded successfully." + RESET)
        except FileNotFoundError:
            logging.error(RED + "File not found. Please check the path." + RESET)
        except pd.errors.EmptyDataError:
            logging.error(RED + "No data: the file is empty." + RESET)
        except Exception as e:
            logging.error(f"Error loading data: {e}")

    # Cleaning the Data
    def clean_data(self):
        """Clean the dataset by removing duplicates and handling missing values."""
        if self.data is None:
            logging.error(RED + "No data loaded to clean." + RESET)
            return
        
        initial_shape = self.data.shape
        self.data.drop_duplicates(inplace=True)
        logging.info(f"Removed duplicates: {initial_shape[0]} -> {self.data.shape[0]} rows.")
        
        logging.info(YELLOW + "Current missing values:\n" + RESET)
        for col, count in self.data.isnull().sum().items():
            logging.info(f"{col}: {count}")
        
        while True:
            action = input(BLUE + "\nDo you want to (1) remove rows with missing values, (2) fill them, or (3) skip to the next step? (Enter 1, 2, or 3): " + RESET)
            if action == '1':
                self.data.dropna(inplace=True)
                logging.info(YELLOW + "Removed rows with missing values." + RESET)
                break
            elif action == '2':
                fill_value = input("Enter the value to fill missing values (e.g., 0 or 'mean'): ")
                if fill_value.lower() == 'mean':
                    self.data.fillna(self.data.mean(), inplace=True)
                else:
                    try:
                        fill_value = float(fill_value)
                        self.data.fillna(fill_value, inplace=True)
                    except ValueError:
                        logging.error(RED + "Invalid fill value entered. Please enter a numeric value or 'mean'." + RESET)
                        continue
                logging.info("Filled missing values.")
                break
            elif action == '3':
                logging.info(YELLOW + "Skipping missing value handling." + RESET)
                break
            else:
                logging.error("Invalid action for missing values.")

    # Preprocessing the Data
    def preprocess_data(self):
        """Preprocess the data by converting date columns and filling missing values."""
        if self.data is not None:
            if 'Date' in self.data.columns:
                self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data.ffill(inplace=True)  # Using forward fill for missing values
            logging.info(GREEN + "Data preprocessing complete." + RESET)
        else:
            logging.error("No data loaded to preprocess.")

    # Statistical Analysis
    def statistical_analysis(self):
        """Perform statistical analysis on numerical columns."""
        if self.data is None:
            logging.error("No data loaded for statistical analysis.")
            return
        
        logging.info(GREEN + "Statistical Summary:\n" + RESET)
        
        # Get the statistical summary
        summary = self.data.describe()
        
        # Prepare the formatted output based on the number of summary columns
        format_str = "{:<12}" + "{:>12}" * len(summary.columns)
        
        # Log the header
        logging.info(format_str.format("Variable", *summary.columns))

        # Log each row of the summary
        for index in summary.index:
            logging.info(format_str.format(index, *summary.loc[index]))

        column = input(BLUE + "\nEnter a column name for statistical analysis (e.g., 'Weekly_Sales'): " + RESET)
        if column in self.data.columns:
            data_series = self.data[column].dropna()  # Remove NaN values for calculations
            
            # Normality test
            logging.info(f"Normality test for {column}:")
            k2, p = stats.normaltest(data_series)
            alpha = 0.05
            if p < alpha:
                logging.info(f"{column} does not follow a normal distribution (p-value = {p:.4f}).")
            else:
                logging.info(f"{column} follows a normal distribution (p-value = {p:.4f}).")

            # Statistical calculations
            mean = data_series.mean()
            median = data_series.median()
            mode = data_series.mode().values[0]  # Get the first mode
            data_range = data_series.max() - data_series.min()
            sample_size = data_series.count()
            std_dev = data_series.std()

            # Confidence Interval Calculation
            confidence_level = 0.95
            degrees_freedom = sample_size - 1
            confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=mean, scale=std_dev / (sample_size ** 0.5))
            lower_ci, upper_ci = confidence_interval

            # Log results with formatting
            logging.info(GREEN + "Statistical Results:\n" + RESET)
            # Update format_str to accommodate fewer arguments
            results_format_str = "{:<12}" + "{:>12}"
            logging.info(results_format_str.format("Mean:", YELLOW + f"{mean:.2f}" + RESET))
            logging.info(results_format_str.format("Median:", YELLOW + f"{median:.2f}" + RESET))
            logging.info(results_format_str.format("Mode:", YELLOW + f"{mode:.2f}" + RESET))
            logging.info(results_format_str.format("Range:", YELLOW + f"{data_range:.2f}" + RESET))
            logging.info(results_format_str.format("Sample Size:", YELLOW + f"{sample_size}" + RESET))
            logging.info(results_format_str.format("Std Dev:", YELLOW + f"{std_dev:.2f}" + RESET))
            logging.info(results_format_str.format("95% CI:", YELLOW + f"[{lower_ci:.2f}, {upper_ci:.2f}]" + RESET))
        else:
            logging.error(RED + f"Column '{column}' is not present in the data." + RESET)


    # Machine Learning
    def machine_learning(self, target_column):
        """Train a simple machine learning model."""
        if target_column not in self.data.columns:
            logging.error(RED + f"Target column '{target_column}' is missing from the data." + RESET)
            return
        
        X = self.data.drop(target_column, axis=1).select_dtypes(include=[np.number])  # Select numeric columns
        y = self.data[target_column]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression()
        model.fit(X_train, y_train)

        score = model.score(X_test, y_test)
        logging.info(GREEN + f"Linear Regression model R² score: {score:.4f}" + RESET)

    # Visualization
    def visualize_data(self, column, chart_type):
        """Visualize the data based on the chosen chart type."""
        if column not in self.data.columns:
            logging.error(RED + f"Column '{column}' is not present in the data." + RESET)
            return
        
        plt.figure(figsize=(10, 6))
        
        try:
            if chart_type == '1':  # Distribution Plot
                sns.histplot(self.data[column], kde=True)
                plt.title(f'Distribution of {column}')
            elif chart_type == '2':  # Bar Chart
                sns.countplot(x=column, data=self.data)
                plt.title(f'Bar Chart of {column}')
            elif chart_type == '3':  # Box Plot
                sns.boxplot(x=self.data[column])
                plt.title(f'Box Plot of {column}')
            elif chart_type == '4':  # Scatter Plot
                feature_column = input(BLUE + "Enter a feature column name for the scatter plot: " + RESET)
                if feature_column not in self.data.columns or not np.issubdtype(self.data[feature_column].dtype, np.number):
                    logging.error(f"Feature column '{feature_column}' must be numeric and present in the data.")
                    return
                sns.scatterplot(x=self.data[feature_column], y=self.data[column])
                plt.title(f'Scatter Plot of {column} vs {feature_column}')
            elif chart_type == '5':  # Scatter Plot with Linear Regression
                feature_column = input(BLUE + "\nEnter a feature column name for the regression plot: " + RESET)
                if feature_column not in self.data.columns or not np.issubdtype(self.data[feature_column].dtype, np.number):
                    logging.error(f"Feature column '{feature_column}' must be numeric and present in the data.")
                    return
                sns.regplot(x=self.data[feature_column], y=self.data[column])
                plt.title(f'Scatter Plot with Linear Regression of {column} vs {feature_column}')
            elif chart_type == '6':  # Histogram
                sns.histplot(self.data[column], bins=30)
                plt.title(f'Histogram of {column}')
            elif chart_type == '7':  # Pie Chart
                self.data[column].value_counts().plot.pie(autopct='%1.1f%%')
                plt.title(f'Pie Chart of {column}')
            else:
                logging.error("Invalid chart type selected.")
                return

            plt.show()
            logging.info(GREEN + f"\nSuccessfully displayed the {chart_type} for {column}." + RESET)
        except Exception as e:
            logging.error(RED + f"An error occurred while visualizing the data: {e}" + RESET)

# Main Function
def main():
    """Main function to run the DataVista application."""
    print(GREEN + f"\nWelcome to DataVista v{APP_VERSION}!" + RESET)
    print(GREEN + "Your companion for data analysis and visualization.\n" + RESET)

    parser = argparse.ArgumentParser(description="DataVista App")
    parser.add_argument('--data', type=str, help='Path to the CSV file', default='data/walmart_grocery_data.csv')
    args = parser.parse_args()

    app = DataVista()
    
    # Load data
    app.load_data(args.data)
    
    # Clean data
    app.clean_data()
    
    # Preprocess data
    app.preprocess_data()

    # User options
    while True:
        print(BLUE + "\nAvailable options:\n" + RESET)
        print("1. Perform Statistical Analysis")
        print("2. Train Machine Learning Model")
        print("3. Visualize Data")
        print("4. Exit")
        
        choice = input(BLUE + "\nChoose an option (1-4): " + RESET)
        
        if choice == '1':
            app.statistical_analysis()
        elif choice == '2':
            target_column = input(BLUE + "\nEnter the target column name for machine learning: " + RESET)
            app.machine_learning(target_column)
        elif choice == '3':
            feature_column = input(BLUE + "\nEnter a feature column name to visualize: " + RESET)
            print(BLUE + "\nChoose a chart type:\n" + RESET)
            print("1. Distribution Plot")
            print("2. Bar Chart")
            print("3. Box Plot")
            print("4. Scatter Plot")
            print("5. Scatter Plot with Linear Regression")
            print("6. Histogram")
            print("7. Pie Chart")
            chart_choice = input(BLUE + "\nEnter the chart type (1-7): " + RESET)
            app.visualize_data(feature_column, chart_choice)
        elif choice == '4':
            if input(YELLOW + "\nAre you sure you want to exit? (y/n): " + RESET).lower() == 'y':
                logging.info(GREEN + "Thanks for using DataVista. Goodbye!" + RESET)
                break
        else:
            logging.error("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()  # Execute the main function
