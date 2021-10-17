import pandas as pd

flights = pd.read_csv(r"C:\Users\DELL\Documents\flights.csv", encoding='latin1')

flights.to_html("planes.html")