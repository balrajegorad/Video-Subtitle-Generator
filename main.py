import os
import math
import streamlit as st
import ffmpeg
from faster_whisper import WhisperModel

# Function to extract audio from video
def extract_audio(input_video, input_video_name):
    extracted_audio = f"audio-{input_video_name}.wav"
    stream = ffmpeg.input(input_video)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

# Function to transcribe audio
def transcribe(audio):
    model = WhisperModel("small", device="cpu")  # Change to "large" for better accuracy if needed
    segments, info = model.transcribe(audio)
    language = info[0]
    segments = list(segments)
    return language, segments

# Function to format time
def format_time(seconds):
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
    return formatted_time

# Function to generate subtitle file
def generate_subtitle_file(language, segments, input_video_name):
    subtitle_file = f"sub-{input_video_name}.{language}.srt"
    text = ""
    for index, segment in enumerate(segments):
        segment_start = format_time(segment.start)
        segment_end = format_time(segment.end)
        text += f"{str(index+1)} \n"
        text += f"{segment_start} --> {segment_end} \n"
        text += f"{segment.text} \n"
        text += "\n"
        
    with open(subtitle_file, "w") as f:
        f.write(text)

    return subtitle_file

def add_subtitle_to_video(input_video, subtitle_file, subtitle_language, input_video_name, soft_subtitle=True):
    video_input_stream = ffmpeg.input(input_video)
    output_video = f"uploads/output-{input_video_name}.mp4"
    
    try:
        # Soft subtitles - Using the mov_text codec
        if soft_subtitle:
            # Remove 'c="copy"' as it conflicts with the filter
            stream = ffmpeg.output(
                video_input_stream, output_video, vf=f"subtitles={subtitle_file}",
                **{"c:s": "mov_text"}, metadata=f"language={subtitle_language}"
            )
            ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)
        else:
            # Hard subtitles - Burn the subtitles onto the video
            stream = ffmpeg.output(video_input_stream, output_video, vf=f"subtitles={subtitle_file}")
            ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)
        
        return output_video

    except ffmpeg.Error as e:
        error_message = e.stderr.decode() if e.stderr else e.stdout.decode() if e.stdout else "No output"
        st.error(f"Error during ffmpeg processing: {error_message}")
        return None

    except ffmpeg.Error as e:
        # Check if e.stderr is None before calling decode()
        error_message = e.stderr.decode() if e.stderr else e.stdout.decode() if e.stdout else "No output"
        st.error(f"Error during ffmpeg processing: {error_message}")
        return None

# Streamlit UI and logic
def run():
    st.title("Video Subtitle Generator")
    
    # Upload video
    uploaded_video = st.file_uploader("Choose a video", type=["mp4"])
    
    if uploaded_video is not None:
        input_video_name = uploaded_video.name.replace(".mp4", "")
        input_video_path = os.path.join("uploads", uploaded_video.name)
        
        # Save uploaded video to local directory
        with open(input_video_path, "wb") as f:
            f.write(uploaded_video.getbuffer())

        # Display message that video is being processed
        st.write("Processing video...")

        # Use a spinner to show that processing is ongoing
        with st.spinner("Extracting audio and transcribing..."):
            # Step 1: Extract audio
            extracted_audio = extract_audio(input_video_path, input_video_name)

            # Step 2: Transcribe audio
            language, segments = transcribe(extracted_audio)

            # Step 3: Generate subtitle file
            subtitle_file = generate_subtitle_file(language, segments, input_video_name)

            # Step 4: Add subtitles to video
            output_video = add_subtitle_to_video(input_video_path, subtitle_file, language, input_video_name)

            # Log output video path
            if output_video:
                st.write(f"Subtitled video saved at: {output_video}")

                # Check if file exists
                if os.path.exists(output_video):
                    st.write("Subtitled Video:")
                    st.video(output_video)
                else:
                    st.write("Error: Subtitled video not found. Please try again.")
            else:
                st.write("Error occurred during video processing.")

# Run the Streamlit app
if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    run()
