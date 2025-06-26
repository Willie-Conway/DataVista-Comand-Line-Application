# WALKTHROUGH.md
![DataVista](https://github.com/Willie-Conway/DataVista-App/blob/62b22806b37009186f100531f50769ed98517397/assets/DataVista.png)

The **WALKTHROUGH.md** file serves as a comprehensive guide for users of the DataVista application. It documents step-by-step processes for various tasks, such as performing statistical analysis, training machine learning models, visualizing data, saving and loading models, performing clustering, conducting time series forecasting, and performing hypothesis testing. Each task includes clear instructions, user inputs, and expected outputs, making it easier for users to navigate the application and understand its functionalities. This structured approach enhances usability and facilitates learning for both new and experienced users.

## Table of Contents

1. [Task 1: Perform Statistical Analysis](#task-1-perform-statistical-analysis)
   - [Step 1: Load Data](#step-1-load-data)
   - [Step 2: Handle Missing Values](#step-2-handle-missing-values)
   - [Step 3: Scaling Features](#step-3-scaling-features)
   - [Step 4: Handle Outliers](#step-4-handle-outliers)
   - [Step 5: Perform Statistical Analysis](#step-5-perform-statistical-analysis)
   - [Correlation Analysis](#correlation-analysis)
   - [End of Walkthrough 1](#end-of-walkthrough-1)

2. [Task 2: Train Machine Learning Model](#task-2-train-machine-learning-model)
   - [Step 1: Choose Option](#step-1-choose-option)
   - [Step 2: Enter Target Column](#step-2-enter-target-column)
   - [Step 3: Choose Algorithm](#step-3-choose-algorithm)
   - [End of Walkthrough 2](#end-of-walkthrough-2)

3. [Task 3: Visualize Data](#task-3-visualize-data)
   - [Step 1: Choose Option](#step-1-choose-option-1)
   - [Step 2: Enter Feature Column Names](#step-2-enter-feature-column-names)
   - [Step 3: Choose Chart Type](#step-3-choose-chart-type)
   - [Step 4: Axis and Title Options](#step-4-axis-and-title-options)
   - [Step 5: Choose Color Palette](#step-5-choose-color-palette)
   - [Output](#output)
   - [End of Walkthrough 3](#end-of-walkthrough-3)

4. [Task 4: Load Model and View Loaded Model](#task-4-load-model-and-view-loaded-model)
   - [Step 1: Choose Option to Load Model](#step-1-choose-option-to-load-model)
   - [Step 2: Enter Filename to Load the Model](#step-2-enter-filename-to-load-the-model)
   - [Step 3: Confirmation of Model Load](#step-3-confirmation-of-model-load)
   - [Step 4: Choose Option to View Loaded Model](#step-4-choose-option-to-view-loaded-model)
   - [Step 5: View Model Details](#step-5-view-model-details)
   - [End of Walkthrough 4](#end-of-walkthrough-4)

5. [Task 5: Perform Clustering](#task-5-perform-clustering)
   - [Step 1: Choose Option to Perform Clustering](#step-1-choose-option-to-perform-clustering)
   - [Step 2: Enter Number of Clusters](#step-2-enter-number-of-clusters)
   - [Step 3: Confirmation of Clustering](#step-3-confirmation-of-clustering)
   - [Step 4: View Clusters Formed](#step-4-view-clusters-formed)
   - [End of Walkthrough 5](#end-of-walkthrough-5)

6. [Task 6: Time Series Forecasting](#task-6-time-series-forecasting)
   - [Step 1: Choose Option for Time Series Forecasting](#step-1-choose-option-for-time-series-forecasting)
   - [Step 2: Specify Target Column](#step-2-specify-target-column)
   - [Step 3: Enter ARIMA Order](#step-3-enter-arima-order)
   - [Step 4: View Forecast Results](#step-4-view-forecast-results)
   - [Step 5: Summary of Forecast](#step-5-summary-of-forecast)
   - [End of Walkthrough 6](#end-of-walkthrough-6)

7. [Task 7: Exit the Application](#task-7-exit-the-application)
   - [Step 1: Choose Option to Exit](#step-1-choose-option-to-exit)
   - [Step 2: Confirm Exit](#step-2-confirm-exit)
   - [Step 3: Exit Message](#step-3-exit-message)
   - [End of Walkthrough 7](#end-of-walkthrough-7)

8. [Task 8: Save Model](#task-8-save-model)
   - [Step 1: Choose Option to Save Model](#step-1-choose-option-to-save-model)
   - [Step 2: Enter Filename to Save the Model](#step-2-enter-filename-to-save-the-model)
   - [Step 3: Confirmation of Save](#step-3-confirmation-of-save)
   - [End of Walkthrough 8](#end-of-walkthrough-8)

9. [Task 9: Perform Hypothesis Testing](#task-9-perform-hypothesis-testing)
   - [Step 1: Choose Option](#step-1-choose-option)
   - [Step 2: Choose Test](#step-2-choose-test)
   - [Step 3: Enter Column Names for T-Test](#step-3-enter-column-names-for-t-test)
   - [Step 4: Enter Significance Level](#step-4-enter-significance-level)
   - [Output](#output)
   - [End of Walkthrough 9](#end-of-walkthrough-9)

---

 Here's the first walkthrough based on the output you provided for the **Perform Statistical Analysis** task:
  
## Task 1: Perform Statistical Analysis

### Step 1: Load Data
You start by loading the dataset `market_research.csv` with the following command:

```bash
python src/data_vista.py --data data/market_research.csv
```

### Output
 The application confirms the successful loading of the data and validates it:
  
```markdown

Welcome to DataVista v1.1.0!
Your companion for data analysis and visualization.

2024-10-22 18:59:44,346 - INFO - Data loaded successfully.
2024-10-22 18:59:44,346 - INFO - Data validation complete.
2024-10-22 18:59:44,353 - INFO - Removed duplicates: 10 -> 10 rows.
2024-10-22 18:59:44,353 - INFO - Current missing values:

2024-10-22 18:59:44,354 - INFO - product_id: 0
2024-10-22 18:59:44,354 - INFO - product_name: 0
2024-10-22 18:59:44,354 - INFO - category: 0
2024-10-22 18:59:44,354 - INFO - price: 0
2024-10-22 18:59:44,354 - INFO - market_share: 0

```

### Step 2: Handle Missing Values
You choose to remove rows with missing values:

```markdown
Choose an action for handling missing values:

1. Remove rows with missing values
2. Fill missing values
3. Skip to the next step

Enter your choice (1, 2, or 3): 1

Are you sure you want to remove rows with missing values? (y/n): y

```

### Output
The app provides a cleaning summary:

```markdown
2024-10-22 19:01:01,019 - INFO - Cleaning summary:

Initial rows: 10
Final rows: 10
Rows removed: 0
Rows filled: 0

```

### Step 3: Scaling Features
You choose not to scale the features:

```markdown
Choose an option for scaling features:

1. Scale features
2. Do not scale features

Enter your choice (1 or 2): 2

```

### Step 4: Handle Outliers
You opt to keep outliers:

```markdown
Choose an option for handling outliers:

1. Remove outliers
2. Keep outliers

Enter your choice (1 or 2): 2

```

### Output
The app confirms that preprocessing is complete:

```markdown

2024-10-22 19:01:31,069 - INFO - Skipping feature scaling. Original data retained.
2024-10-22 19:01:31,070 - INFO - Data preprocessing complete.

```

### Step 5: Perform Statistical Analysis
You select the option to perform statistical analysis:

```markdown
Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 1

```

### Output
The application displays the statistical summary for numeric columns:

```markdown

2024-10-22 19:05:50,925 - INFO - Statistical Summary for Numeric Columns:
2024-10-22 19:05:50,926 - INFO - Numeric columns detected: ['product_id', 'price', 'market_share']

```

### Detailed Analysis for price
You enter price for detailed analysis:

```markdown

Enter a numeric column name for detailed analysis: price

```

### Output
The app provides statistical results for the price variable:

```markdown

2024-10-22 19:06:33,366 - INFO - Data for 'price' (first 10 values): [ 25.99 149.99 699.99  59.99 999.99  35.99  89.99 199.99  29.99 249.99]
2024-10-22 19:06:33,366 - INFO - Statistical Results:
2024-10-22 19:06:33,366 - INFO - Count:                              10.0
2024-10-22 19:06:33,366 - INFO - Mean:                             254.19
2024-10-22 19:06:33,366 - INFO - Std:                              330.55
2024-10-22 19:06:33,366 - INFO - Min:                               25.99
2024-10-22 19:06:33,367 - INFO - 25%:                               41.99
2024-10-22 19:06:33,367 - INFO - 50%:                              119.99
2024-10-22 19:06:33,367 - INFO - 75%:                              237.49
2024-10-22 19:06:33,367 - INFO - Max:                              999.99
2024-10-22 19:06:33,373 - INFO - Confidence Interval:     [17.73, 490.65]

```

### Correlation Analysis
The application performs correlation analysis:

```markdown

2024-10-22 19:06:33,384 - INFO - Correlation Analysis:
2024-10-22 19:06:33,384 - INFO -               product_id     price  market_share     
product_id      1.000000 -0.122013     -0.046655
price          -0.122013  1.000000      0.740616
market_share   -0.046655  0.740616      1.000000

```
---
End of Walkthrough  1


Here’s the second walkthrough based on the output you provided for the **Train Machine Learning Model** task:

## Task 2: Train Machine Learning Model

### Step 1: Choose Option
You select the option to train a machine learning model from the main menu:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 2

```


### Step 2: Enter Target Column
You are prompted to enter the target column name for machine learning. You choose `price`:

```markdown

Enter the target column name for machine learning: price

```


### Step 3: Choose Algorithm
Next, you select the algorithm for training the model. You opt for `linear_regression`:

### Output
The application provides feedback on the training process:

```markdown

Choose an algorithm (linear_regression, decision_tree, logistic_regression): linear_regression
2024-10-22 20:01:41,300 - INFO - Model trained with MSE: 41223.787761441214, R^2: -10.45105215595589

```


---

End of Walkthrough  2

Here’s the third walkthrough based on the output you provided for the **Visualize Data** task:

## Task 3: Visualize Data

### Step 1: Choose Option
You select the option to visualize data from the main menu:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 3

```


### Step 2: Enter Feature Column Names
You are prompted to enter feature column names for visualization. You choose `category`:

```markdown

Enter feature column names to visualize (comma-separated): category

```


### Step 3: Choose Chart Type
Next, you select the type of chart to visualize the data. You opt for `Bar Chart`:

```markdown

Choose a chart type:

1. Histogram
2. Boxplot
3. Scatter Plot
4. Scatter Plot with Linear Regression
5. Bar Chart
6. Pie Chart
7. Correlation Heatmap
8. Distribution Plot (KDE)

Enter the chart type (1-8): 5

```


### Step 4: Axis and Title Options
You are asked if you want to name the x-axis and y-axis, to which you respond with `no`:

```markdown

Would you like to name the x-axis and y-axis? (y/n): n

```

You then choose to add a title to the chart and provide it as `Differences in Market Research by Category`:

```markdown

Would you like to add a title to the chart? (y/n): y

Enter the title for the chart: Differences in Market Research by Category

```


### Step 5: Choose Color Palette
Finally, you select a color palette for the chart, choosing `dark`:

```markdown

Choose a color palette:

1. deep
2. muted
3. bright
4. pastel
5. dark
6. colorblind
7. cubehelix
8. Set1
9. Set2
10. Set3
11. RdBu
12. viridis
13. plasma
14. cividis

Enter your choice (1-14, or press Enter for default): 5

```
### Output
Loads and displays  `Bar Chart` you selected.

![Bar Chart](https://tinypic.host/images/2024/10/23/Diffferences-in-Market-Research-by-Category-1.png)

---

End of Walkthrough 3

Here’s the fourth walkthrough based on the output you provided for the **Load Model** and **View Loaded Model** tasks:

## Task 4: Load Model and View Loaded Model

### Step 1: Choose Option to Load Model
You start by selecting the option to load a model from the main menu:

```markdown\

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 5

```

### Step 2: Enter Filename to Load the Model
You are prompted to enter the filename of the model you wish to load. You provide the path to the linear regression model:

```markdown

Enter filename to load the model: models/linear_regression_model.joblib

```


### Step 3: Confirmation of Model Load
Upon successful loading of the model, you receive a confirmation message:

```markdown

2024-10-22 22:42:17,104 - INFO - Model loaded from models/linear_regression_model.joblib.

```


### Step 4: Choose Option to View Loaded Model
After loading the model, you are again presented with the available options. You select the option to view the loaded model:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 6

```

### Step 5: View Model Details
You receive information about the loaded model, including its type, parameters, and coefficients:

```markdown

2024-10-22 22:42:26,555 - INFO - Model type: <class 'sklearn.linear_model._base.LinearRegression'> 2024-10-22 22:42:26,555 - INFO - Model parameters: {'copy_X': True, 'fit_intercept': True, 'n_jobs': None, 'positive': False} 2024-10-22 22:42:26,559 - INFO - Coefficients: [0.50038207 0.1858708 ]

```


---

End of Walkthrough 4

Here’s the fifth walkthrough based on the output you provided for the **Perform Clustering** task:

## Task 5: Perform Clustering

### Step 1: Choose Option to Perform Clustering
You start by selecting the option to perform clustering from the main menu:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 7

```

### Step 2: Enter Number of Clusters
You are prompted to enter the number of clusters for the K-means algorithm. You choose to create 2 clusters:

```markdown

Enter the number of clusters for K-means: 2

```


### Step 3: Confirmation of Clustering
After performing the clustering operation, you receive a confirmation message indicating that K-means clustering was successfully performed:

```markdown

2024-10-22 23:02:39,646 - INFO - K-Means clustering performed with 2 clusters.

```

### Step 4: View Clusters Formed
You also receive information about the clusters formed:

```markdown

Clusters formed: [0 0 1 0 1 0 0 0 0 0]

```


---

End of Walkthrough 5

Here’s the sixth walkthrough based on the output you provided for the **Time Series Forecasting** task:

## Task 6: Time Series Forecasting

### Step 1: Choose Option for Time Series Forecasting
You begin by selecting the option to perform time series forecasting from the main menu:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 8

```


### Step 2: Specify Target Column
You are prompted to enter the target column for forecasting. You choose to forecast the `price`:

```markdown

Enter the target column for time series forecasting: price

```


### Step 3: Enter ARIMA Order
Next, you need to specify the ARIMA order as three integers (p, d, q). You enter the order as `1 1 1`:

```markdown

Enter ARIMA order as three integers (p, d, q) separated by space: 1 1 1

```

### Step 4: View Forecast Results
The application performs the time series forecasting and provides the results:

```markdown

2024-10-22 23:09:04,300 - INFO - Time series forecast for price: 10 259.421787 11 256.698349 12 257.484744 13 257.257672 14 257.323239 Name: predicted_mean, dtype: float64

```

### Step 5: Summary of Forecast
The forecasted values for the next periods are displayed:

```markdown

Forecast: 10 259.421787 11 256.698349 12 257.484744 13 257.257672 14 257.323239 Name: predicted_mean, dtype: float64

```

---

End of Walkthrough 6

Here’s the seventh walkthrough based on the output you provided for the **Exit** task:

## Task 7: Exit the Application

### Step 1: Choose Option to Exit
You start by selecting the option to exit the application from the main menu:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 9

```

### Step 2: Confirm Exit
The application asks for confirmation to exit. You confirm by entering `y`:

```markdown

Are you sure you want to exit? (y/n): y

```

### Step 3: Exit Message
The application displays a goodbye message, indicating the end of your session:

```markdown

2024-10-22 23:16:55,560 - INFO - Thanks for using DataVista. Goodbye!

```

---

End of Walkthrough 7

Here’s the eighth walkthrough based on the output you provided for the **Save Model** task:

## Task 8: Save Model

### Step 1: Choose Option to Save Model
You start by selecting the option to save the trained machine learning model from the main menu:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

Choose an option (1-9): 4

```
### Step 2: Enter Filename to Save the Model
You are prompted to enter a filename to save the model. You choose to save it as `models/decision_tree_model.joblib:`

```markdown

Enter filename to save the model: models/decision_tree_model.joblib

```

### Step 3: Confirmation of Save
The application confirms that the model has been successfully saved:

```markdown

2024-10-22 23:35:36,620 - INFO - Model saved to models/decision_tree_model.joblib.

```

---

End of Walkthrough 8

## Task 9: Perform Hypothesis Testing

### Step 1: Choose Option
You start by selecting the option to perform hypothesis testing from the main menu:

```markdown

Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Perform Hypothesis Testing
10. Exit

The model saving task is complete.

```

### Step 2: Choose Test
You are prompted to choose a test type. You select the T-Test:

```markdown

Choose a test:

1. T-Test
2. Chi-Squared Test

Enter the number corresponding to your choice: 1

T-Test Selected

```

### Step 3: Enter Column Names for T-Test
You are asked to enter the first and second numeric column names for the T-Test. You choose `price` and `market_share`:

```markdown

Enter the first numeric column name for T-Test: price

Enter the second numeric column name for T-Test: market_share

```

### Step 4: Enter Significance Level
You specify the significance level for the test, defaulting to `0.05`:

```markdown

Enter significance level (default 0.05): 0.05

```

### Output
The application displays the results of the T-Test:

```markdown

2024-10-23 03:02:28,938 - INFO - T-test results for 'price' and 'market_share':
2024-10-23 03:02:28,939 - INFO - Statistic: 2.3031217001503737, P-value: 0.03341630467717743
2024-10-23 03:02:28,939 - INFO - Reject the null hypothesis.

```
---
End of Walkthrough 9
