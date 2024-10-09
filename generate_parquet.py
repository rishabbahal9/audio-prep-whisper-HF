import pandas as pd


# Function to read audio as bytes
def read_audio_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

# Example: List of audio files and transcripts
data = [
    {"audio": read_audio_file("audio/output_001.wav"), "audio_filepath": "audio/output_001.wav", "text": "Transcript for audio 1", "duration": 30.0},
    {"audio": read_audio_file("audio/output_002.wav"), "audio_filepath": "audio/output_002.wav", "text": "Transcript for audio 2", "duration": 30.0},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a Parquet file
df.to_parquet('data/audio.parquet')
