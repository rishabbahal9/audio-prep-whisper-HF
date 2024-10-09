import pandas as pd
import json



# Function to read audio as bytes
def read_audio_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

# Reading data.json
# Make sure you have corrected the transcripts if required in data.json
with open('data.json', 'r') as f:
    data = json.load(f)

# converting audio to bytes
for d in data:
    d['audio'] = read_audio_file(d['audio'])

print(data)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a Parquet file
df.to_parquet('data/audio.parquet')
