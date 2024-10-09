from datasets import Dataset, Features, Audio, Value
import pandas as pd

# Load the Parquet file using pandas
df = pd.read_parquet('data/audio.parquet')

# Convert pandas DataFrame to Hugging Face Dataset
dataset = Dataset.from_pandas(df)

# Define the features with the Audio column
features = Features({
    "audio": Audio(),
    "text": Value("string"),
    "audio_filepath": Value("string"), # optional
    "duration": Value("float32") # optional
})

# Load dataset with audio column properly mapped
dataset = dataset.cast(features)

# Test one example to ensure it's correctly loaded
print(dataset[0]["audio_filepath"])  # This will show the audio file details

# Push the dataset to Hugging Face Dataset Hub
dataset.push_to_hub("firstpost_dataset")