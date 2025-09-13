import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("zomato.csv")
if 'rate (out of 5)' in df.columns:
    df['rate (out of 5)'] = df['rate (out of 5)'].astype(str).str.replace('/5', '').str.strip()
    df['rate (out of 5)'] = pd.to_numeric(df['rate (out of 5)'], errors = 'coerce')
cost_col = None 
for cand in ['avg cost (two people)', 'avg_cost(for two people)']:
    if cand in df.columns:
        cost_col = cand 
        break 
if cost_col:
    df[cost_col] = df[cost_col].astype(str).str.replace(',','').str.strip()
    df[cost_col] = pd.to_numeric(df[cost_col], errors = 'coerce')
if 'rate (out of 5)' in df.columns:
    df['rate (out of 5)'].fillna(df['rate (out of 5)'].median(), inplace = True)
if cost_col:
    df[cost_col].fillna(df[cost_col].median(), inplace = True)
print("\n=== ONLINE ORDER counts and percent ===")
if 'online_order' in df.columns:
    oc = df['online_order'].value_counts(dropna = False)
    print(oc)
    print("\npercent:\n", round(100*oc/len(df),2))
else:
    print("Column 'online_order' not found.")
print("\n=== TABLE BOOKING counts and percent ===")
if 'table booking' in df.columns:
    tb = df['table booking'].value_counts(dropna = False)
    print(tb)
    print("\nPercent:\n", round(100*tb/len(df),2))
else:
    print("Column 'table booking' not found.")
print("\n=== Average rating by online_order (mean) ===")
if 'restaurant type' in df.columns:
    top_types = df['restaurant type'].value_counts().head(10)
    print(top_types)
else:
    print("Column 'restaurant type' not found.")
print("\n=== Top 10 cuisines (first listed cuisine) ===")
if 'cuisines type' in df.columns:
    first_cuisine = df['cuisines type'].dropna().astype(str).apply(lambda x:x.split(',')[0].strip())
    top_cuisines = first_cuisine.value_counts().head(10)
    print(top_cuisines)
else:
    print("Column 'cuisines type' not found.")
fig, axes = plt.subplots(2,2, figsize=(16,10))
if 'online_order' in df.columns:
    oc_plot = df['online_order'].value_counts()
    oc_plot.plot(kind = 'bar', ax = axes[0,0], color = ['#4c72b0', '#55a868'])
    axes[0,0].set_title("Online Order vs Offline")
    axes[0,0].set_ylabel("Count")
else:
    axes[0,0].text(0.5, 0.5, "online_order missing", ha='center')
if 'table booking' in df.columns:
    tb_plot = df['table booking'].value_counts()
    tb_plot.plot(kind = 'bar', ax = axes[0,1], color = ['#c44e52', '#8172b3'])
    axes[0,1].set_title("Table Booking Availability")
    axes[0,1].set_ylabel("Count")
else:
    axes[0,1].text(0.5,0.5, "table booking missing", ha = 'center')
if cost_col and 'rate (out of 5)' in df.columns:
    axes[1,0].scatter(df[cost_col], df['rate (out of 5)'], alpha = 0.4)
    axes[1,0].set_xlabel(cost_col)
    axes[1,0].set_ylabel("Rating")
    axes[1,0].set_title("Average cost (for two) vs Rating")
else:
    axes[1,0].text(0.5, 0.5, "cost or rating missing", ha='center')
if 'cuisines type' in df.columns:
    top_cuisines.plot(kind = 'barh', ax = axes[1,1], color = '#8c8c8c')
    axes[1,1].set_title("Top 10 Cuisines (first listed)")
    axes[1,1].text(0.5, 0.5, "cuisines type missing", ha='center')
plt.tight_layout()
plt.show()
fig.savefig("eda_insights.png", dpi=150)
print("\nSaved combined figure as eda_insights.png")