import pandas as pd 
from src.csv_reader import read_csv

df = pd.DataFrame(read_csv("input/Statements.csv"))
print(df.to_string())

