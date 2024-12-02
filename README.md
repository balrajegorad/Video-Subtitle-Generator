# Video Subtitle Generator with Whisper and FFmpeg

This project is a video subtitle generator built using [Streamlit](https://streamlit.io/), [Whisper](https://github.com/openai/whisper), and [FFmpeg](https://ffmpeg.org/). It extracts audio from a video, transcribes the audio using Whisper, generates subtitles in `.srt` format, and adds them back to the original video. It supports both soft and hard subtitles.

---

## Features

- **Audio Extraction**: Extracts audio from video files (supports `.mp4` format).
- **Transcription**: Uses the Whisper model to transcribe the extracted audio into text.
- **Subtitle Generation**: Creates `.srt` subtitle files with timestamps for the transcribed text.
- **Subtitle Embedding**: Adds the generated subtitles to the video either as soft subtitles (text tracks) or hard subtitles (burned into the video).
- **Streamlit Interface**: Easy-to-use web interface for uploading videos and downloading the processed video with subtitles.

---

## Requirements

This project requires several dependencies. Below are the steps to install them:

## 1. Clone the Repository

```bash
https://github.com/balrajegorad/Video-Subtitle-Generator.git
cd Video-Subtitle-Generator
```

## 2. Install Python Dependencies
Create a virtual environment :

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install the required Python packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```
## 3. Install FFmpeg
This project uses FFmpeg for video processing. Ensure FFmpeg is installed and available in your system’s PATH.

macOS (Homebrew):

```bash
brew install ffmpeg
```
Ubuntu:
```bash
sudo apt update
sudo apt install ffmpeg
```
Windows:

Download FFmpeg from [here](https://ffmpeg.org/download.html) and follow the instructions to add it to your PATH.

## 4. Install Whisper Model Dependencies
The project uses the faster-whisper library to handle audio transcription. Install it by running:

```bash
pip install faster-whisper==1.0.3
```
###Running the Application
Once you’ve installed all dependencies, you can run the Streamlit app by following these steps:

1. Start the Streamlit app with the command:

```bash
streamlit run main.py
```
2. Open your browser and go to the URL provided in the terminal (usually http://localhost:8501).

3. The Streamlit interface will allow you to upload a .mp4 video file. The app will process the video by:

Extracting the audio.
Transcribing the audio to text using Whisper.
Generating subtitles in .srt format.
Adding the subtitles back to the video (either soft or hard subtitles).
After processing, you’ll be able to download the subtitled video or view it directly in the browser.

4. After processing, you’ll be able to download the subtitled video or view it directly in the browser.
