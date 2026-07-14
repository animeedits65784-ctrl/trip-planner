import pandas as pd

df = pd.read_csv("housing.csv")
print(df.size)
print(df.shape)

print(df.head())
