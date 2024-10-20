### Data Flow Overview

1. **Loading Data** :

* User provides a CSV file path.
* `load_data()` reads the file and populates `self.data`.

1. **Cleaning Data** :

* `clean_data()` processes `self.data` to remove duplicates and handle missing values.

1. **Preprocessing Data** :

* `preprocess_data()` formats the data for analysis (e.g., date conversion).

1. **Statistical Analysis** :

* User selects a column for analysis.
* `statistical_analysis()` computes and logs various statistics.

1. **Machine Learning** :

* User specifies a target column.
* `machine_learning()` trains a model and logs the performance.

1. **Data Visualization** :

* User selects a visualization type and column.
* `visualize_data()` generates and displays the chart.
