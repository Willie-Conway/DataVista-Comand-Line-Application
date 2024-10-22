# WALKTHROUGH.md
 Here's the first walkthrough based on the output you provided for the **Perform Statistical Analysis** task:
  
## Task 1: Perform Statistical Analysis

### Step 1: Load Data
You start by loading the dataset `market_research.csv` with the following command:

```bash
python src/data_vista.py --data data/market_research.csv
```

### Output
 The application confirms the successful loading of the data and validates it:
  
```python

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

```python
Choose an action for handling missing values:

1. Remove rows with missing values
2. Fill missing values
3. Skip to the next step

Enter your choice (1, 2, or 3): 1

Are you sure you want to remove rows with missing values? (y/n): y

```

### Output
The app provides a cleaning summary:

```python
2024-10-22 19:01:01,019 - INFO - Cleaning summary:

Initial rows: 10
Final rows: 10
Rows removed: 0
Rows filled: 0

```

### Step 3: Scaling Features
You choose not to scale the features:

```python
Choose an option for scaling features:

1. Scale features
2. Do not scale features

Enter your choice (1 or 2): 2

```

### Step 4: Handle Outliers
You opt to keep outliers:

```python
Choose an option for handling outliers:

1. Remove outliers
2. Keep outliers

Enter your choice (1 or 2): 2

```

### Output
The app confirms that preprocessing is complete:

```python

2024-10-22 19:01:31,069 - INFO - Skipping feature scaling. Original data retained.
2024-10-22 19:01:31,070 - INFO - Data preprocessing complete.

```

### Step 5: Perform Statistical Analysis
You select the option to perform statistical analysis:

```python
Available options:

1. Perform Statistical Analysis
2. Train Machine Learning Model
3. Visualize Data
4. Save Model
5. Load Model
6. View Loaded Model
7. Perform Clustering
8. Time Series Forecasting
9. Exit

Choose an option (1-9): 1

```

### Output
The application displays the statistical summary for numeric columns:

```python

2024-10-22 19:05:50,925 - INFO - Statistical Summary for Numeric Columns:
2024-10-22 19:05:50,926 - INFO - Numeric columns detected: ['product_id', 'price', 'market_share']

```

### Detailed Analysis for price
You enter price for detailed analysis:

```python

Enter a numeric column name for detailed analysis: price

```

### Output
The app provides statistical results for the price variable:

```python

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

```python

2024-10-22 19:06:33,384 - INFO - Correlation Analysis:
2024-10-22 19:06:33,384 - INFO -               product_id     price  market_share     
product_id      1.000000 -0.122013     -0.046655
price          -0.122013  1.000000      0.740616
market_share   -0.046655  0.740616      1.000000

```
