import pandas as pd
df = pd.read_csv("zomato.csv")
print("dataset loaded successfully!")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())