import logging
import pandas as pd
from scipy import stats
from colorama import Fore

class HypothesisTesting:
    def __init__(self, data):
        self.data = data

    def t_test(self, column1, column2, alpha=0.05):
        """Perform a two-sample t-test."""
        if column1 not in self.data.columns or column2 not in self.data.columns:
            logging.error(Fore.RED + "One or both columns not found in the dataset." + Fore.RESET)
            return
        
        stat, p_value = stats.ttest_ind(self.data[column1].dropna(), self.data[column2].dropna())
        logging.info(Fore.GREEN + f"T-test results for '{column1}' and '{column2}':" + Fore.RESET)
        logging.info(Fore.GREEN + f"Statistic: {stat}, P-value: {p_value}" + Fore.RESET)

        if p_value < alpha:
            logging.info(Fore.GREEN + "Reject the null hypothesis." + Fore.RESET)
        else:
            logging.info(Fore.GREEN + "Fail to reject the null hypothesis." + Fore.RESET)

    def chi_squared_test(self, column1, column2, alpha=0.05):
        """Perform a chi-squared test for independence."""
        if column1 not in self.data.columns or column2 not in self.data.columns:
            logging.error(Fore.RED + "One or both columns not found in the dataset." + Fore.RESET)
            return
        
        contingency_table = pd.crosstab(self.data[column1], self.data[column2])
        stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        logging.info(Fore.GREEN + f"Chi-squared test results for '{column1}' and '{column2}':" + Fore.RESET)
        logging.info(Fore.GREEN + f"Statistic: {stat}, P-value: {p_value}" + Fore.RESET)

        if p_value < alpha:
            logging.info(Fore.GREEN + "Reject the null hypothesis." + Fore.RESET)
        else:
            logging.info(Fore.GREEN + "Fail to reject the null hypothesis." + Fore.RESET)
