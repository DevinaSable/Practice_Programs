# make visual for years 1950 & 1960 from flights data

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

flight = pd.read_csv(r"C:\Users\DELL\Documents\flight.csv", encoding='latin1')

df = flight.head(12)

df = df.set_index(["month"])

sd = df.reindex(columns=['1950', '1960'])

db = sd.diff(axis=1)               #this gives % diff

sd.plot(kind='bar')
plt.show()
#print(sd)


