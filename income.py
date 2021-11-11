def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

income_data = pd.read_csv('income.csv',header = 0,delimiter = ", ")
print(income_data.head())

# Format The Data For Scikit-learn
labels = income_data[["income"]]
