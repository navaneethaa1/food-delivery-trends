import pandas as pd
df = pd.read_csv("zomato.csv")
print(df.columns.tolist())
df['rate (out of 5)'] = df['rate (out of 5)'].astype(str).str.replace('/5', '').str.strip()
df['rate (out of 5)'] = pd.to_numeric(df['rate (out of 5)'], errors = 'coerce')
df['rate (out of 5)'].fillna(df['rate (out of 5)'].median(),inplace=True)
df['avg cost (two people)'] = pd.to_numeric(df['avg cost (two people)'].astype(str).str.replace(',',''), errors = 'coerce')
df['avg cost (two people)'].fillna(df['avg cost (two people)'].median(),inplace=True)
print(df.isnull().sum())