import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from itertools import combinations
from sklearn.model_selection import cross_val_score

df = pd.read_csv("grad.csv")

print(df.describe().T)

# No time to self-teach myself crosstbabing

# This was no help at all
scatter_matrix(df, figsize = (12, 12))
plt.show()

df.plot(kind = "bar")

dependent = "admit"

columns = [c for c in list(df) if c != dependent]
results = []
for i in range(1, len(columns) + 1):
    combos = list(combinations(columns, i))
    for c in combos:
        y = df[dependent]
        X = pd.DataFrame(df, columns = c) #Alternative assignment method
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
        for j in range(2):
            model = LogisticRegression(fit_intercept = False).fit(X_train, y_train)
            score = cross_val_score(model, X, y, cv = 10, scoring = "accuracy").mean()
            results.append([score, "Intercept: {}".format(j == 1), c, "Coef: {}".format(model.coef_), "Int: {}".format(model.intercept_)])

print(max(results))

# Best results for no Intercept == False
print(max([r for r in results if r[1] == "Intercept: False"]))

# Accuracy is .7023

# No preference over sensitivy/recall and
# precision.  Higher sensitivity, we're rejecting
# qualified appicants at a higher rate but,
# accepting fewer unqualified applicants.
