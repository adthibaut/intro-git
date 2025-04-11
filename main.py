import pandas as pd

df = pd.read_csv(
    "input_file.csv", 
    sep=",",
)

print(df.head())
