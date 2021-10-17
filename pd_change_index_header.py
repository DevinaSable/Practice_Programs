import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

df = pd.DataFrame({'Day': [1,2,3,4,5,6],
                    "visitors":[1000, 2000, 5000, 3000, 2000, 4500],
                    "Bounce_rate":[20, 30, 25, 45, 30, 20]})

#df.set_index("Day", inplace=True)         #changes index to given header


#df.plot()
#plt.show()

#changing header

df = df.rename(columns={"visitors":"Users"})
print(df)
