import pandas as pd

# Read Parquet file
df = pd.read_parquet('data/audio.parquet')

# Display the DataFrame
print(df.head())