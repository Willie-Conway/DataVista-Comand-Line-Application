import logging
import pandas as pd
import numpy as np
from colorama import Fore
from scipy import stats

class StatisticalAnalysis:
    def __init__(self, data):
        self.data = data
        self.summary_report = []

    def perform_analysis(self):
        """Perform statistical analysis on all numeric columns."""
        if self.data is None:
            logging.error(Fore.RED + "No data loaded for statistical analysis." + Fore.RESET)
            return
        
        logging.info(Fore.GREEN + "Statistical Summary for Numeric Columns:\n" + Fore.RESET)

        # Get all numeric columns
        numeric_columns = self.data.select_dtypes(include=[np.number]).columns.tolist()

        # Log the numeric columns found
        logging.info(Fore.BLUE + "Numeric columns detected: " + str(numeric_columns) + Fore.RESET)

        if not numeric_columns:
            logging.warning(Fore.YELLOW + "No numeric columns found in the dataset." + Fore.RESET)
            return

        # Numeric summary using describe() for all numeric columns
        numeric_summary = self.data[numeric_columns].describe()
        format_str = "{:<12}" + "{:>12}" * len(numeric_summary.columns)

        logging.info(format_str.format(Fore.GREEN + "Variable", *numeric_summary.columns) + Fore.RESET)

        for index in numeric_summary.index:
            rounded_values = [round(v, 2) for v in numeric_summary.loc[index]]  # Round all values
            logging.info(Fore.GREEN + format_str.format(index, *rounded_values) + Fore.RESET)

        # Non-numeric summary
        logging.info(Fore.GREEN + "\n\nNon-Numeric Columns Summary:" + Fore.RESET)
        for column in self.data.select_dtypes(exclude=[np.number]).columns:
            unique_values = self.data[column].unique()
            logging.info(Fore.GREEN + f"{column} : {unique_values}" + Fore.RESET)

        # Prompt user for analysis on a specific numeric column
        column = input(Fore.BLUE + "\nEnter a numeric column name for detailed analysis: " + Fore.RESET)
        if column in numeric_columns:
            self.analyze_column(column)
            self.perform_correlation_analysis()
        else:
            logging.error(Fore.RED + "Column not found in the dataset." + Fore.RESET)

    def analyze_column(self, column):
        """Analyze the specified column and log results."""
        data_series = self.data[column].dropna()
        logging.info(Fore.GREEN + f"Data for '{column}' (first 10 values): {data_series.head(10).values}" + Fore.RESET)

        # Use describe() for detailed statistics
        analysis_summary = data_series.describe()
        logging.info(Fore.GREEN + "Statistical Results:\n" + Fore.RESET)

        results_format_str = "{:<25}" + "{:>15}"
        for stat, value in analysis_summary.items():
            logging.info(Fore.GREEN + results_format_str.format(f"{stat.capitalize()}:", round(value, 2)) + Fore.RESET)

        # Confidence interval calculation
        sample_size = data_series.count()
        if sample_size > 1:
            mean = analysis_summary['mean']
            std_dev = analysis_summary['std']
            confidence_level = 0.95
            degrees_freedom = sample_size - 1
            confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=mean, scale=std_dev / (sample_size ** 0.5))
            lower_ci, upper_ci = confidence_interval
        else:
            lower_ci, upper_ci = np.nan, np.nan

        logging.info(Fore.GREEN + results_format_str.format("Confidence Interval:", f"[{lower_ci:.2f}, {upper_ci:.2f}]") + Fore.RESET)

        self.summary_report.append({
            'column': column,
            'mean': analysis_summary['mean'],
            'std_dev': analysis_summary['std'],
            'confidence_interval': (lower_ci, upper_ci)
        })

    def perform_correlation_analysis(self):
        """Perform correlation analysis on numeric columns."""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) < 2:
            logging.error(Fore.RED + "Not enough numeric columns for correlation analysis." + Fore.RESET)
            return

        logging.info(Fore.GREEN + "Correlation Analysis:\n" + Fore.RESET)
        correlation_matrix = self.data[numeric_cols].corr()
        logging.info(Fore.GREEN + str(correlation_matrix) + Fore.RESET)

    def print_summary_report(self):
        """Print a summary report of all analyses performed."""
        logging.info(Fore.GREEN + "\nSummary Report of Statistical Analysis:\n" + Fore.RESET)
        for report in self.summary_report:
            logging.info(Fore.GREEN + str(report) + Fore.RESET)

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    file_path = input(Fore.BLUE + "Enter the path to your dataset (CSV): " + Fore.RESET)
    try:
        data = pd.read_csv(file_path)
        analysis = StatisticalAnalysis(data)
        analysis.perform_analysis()
        analysis.print_summary_report()
    except Exception as e:
        logging.error(Fore.RED + f"Failed to load data: {e}" + Fore.RESET)
