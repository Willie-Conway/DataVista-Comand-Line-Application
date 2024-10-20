import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from colorama import Fore

class Visualization:
    def __init__(self, data):
        self.data = data

    def visualize(self, columns, chart_type):
        """Visualize data using various chart types."""
        if self.data is None:
            logging.error(Fore.RED + "No data loaded for visualization." + Fore.RESET)
            return

        for column in columns:
            if column not in self.data.columns:
                logging.error(Fore.RED + f"Column '{column}' not found in the dataset." + Fore.RESET)
                return

        if self.data.empty:
            logging.error(Fore.RED + "The dataset is empty." + Fore.RESET)
            return

        try:
            color_palette = self.choose_color_palette()

            if chart_type == '1':  # Histogram
                plt.figure()
                for column in columns:
                    self.data[column].hist(alpha=0.5, color=color_palette[0], label=column)
                plt.title('Histogram')
                plt.xlabel('Value')
                plt.ylabel('Frequency')
                plt.legend()
                self.show_or_save_plot()

            elif chart_type == '2':  # Boxplot
                plt.figure()
                sns.boxplot(data=self.data[columns], palette=color_palette)
                plt.title('Boxplot')
                self.show_or_save_plot()

            elif chart_type == '3':  # Scatter Plot
                plt.figure()
                for column in columns:
                    plt.scatter(self.data.index, self.data[column], alpha=0.5, label=column)
                plt.title('Scatter Plot')
                plt.xlabel('Index')
                plt.ylabel('Value')
                plt.legend()
                self.show_or_save_plot()

            elif chart_type == '4':  # Scatter Plot with Linear Regression
                plt.figure()
                for column in columns:
                    sns.regplot(x=self.data.index, y=self.data[column], label=column)
                plt.title('Scatter Plot with Linear Regression')
                plt.legend()
                self.show_or_save_plot()

            elif chart_type == '5':  # Bar Chart
                plt.figure()
                for column in columns:
                    self.data[column].value_counts().plot(kind='bar', alpha=0.5, label=column)
                plt.title('Bar Chart')
                plt.xlabel('Categories')
                plt.ylabel('Count')
                plt.legend()
                self.show_or_save_plot()

            elif chart_type == '6':  # Pie Chart
                plt.figure()
                for column in columns:
                    self.data[column].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=color_palette, label=column)
                    plt.title(f'Pie Chart of {column}')
                    plt.show()  # Pie charts often do not require saving

            elif chart_type == '7':  # Correlation Heatmap
                plt.figure(figsize=(10, 8))
                sns.heatmap(self.data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
                plt.title('Correlation Heatmap')
                self.show_or_save_plot()

            elif chart_type == '8':  # Distribution Plot (KDE)
                plt.figure()
                for column in columns:
                    sns.kdeplot(self.data[column], label=column, fill=True, alpha=0.5)
                plt.title('Distribution Plot (KDE)')
                plt.xlabel('Value')
                plt.ylabel('Density')
                plt.legend()
                self.show_or_save_plot()

            else:
                logging.error(Fore.RED + "Invalid chart type selected." + Fore.RESET)

        except Exception as e:
            logging.error(Fore.RED + f"An error occurred while visualizing: {str(e)}" + Fore.RESET)

    def choose_color_palette(self):
        """Allow users to select a color palette for visualizations."""
        palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind']
        print(Fore.BLUE + "\nChoose a color palette:\n" + Fore.RESET)
        for i, palette in enumerate(palettes, 1):
            print(f"{i}. {palette}")
        
        choice = input(Fore.BLUE + "\nEnter your choice (1-6, or press Enter for default): " + Fore.RESET)
        if choice.isdigit() and 1 <= int(choice) <= len(palettes):
            return sns.color_palette(palettes[int(choice) - 1])
        else:
            return sns.color_palette()  # Default palette

    def show_or_save_plot(self):
        """Display the plot or save it to a file based on user input."""
        action = input(Fore.BLUE + "\nWould you like to save this plot? (y/n): " + Fore.RESET)
        if action.lower() == 'y':
            filename = input(Fore.BLUE + "Enter the filename (without extension): " + Fore.RESET)
            plt.savefig(f"{filename}.png")  # Save as PNG by default
            logging.info(Fore.GREEN + f"Plot saved as {filename}.png" + Fore.RESET)
        plt.show()  # Show the plot regardless of save option
