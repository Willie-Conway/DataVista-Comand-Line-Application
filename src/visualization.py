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

        # Check if columns exist in the dataset
        for column in columns:
            if column not in self.data.columns:
                logging.error(Fore.RED + f"Column '{column}' not found in the dataset." + Fore.RESET)
                return

        if self.data.empty:
            logging.error(Fore.RED + "The dataset is empty." + Fore.RESET)
            return

        # Identify numeric and categorical columns
        numeric_columns = self.data[columns].select_dtypes(include=['number']).columns.tolist()
        categorical_columns = self.data[columns].select_dtypes(include=['object', 'category']).columns.tolist()

        if len(numeric_columns) + len(categorical_columns) == 0:
            logging.error(Fore.RED + "No numeric or categorical columns selected for visualization." + Fore.RESET)
            return

        # Ask for labels and title
        x_label, y_label, chart_title = self.get_chart_labels()

        # Choose a color palette
        color_palette = self.choose_color_palette()

        try:
            y_range = None
            
            if numeric_columns:
                _, y_range = self.get_axis_ranges(numeric_columns)  # Only get y_range

            if chart_type == '1':  # Histogram
                plt.figure()
                for idx, column in enumerate(numeric_columns):
                    plt.hist(self.data[column], bins=10, alpha=0.5, color=color_palette[idx % len(color_palette)], label=column)
                plt.title(chart_title or 'Histogram')
                plt.xlabel(x_label or 'Value')
                plt.ylabel('Frequency')
                plt.ylim(y_range)  # Set y-axis limit
                plt.legend()
                self.show_or_save_plot()

            elif chart_type == '2':  # Boxplot
                plt.figure()
                sns.boxplot(data=self.data[numeric_columns], palette=color_palette)
                plt.title(chart_title or 'Boxplot')
                plt.ylabel(y_label or 'Value')
                plt.ylim(y_range)  # Set y-axis limit
                self.show_or_save_plot()

            elif chart_type == '3':  # Scatter Plot
                plt.figure()
                if len(categorical_columns) > 0:
                    category_column = categorical_columns[0]
                    selected_categories = self.select_categories(self.data[category_column].unique())
                    for idx, category in enumerate(selected_categories):
                        subset = self.data[self.data[category_column] == category]
                        plt.scatter(subset[numeric_columns[0]], subset[numeric_columns[1]], alpha=0.5, color=color_palette[idx % len(color_palette)], label=category)
                    plt.title(chart_title or 'Scatter Plot')
                    plt.xlabel(x_label or numeric_columns[0])
                    plt.ylabel(y_label or numeric_columns[1])
                    plt.ylim(y_range)  # Set y-axis limit
                    plt.legend()
                self.show_or_save_plot()

            elif chart_type == '4':  # Scatter Plot with Linear Regression
                plt.figure()
                if numeric_columns:
                    sns.regplot(x=self.data[numeric_columns[0]], y=self.data[numeric_columns[1]], color=color_palette[0])
                    plt.ylim(y_range)  # Set y-axis limit
                plt.title(chart_title or 'Scatter Plot with Linear Regression')
                plt.xlabel(x_label or numeric_columns[0])
                plt.ylabel(y_label or numeric_columns[1])
                self.show_or_save_plot()

            elif chart_type == '5':  # Bar Chart
                plt.figure()
                for column in categorical_columns:
                    self.data[column].value_counts().plot(kind='bar', color=color_palette, alpha=0.7)
                    plt.title(chart_title or 'Bar Chart')
                    plt.xlabel(x_label or 'Categories')
                    plt.ylabel('Count')
                    plt.ylim(y_range)  # Set y-axis limit
                    plt.legend()
                    plt.show()

            elif chart_type == '6':  # Pie Chart
                for column in categorical_columns:
                    plt.figure()
                    self.data[column].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=color_palette)
                    plt.title(chart_title or f'Pie Chart of {column}')
                    plt.ylabel('')
                    plt.show()

            elif chart_type == '7':  # Correlation Heatmap
                plt.figure(figsize=(10, 8))
                sns.heatmap(self.data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
                plt.title(chart_title or 'Correlation Heatmap')
                self.show_or_save_plot()

            elif chart_type == '8':  # Distribution Plot (KDE)
                plt.figure()
                for idx, column in enumerate(numeric_columns):
                    sns.kdeplot(self.data[column], label=column, fill=True, alpha=0.5, color=color_palette[idx % len(color_palette)])
                plt.title(chart_title or 'Distribution Plot (KDE)')
                plt.xlabel(x_label or 'Value')
                plt.ylabel('Density')
                plt.ylim(0, self.data[numeric_columns].max().max() * 1.1)  # Set y-axis limit
                plt.legend()
                self.show_or_save_plot()

            else:
                logging.error(Fore.RED + "Invalid chart type selected." + Fore.RESET)

        except Exception as e:
            logging.error(Fore.RED + f"An error occurred while visualizing: {str(e)}" + Fore.RESET)

    def get_chart_labels(self):
        """Get labels and title from user with input validation."""
        x_label, y_label = None, None

        label_axes = input(Fore.BLUE + "\nWould you like to name the x-axis and y-axis? (y/n): " + Fore.RESET).lower()
        while label_axes not in ['y', 'n']:
            logging.error(Fore.RED + "Invalid input. Please enter 'y' or 'n'." + Fore.RESET)
            label_axes = input(Fore.BLUE + "Would you like to name the x-axis and y-axis? (y/n): " + Fore.RESET).lower()

        if label_axes == 'y':
            x_label = input(Fore.BLUE + "\nEnter label for the x-axis: " + Fore.RESET)
            y_label = input(Fore.BLUE + "\nEnter label for the y-axis: " + Fore.RESET)

        title_option = input(Fore.BLUE + "\nWould you like to add a title to the chart? (y/n): " + Fore.RESET).lower()
        while title_option not in ['y', 'n']:
            logging.error(Fore.RED + "Invalid input. Please enter 'y' or 'n'." + Fore.RESET)
            title_option = input(Fore.BLUE + "Would you like to add a title to the chart? (y/n): " + Fore.RESET).lower()

        chart_title = ""
        if title_option == 'y':
            chart_title = input(Fore.BLUE + "\nEnter the title for the chart: " + Fore.RESET)

        return x_label, y_label, chart_title

    def get_axis_ranges(self, numeric_columns):
        """Prompt user for y-axis limits only."""
        y_range = None

        if numeric_columns:
            print(Fore.BLUE + "\nSet range for the y-axis (leave empty for default):\n")

            # Set y-axis limits
            y_min = input(Fore.BLUE + f"Enter minimum y value (default is {self.data[numeric_columns[0]].min()}): " + Fore.RESET)
            y_max = input(Fore.BLUE + f"Enter maximum y value (default is {self.data[numeric_columns[0]].max()}): " + Fore.RESET)
            y_range = (float(y_min) if y_min else 0,
                        float(y_max) if y_max else self.data[numeric_columns[0]].max() * 1.1)

        return None, y_range  # Return None for x_range and the specified y_range

    def choose_color_palette(self):
        """Allow users to select a color palette for visualizations."""
        palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind', 'cubehelix', 'Set1', 'Set2', 'Set3', 'RdBu', 'viridis', 'plasma', 'cividis']
        print(Fore.BLUE + "\nChoose a color palette:\n" + Fore.RESET)
        for i, palette in enumerate(palettes, 1):
            print(f"{i}. {palette}")

        choice = input(Fore.BLUE + "\nEnter your choice (1-14, or press Enter for default): " + Fore.RESET)
        if choice.isdigit() and 1 <= int(choice) <= len(palettes):
            return sns.color_palette(palettes[int(choice) - 1])
        else:
            return sns.color_palette()  # Default palette

    def select_categories(self, categories):
        """Allow users to select specific categories for visualization."""
        print(Fore.BLUE + "\nAvailable categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        selected_indices = input(Fore.BLUE + "\nEnter the numbers of the categories you want to visualize (comma-separated): " + Fore.RESET)
        selected_indices = [int(i.strip()) - 1 for i in selected_indices.split(',') if i.strip().isdigit() and 0 < int(i.strip()) <= len(categories)]

        selected_categories = [categories[i] for i in selected_indices]
        return selected_categories

    def show_or_save_plot(self):
        """Display the plot or save it to a file based on user input."""
        action = input(Fore.BLUE + "\nWould you like to save this plot? (y/n): " + Fore.RESET)
        if action.lower() == 'y':
            filename = input(Fore.BLUE + "Enter the filename (without extension): " + Fore.RESET)
            plt.savefig(f"{filename}.png")  # Save as PNG by default
            logging.info(Fore.GREEN + f"Plot saved as {filename}.png" + Fore.RESET)
        plt.show()
