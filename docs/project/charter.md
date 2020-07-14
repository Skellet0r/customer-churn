# Project Charter

## Business background

- Who is the client, what business domain the client is in.
  - Our client is SyriaTel, a telecommunications company based in the United States.
- What business problems are we trying to address?
  - Our client is losing money when customers stop doing business with them.
    They would like to focus efforts in keeping customers, but do not know
    if a customer is soon going to leave.

## Scope
- What data science solutions are we trying to build?
  - We will aim to build a binary classification model which identifies whether
    a customer will soon leave or stay.
- How is it going to be consumed by the customer?
  - This will not be consumed by the customer and will instead be an internal
    tool used to identify customers to focus efforts on.

## Metrics
- What are the qualitative objectives?
  - Identify whether a customer is soon going to stop doing business
- What is a quantifiable metric?
  - Have an accuracy greater than 90%
- Quantify what improvement in the values of the metrics are useful for the customer scenario
  - Having an accuracy of 75% or greater would be an improvement compared to random guessing.
- What is the baseline (current) value of the metric?
  - Current prediction accuracy is 50% (random guessing)
- How will we measure the metric?
  - Using training and testing data

## Plan
- Data Collection
- Data Cleaning/Exploration
- Modeling
  - Logistic Regression
  - KNN
  - Naive Bayes
  - Decision Trees
  - Random Forest
    - Bagging
    - Adaboost
    - Gradient Boosting
    - XGBoost
  - SVM
    - Linear
    - Radial
    - Polynomial
    - Sigmoid

## Architecture
- What data do we expect? Raw data in the customer data sources
  - Historical data showing customer status
- What tools and data storage/analytics resources will be used in the solution
  - Python for feature construction, aggregation, sampling, and modeling
- How will the client use the model results to make decisions
  - Client will use the model to identify which customers to focus on in terms of support and marketing
    efforts in order to keep the customer on board.

