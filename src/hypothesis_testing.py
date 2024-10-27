import logging
import pandas as pd
from scipy import stats
from colorama import Fore

class HypothesisTesting:
    def __init__(self, data):
        self.data = data

    def _validate_columns(self, *columns):
        """Check if columns exist and have appropriate data types."""
        for column in columns:
            if column not in self.data.columns:
                logging.error(Fore.RED + f"Column '{column}' not found in the dataset." + Fore.RESET)
                return False
            # Allow both numeric and categorical types for Chi-squared test
            if self.data[column].dtype not in ['int64', 'float64', 'object', 'category']:
                logging.error(Fore.RED + f"Column '{column}' must be numeric or categorical." + Fore.RESET)
                return False
        return True

    def _check_sufficiency(self, column):
        """Ensure there are enough data points in the column."""
        if self.data[column].dropna().shape[0] < 2:
            logging.error(Fore.RED + f"Not enough data points in '{column}' to perform the test." + Fore.RESET)
            return False
        return True

    def t_test(self, column1, column2, alpha=0.05):
        """Perform a two-sample t-test."""
        if not self._validate_columns(column1, column2):
            return
        if not self._check_sufficiency(column1) or not self._check_sufficiency(column2):
            return

        group1 = self.data[column1].dropna()
        group2 = self.data[column2].dropna()
        stat, p_value = stats.ttest_ind(group1, group2)

        logging.info(Fore.GREEN + f"T-test results for '{column1}' and '{column2}':" + Fore.RESET)
        logging.info(Fore.GREEN + f"Sample Size: {len(group1)} vs {len(group2)}" + Fore.RESET)
        logging.info(Fore.GREEN + f"Means: {group1.mean()} vs {group2.mean()}" + Fore.RESET)
        logging.info(Fore.GREEN + f"Statistic: {stat}, P-value: {p_value}" + Fore.RESET)

        if p_value < alpha:
            logging.info(Fore.GREEN + "Reject the null hypothesis." + Fore.RESET)
        else:
            logging.info(Fore.GREEN + "Fail to reject the null hypothesis." + Fore.RESET)

    def chi_squared_test(self, column1, column2, alpha=0.05):
        """Perform a chi-squared test for independence."""
        if not self._validate_columns(column1, column2):
            return

        contingency_table = pd.crosstab(self.data[column1], self.data[column2])
        stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)

        logging.info(Fore.GREEN + f"Chi-squared test results for '{column1}' and '{column2}':" + Fore.RESET)
        logging.info(Fore.GREEN + f"Contingency Table:\n{contingency_table}" + Fore.RESET)
        logging.info(Fore.GREEN + f"Statistic: {stat}, P-value: {p_value}, Degrees of Freedom: {dof}" + Fore.RESET)

        if p_value < alpha:
            logging.info(Fore.GREEN + "Reject the null hypothesis." + Fore.RESET)
        else:
            logging.info(Fore.GREEN + "Fail to reject the null hypothesis." + Fore.RESET)

    def one_sample_t_test(self, column, population_mean, alpha=0.05):
        """Perform a one-sample t-test."""
        if not self._validate_columns(column):
            return
        if not self._check_sufficiency(column):
            return

        sample = self.data[column].dropna()
        stat, p_value = stats.ttest_1samp(sample, population_mean)

        logging.info(Fore.GREEN + f"One-sample T-test results for '{column}':" + Fore.RESET)
        logging.info(Fore.GREEN + f"Sample Size: {len(sample)}, Sample Mean: {sample.mean()}" + Fore.RESET)
        logging.info(Fore.GREEN + f"Statistic: {stat}, P-value: {p_value}" + Fore.RESET)

        if p_value < alpha:
            logging.info(Fore.GREEN + "Reject the null hypothesis." + Fore.RESET)
        else:
            logging.info(Fore.GREEN + "Fail to reject the null hypothesis." + Fore.RESET)

    def paired_t_test(self, column1, column2, alpha=0.05):
        """Perform a paired t-test."""
        if not self._validate_columns(column1, column2):
            return
        if not self._check_sufficiency(column1) or not self._check_sufficiency(column2):
            return

        group1 = self.data[column1].dropna()
        group2 = self.data[column2].dropna()

        if len(group1) != len(group2):
            logging.error(Fore.RED + "Columns must have the same number of data points for paired t-test." + Fore.RESET)
            return

        stat, p_value = stats.ttest_rel(group1, group2)

        logging.info(Fore.GREEN + f"Paired T-test results for '{column1}' and '{column2}':" + Fore.RESET)
        logging.info(Fore.GREEN + f"Sample Size: {len(group1)}, Means: {group1.mean()} vs {group2.mean()}" + Fore.RESET)
        logging.info(Fore.GREEN + f"Statistic: {stat}, P-value: {p_value}" + Fore.RESET)

        if p_value < alpha:
            logging.info(Fore.GREEN + "Reject the null hypothesis." + Fore.RESET)
        else:
            logging.info(Fore.GREEN + "Fail to reject the null hypothesis." + Fore.RESET)

    def effect_size(self, column1, column2):
        """Calculate Cohen's d for two samples."""
        if not self._validate_columns(column1, column2):
            return

        group1 = self.data[column1].dropna()
        group2 = self.data[column2].dropna()

        d = (group1.mean() - group2.mean()) / ((group1.std(ddof=1) + group2.std(ddof=1)) / 2)
        logging.info(Fore.GREEN + f"Cohen's d effect size for '{column1}' and '{column2}': {d}" + Fore.RESET)

    def output_summary(self, column1, column2):
        """Output a structured summary of the test results."""
        logging.info(Fore.GREEN + f"Summary for '{column1}' and '{column2}':" + Fore.RESET)
        # Placeholder for expanded summary implementation
