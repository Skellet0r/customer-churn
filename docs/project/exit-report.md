# Exit Report of Project 'Customer Churn Classification' for Customer SyriaTel

Customer: SyriaTel

Team Members: Edward Amor

##	Overview

To identify customers who will soon stop doing business with SyriaTel, a classification model was generated. The generated model has an accuracy of over 90% in tests, and
utilizes many decision trees (a series of if-else branches) which vote on whether a customer will soon leave.

##	Business Domain

Our client is in the telecommunications industry, and as such provides phone service plans to customers. Our client offers PAYG (Pay As You Go) or pre-paid plans to customers,
in which the customer pays for their minutes at a pre-defined rate.

##	Business Problem

Our client currently is seeing a sizeable portion of their clients ending their service plan and switching to a new service provider. The bottom line is
our client is seeing profits diminish over time as their clients are consistently leaving, and they have no way of identifying accurately whether a client will soon
stop their service plan.

##	Data Processing

Original Dataset Schema:

- state
- account length
- area code
- phone number
- international plan
- voice mail plan
- number vmail messages
- total day minutes
- total day calls
- total day charge
- total eve minutes
- total eve calls
- total eve charge
- total night minutes
- total night calls
- total night charge
- total intl minutes
- total intl calls
- total intl charge
- customer service calls
- churn

Processing of the data involved encoding the state feature into multiple columns, dropping the phone number column, binarizing the international plan & voice mail plan features,
and then scaling the data into a z score.

## Modeling, Validation

Validating our model started first by separating 25% of our processed data as a final testing set, our data was randomly split and stratified to make sure 
class sizes maintained the same. Throughout the modeling phase, 10 fold stratified cross validation was implemented during training to verify metrics.

## Benefits

###	Client Benefits

Exact savings are not available but based on testing we can see that there is a consistent accuracy of over 90%. Our model in testing shows that it can identify approx. 80%
of customers who will soon end their service plan with SyriaTel.

## Learnings

### Data science / Engineering

- Pickling models after long running processes allows you to continue them in a new notebook. Reduces the amount of time required to restart and run all cells in a notebook.
- Having an environment.yml allows you to use services like nbviewer and binder.

###	What's unique about this project, specific challenges

One issue was identifying which metric to focus on and optimize, if you focus solely on recall, your precision will fall, and if you focus on precision recall suffers.
Depending on which metric you choose your decision threshold changes. Using metrics like AUC and F Measure, it's easier to compare models and also tune them in a more
holistic way.

Another issue was run time of modeling, some methods of optimizing models such as GridSearchCV, which is an exhaustive search of a parameter space can take a very long time
if one doesn't smartly choose a good parameter space. It's also very important to split up work into separate notebooks so that the cost of running a notebook isn't as great.

##	Next Steps
 
 Next steps for this project include:

 - Removing correlated features and analyzing the effect on models
 - Further reducing the feature set
 - Analyzing the baseline performance of different classifiers with a smaller feature set.
 - Exploring more hyper parameters

