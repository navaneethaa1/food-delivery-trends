import pandas as pd
df = pd.read_csv("zomato.csv", encoding="latin-1")
print(df.head())
print(df.info())
print(df.isnull().sum())