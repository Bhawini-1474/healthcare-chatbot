import pandas as pd

# Load the dataset
df = pd.read_csv('data\dataset.csv')

df.fillna('Unknown', inplace=True)
# Display the first few rows
print(df.head())


