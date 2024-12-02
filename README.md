# Video-Subtitle-Generator
Video Subtitle Generator with Whisper and FFmpeg This project is a video subtitle generator built using Streamlit, Whisper, and FFmpeg. It extracts audio from a video, transcribes the audio using Whisper, generates subtitles in .srt format, and adds them back to the original video. It supports both soft and hard subtitles.

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

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/video-subtitle-generator.git
cd video-subtitle-generator


