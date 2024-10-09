from datasets import Dataset, Features, Audio, Value, DatasetDict
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the Parquet file using pandas
df = pd.read_parquet('data/audio.parquet')

# Perform a train-test split
train_df, test_df = train_test_split(df, test_size=0.2)

# Convert pandas DataFrame to Hugging Face Dataset
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

# Define the features with the Audio column
features = Features({
    "audio": Audio(),
    "text": Value("string"),
    "audio_filepath": Value("string"), # optional
    "duration": Value("float32"), # optional
    "__index_level_0__": Value("int64") # optional
})

# Cast both train and test datasets with the correct features
train_dataset = train_dataset.cast(features)
test_dataset = test_dataset.cast(features)

# Create a DatasetDict to hold both train and test splits
dataset = DatasetDict({
    "train": train_dataset,
    "test": test_dataset
})

# Push the dataset to Hugging Face Dataset Hub
dataset.push_to_hub("pancake_dataset")