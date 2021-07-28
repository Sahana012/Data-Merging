import pandas as pd

df = pd.read_csv("dwarf_stars.csv")
print(df.head())

df["Radius"] = 0.102763*df["Radius"]

df.to_csv("unit_converted_stars.csv")