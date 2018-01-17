# 2018-01-17-morning

### The Setup
- Fork this repo
- Clone it
- Switch to `answers` branch
- Perform you work
- Add and Commit after finishing
- Push your `answers` branch to your repo on Github
- Send a pull request

### The Data
- `grad.csv` is in this repository

### The Problem
The data we will be using is admission data on Grad school acceptances.

* `admit`: whether or not the applicant was admitted to grad. school
* `gpa`: undergraduate GPA
* `gre`: score of GRE test
* `rank`: prestige of undergraduate school (1 is highest prestige, ala Harvard)

We will use the GPA, GRE, and rank of the applicants to try to predict whether or not they will be accepted into graduate school.

Before we get to predictions, we should do some data exploration.

1. Load in the dataset into pandas: `data/grad.csv`.

2. Use the pandas `describe` method to get some preliminary summary statistics on the data. In particular look at the mean values of the features.

3. Use the pandas `crosstab` method to see how many applicants from each rank of school were accepted. You should get a dataframe that looks like this:

    ```
    rank    1   2   3   4
    admit
    0      28  ..  ..  ..
    1      33  ..  ..  ..
    ```

    Make a bar plot of the percent of applicants from each rank who were accepted. You can do `.plot(kind="bar")` on a pandas dataframe.

4. What does the distribution of the GPA and GRE scores look like? Do the distributions differ much?

    Hint: Use the pandas `hist` method.

5. One of the issues with classification can be unbalanced classes. What percentage of the data was admitted? Do you think this will be a problem?

6. Perform a Logistic Regression. (Do you need to change the `rank` column?)
 
7. Use Cross Validation so the model doesn't overfit the data.

8. What's your accuracy?

9. What is better to have, a higher recall or precison in the context of admitting someone into graduate school. Whichever metric you choose, what is the value from your model?
