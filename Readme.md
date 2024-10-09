# Preparing data for whisper training & HF's audio datasets

## Introduction
This repository will help you prepare audio chunks with transcripts in parquet format that can be used to fine tune 
whisper model by open ai.

## Instructions
### Step 1: Clone the repository
```bash
git clone <repository_link>
```

### Step 2: Install the required packages
```bash
pip install -r requirements.txt
```

### Step 3: Download the video
Download the video you want to extract audio from in mp4 format. I use yt1d.com to download youtube videos.

### Step 4: Extract audio from the video in .wav format
```bash
ffmpeg -i video.mp4 -q:a 0 -map a audio.wav
```
### Step 5: Make sure audio is in the right format (mono-channel, 16 kHz)
```bash
ffmpeg -i audio.wav -ac 1 -ar 16000 audio_16khz.wav
```

### Step 6: Split the audio into chunks
By default, I am doing 30 seconds chunks. You can change the duration by changing the value of "segment_time" in the command below.
```bash
mkdir audio # create "audio" directory
ffmpeg -i audio_16khz.wav -f segment -segment_time 30 -c copy audio/output_%03d.wav
```
