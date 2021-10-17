import pandas as pd

abc_web = {'Day': [1,2,3,4,5,6], "visitors":[1000, 2000, 5000, 3000, 2000, 4500], "Bounce_rate":[20, 30, 25, 45, 30, 20]}

df = pd.DataFrame(abc_web)   #converting dict to pd dataframe

#print(df)

# slicing dataframe
print(df.head(2))
print(df.tail(2))
