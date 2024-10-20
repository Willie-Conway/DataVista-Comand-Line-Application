import logging
import pandas as pd
from colorama import Fore
from scipy import stats

class StatisticalAnalysis:
    def __init__(self, data):
        self.data = data

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
        else:
            logging.error(Fore.RED + "Column not found in the dataset." + Fore.RESET)
