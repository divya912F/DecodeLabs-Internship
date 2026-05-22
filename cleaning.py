import pandas as pd
df = pd.read_excel("dataset.xlsx")

print(df.isnull().sum())

df = df.drop_duplicates()

for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].fillna("Unknown")
    else:
        df[column] = df[column].fillna(df[column].mean())

df.to_csv("cleaned_dataset.csv", index=False)

print("Dataset cleaned successfully!")