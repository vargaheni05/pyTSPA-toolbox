pyTSPA Example Usage
=====================

Interactive Colab Notebook
---------------------------

For an interactive demonstration of the pyTSPA toolbox, visit the Colab notebook:

.. raw:: html

   <a href="https://colab.research.google.com/drive/1fKSwwWb85Zb0z_N65EPa_3mWJwH6juC4?usp=sharing#scrollTo=1aQrAPRPJRuW">Colab Notebook</a>

Data Handling
-------------
The `data.py` module provides functions for loading, cleaning, and profiling match data.  
These functions are designed to efficiently process raw match data, ensuring it is clean and well-structured for further analysis.  

**Steps:**  
1. Load the raw data from CSV or Excel.  
2. Clean the data, including handling missing values.  
3. Profile the data to understand its structure and basic statistics.  

.. code-block:: python

    from pyTSPA.data import load_match_data, clean_data, data_profiling

    # Load sample data
    data_path = "path/to/match_data.csv"
    df = load_match_data(data_path)

    # Data cleaning
    df_cleaned = clean_data(df)

    # Data profiling
    data_profiling(df_cleaned)

Metrics Calculation
-------------------
The `metrics.py` module is the core of the toolbox, providing statistical analysis and prediction capabilities.  
It offers functions to calculate performance metrics for individual teams and the entire league.  

In addition to basic metrics like **Win Percentage** and **Goal Difference**, the module also supports machine learning-based predictions.  
The logistic regression model predicts match outcomes (Home Win, Draw, Away Win) based on calculated metrics such as the **Pythagorean Expectation**.  

**Steps:**  

1. Calculate match and team-level statistics.

2. Predict match outcomes using logistic regression.  

3. Generate a second-half prediction based on the first-half performance.  

.. code-block:: python

    from pyTSPA.metrics import result_stats, team_performance, each_win_percentage, logistic_regression_prediction, season_half_prediction

    # Step 1: Match result statistics
    stats = result_stats(df_cleaned)
    print("Overall Result Statistics:", stats)

    # Step 2: Calculate team performance metrics
    team_stats = team_performance(df_cleaned, "Arsenal")
    print("Arsenal Performance:", team_stats)

    # Step 3: Calculate win percentage for all teams
    win_perc = each_win_percentage(df_cleaned)
    print("Win Percentage for all teams:", win_perc)

    # Step 4: Logistic regression prediction
    prediction_result = logistic_regression_prediction(df_cleaned)
    print("Prediction Accuracy:", prediction_result["accuracy"])
    print("Confusion Matrix:", prediction_result["confusion_matrix"])

**Explanation:**  
The logistic regression model uses the calculated metrics to predict the match outcomes.  
It employs a multinomial logistic regression algorithm, which can handle three possible outcomes (Home Win, Draw, Away Win).  
To handle the imbalance in the dataset (e.g., fewer draws), the model uses **SMOTE** for oversampling.  

The model is evaluated using accuracy and a confusion matrix, which compares the predicted and actual outcomes.  
The predicted outcomes can be further visualized to compare the model's effectiveness.  

.. code-block:: python

    # Step 5: Predict outcomes for the second half of the season
    second_half_predictions = season_half_prediction(df_cleaned)
    print("Second Half Predictions:", second_half_predictions.head())

Visualization
-------------
The `visualization.py` module is used to create plots for visualizing the calculated metrics and prediction results.  
These visualizations help identify patterns and trends, making the data analysis more intuitive.  

**Steps:**

1. Visualize the overall result distribution. 

2. Plot team-specific match outcomes.  

3. Generate a league points table.  

4. Visualize the Pythagorean Expectation and compare it with actual points.  

.. code-block:: python

    from pyTSPA.visualization import plot_result_distribution, plot_team_results, plot_league_points_table, plot_pythagorean_expectation

    # Step 1: Plot result distribution for the whole league
    plot_result_distribution(df_cleaned)

    # Step 2: Plot match outcomes for a specific team
    plot_team_results(df_cleaned, "Arsenal")

    # Step 3: Plot the league points table
    league_stats = each_team_performance(df_cleaned)
    plot_league_points_table(league_stats)

    # Step 4: Plot the Pythagorean Expectation
    league_stats = league_stats.merge(each_pythagorean_expectation(df_cleaned), on="Team")
    plot_pythagorean_expectation(league_stats)

**Explanation:**  
The visualizations are created using **Seaborn** and **Matplotlib**, focusing on clarity and accuracy.  
The league table plot helps visualize the points distribution, while the Pythagorean Expectation plot compares expected and actual points.

This example guide provides an overview of the main functionalities in the pyTSPA toolbox, covering data handling, metrics calculation, and visualization.  
For a more comprehensive and interactive walkthrough, refer to the Colab notebook linked above.
