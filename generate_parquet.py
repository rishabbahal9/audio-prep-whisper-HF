import os
import pandas as pd
from openai import OpenAI
client = OpenAI()

# check if .wav file or not
def is_wav_file(filename):
    return filename.lower().endswith('.wav')

# Transcribe audio
# make sure environment variable OPENAI_API_KEY is set
def transcribe_audio(file_path):
    print(f"Transcribing {file_path}...")

    try:
        # Call the Whisper API for transcription
        with open(file_path, 'rb') as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",  # Specify the Whisper model
                file=audio_file,
                response_format="text"  # Adjust response format as needed
            )
            return response
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

# Function to read audio as bytes
def read_audio_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

# Example: List of audio files and transcripts
# data = [
#     {"audio": read_audio_file("audio/output_001.wav"), "audio_filepath": "audio/output_001.wav", "text": "Transcript for audio 1", "duration": 10.0},
#     {"audio": read_audio_file("audio/output_002.wav"), "audio_filepath": "audio/output_002.wav", "text": "Transcript for audio 2", "duration": 10.0},
# ]
data = []
# Traverse through the audio chunks
for dirpath, dirnames, filenames in os.walk("audio"):
    print(f'Current directory: {dirpath}')

    for filename in filenames:
        print(f'Found file: {filename}')
        if is_wav_file(filename):
            file_path = os.path.join(dirpath, filename)
            resp_text = transcribe_audio(file_path)
            data.append({"audio": read_audio_file(file_path), "text": resp_text, "audio_filepath": file_path, "duration": 10.0})

print("Transcription completed.")
print(data)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a Parquet file
df.to_parquet('data/audio.parquet')
