import csv 
import pandas as pd 
df = pd.read_csv("total_stars.csv")
print(df.shape)
del df["luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Unamed: 0"]
del df["Unamed: 6"]
print(df.shape)
df.to_csv("all_stars.csv")