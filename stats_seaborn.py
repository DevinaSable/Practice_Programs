import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

flights = pd.read_csv('https://github.com/mwaskom/seaborn-data/blob/master/flights.csv')
flights.head(10)
a = sns.load_dataset("flights")

sns.relplot(x="passenger", y="month", data=a)
sns.plt.show()