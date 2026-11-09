import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("datasets/placement.csv")
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["placed"].value_counts())

df.hist(figsize=(10,6))
plt.tight_layout()
plt.savefig("Lab3/placement_histograms.png")
plt.show()
