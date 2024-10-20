import logging
import pandas as pd
import numpy as np
from colorama import Fore
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

class StatisticalAnalysis:
    def __init__(self, data):
        self.data = data
        self.summary_report = []

    def perform_analysis(self):
        """Perform statistical analysis on numerical columns."""
        if self.data is None:
            logging.error(Fore.RED + "No data loaded for statistical analysis." + Fore.RESET)
            return
        
        logging.info(Fore.GREEN + "Statistical Summary:\n" + Fore.RESET)
        summary = self.data.describe()
        format_str = "{:<12}" + "{:>12}" * len(summary.columns)
        logging.info(format_str.format("Variable", *summary.columns))

        for index in summary.index:
            logging.info(format_str.format(index, *summary.loc[index]))

        column = input(Fore.BLUE + "\nEnter a column name for statistical analysis: " + Fore.RESET)
        if column in self.data.columns:
            if not np.issubdtype(self.data[column].dtype, np.number):
                logging.error(Fore.RED + f"Column '{column}' must be numeric for analysis." + Fore.RESET)
                return
            
            self.analyze_column(column)

            # Correlation Analysis
            self.perform_correlation_analysis()

            # Hypothesis Testing
            self.perform_hypothesis_testing()
        else:
            logging.error(Fore.RED + "Column not found in the dataset." + Fore.RESET)

    def analyze_column(self, column):
        """Analyze the specified column and log results."""
        data_series = self.data[column].dropna()
        mean = data_series.mean()
        median = data_series.median()
        mode = data_series.mode().values[0]
        data_range = data_series.max() - data_series.min()
        sample_size = data_series.count()
        std_dev = data_series.std()

        confidence_level = 0.95
        degrees_freedom = sample_size - 1
        confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=mean, scale=std_dev / (sample_size ** 0.5))
        lower_ci, upper_ci = confidence_interval

        logging.info(Fore.GREEN + "Statistical Results:\n" + Fore.RESET)
        results_format_str = "{:<12}" + "{:>12}"
        logging.info(results_format_str.format("Mean:", Fore.YELLOW + f"{mean:.2f}" + Fore.RESET))
        logging.info(results_format_str.format("Median:", Fore.YELLOW + f"{median:.2f}" + Fore.RESET))
        logging.info(results_format_str.format("Mode:", Fore.YELLOW + f"{mode:.2f}" + Fore.RESET))
        logging.info(results_format_str.format("Range:", Fore.YELLOW + f"{data_range:.2f}" + Fore.RESET))
        logging.info(results_format_str.format("Sample Size:", Fore.YELLOW + f"{sample_size}" + Fore.RESET))
        logging.info(results_format_str.format("Std Dev:", Fore.YELLOW + f"{std_dev:.2f}" + Fore.RESET))
        logging.info(results_format_str.format("Confidence Interval:", Fore.YELLOW + f"[{lower_ci:.2f}, {upper_ci:.2f}]" + Fore.RESET))

        # Log the summary report for later use
        self.summary_report.append({
            'column': column,
            'mean': mean,
            'median': median,
            'mode': mode,
            'range': data_range,
            'sample_size': sample_size,
            'std_dev': std_dev,
            'confidence_interval': (lower_ci, upper_ci)
        })

    def perform_correlation_analysis(self):
        """Perform correlation analysis on numerical columns."""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) < 2:
            logging.error(Fore.RED + "Not enough numeric columns for correlation analysis." + Fore.RESET)
            return

        logging.info(Fore.GREEN + "Correlation Analysis:\n" + Fore.RESET)
        correlation_matrix = self.data[numeric_cols].corr()
        logging.info(correlation_matrix)

        # Visualize the correlation heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

    def perform_hypothesis_testing(self):
        """Perform hypothesis testing (e.g., t-tests)."""
        print(Fore.BLUE + "\nChoose a hypothesis test:\n\n1. One-sample t-test\n2. Two-sample t-test\n" + Fore.RESET)
        test_choice = input(Fore.BLUE + "Enter your choice (1 or 2): " + Fore.RESET)

        if test_choice == '1':
            column = input(Fore.BLUE + "Enter the column for one-sample t-test: " + Fore.RESET)
            if column in self.data.columns:
                population_mean = float(input(Fore.BLUE + "Enter the population mean for comparison: " + Fore.RESET))
                t_stat, p_value = stats.ttest_1samp(self.data[column].dropna(), population_mean)
                logging.info(Fore.GREEN + f"One-sample t-test results: t-statistic = {t_stat}, p-value = {p_value}" + Fore.RESET)
            else:
                logging.error(Fore.RED + "Column not found." + Fore.RESET)
        elif test_choice == '2':
            column1 = input(Fore.BLUE + "Enter the first column for two-sample t-test: " + Fore.RESET)
            column2 = input(Fore.BLUE + "Enter the second column for two-sample t-test: " + Fore.RESET)
            if column1 in self.data.columns and column2 in self.data.columns:
                t_stat, p_value = stats.ttest_ind(self.data[column1].dropna(), self.data[column2].dropna())
                logging.info(Fore.GREEN + f"Two-sample t-test results: t-statistic = {t_stat}, p-value = {p_value}" + Fore.RESET)
            else:
                logging.error(Fore.RED + "One or both columns not found." + Fore.RESET)

    def print_summary_report(self):
        """Print a summary report of all analyses performed."""
        logging.info(Fore.GREEN + "\nSummary Report of Statistical Analysis:\n" + Fore.RESET)
        for report in self.summary_report:
            logging.info(report)
