import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from colorama import Fore

class Visualization:
    def __init__(self, data):
        self.data = data

    def visualize(self, column, chart_type):
        """Visualize data using various chart types."""
        if self.data is None:
            logging.error(Fore.RED + "No data loaded for visualization." + Fore.RESET)
            return

        if column not in self.data.columns:
            logging.error(Fore.RED + f"Column '{column}' not found in the dataset." + Fore.RESET)
            return

        if self.data.empty:
            logging.error(Fore.RED + "The dataset is empty." + Fore.RESET)
            return

        try:
            if chart_type == '1':  # Histogram
                self.data[column].hist()
                plt.title(f'Histogram of {column}')
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plt.show()

            elif chart_type == '2':  # Boxplot
                sns.boxplot(x=self.data[column])
                plt.title(f'Boxplot of {column}')
                plt.show()

            elif chart_type == '3':  # Scatter Plot
                plt.scatter(self.data.index, self.data[column])
                plt.title(f'Scatter Plot of {column}')
                plt.xlabel('Index')
                plt.ylabel(column)
                plt.show()

            elif chart_type == '4':  # Scatter Plot with Linear Regression
                sns.regplot(x=self.data.index, y=self.data[column])
                plt.title(f'Scatter Plot with Linear Regression of {column}')
                plt.show()

            elif chart_type == '5':  # Bar Chart
                self.data[column].value_counts().plot(kind='bar')
                plt.title(f'Bar Chart of {column}')
                plt.xlabel(column)
                plt.ylabel('Count')
                plt.show()

            elif chart_type == '6':  # Pie Chart
                self.data[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
                plt.title(f'Pie Chart of {column}')
                plt.show()

            elif chart_type == '7':  # Correlation Heatmap
                plt.figure(figsize=(10, 8))
                sns.heatmap(self.data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
                plt.title('Correlation Heatmap')
                plt.show()

            else:
                logging.error(Fore.RED + "Invalid chart type selected." + Fore.RESET)

        except Exception as e:
            logging.error(Fore.RED + f"An error occurred while visualizing: {str(e)}" + Fore.RESET)
