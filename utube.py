import streamlit as st
from pytubefix import YouTube
import requests
from bs4 import BeautifulSoup
import os
# Function to get video metadata
def scrape_youtube_video_details(video_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    try:
        response = requests.get(video_url, headers=headers)
        if response.status_code != 200:
            st.error(f"Failed to retrieve video page. Status code: {response.status_code}, Content: {response.text}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find("meta", property="og:title")
        description_tag = soup.find("meta", property="og:description")
        thumbnail_tag = soup.find("meta", property="og:image")

        return {
            "title": title_tag["content"] if title_tag else "N/A",
            "description": description_tag["content"] if description_tag else "N/A",
            "thumbnail": thumbnail_tag["content"] if thumbnail_tag else ""
        }
    except Exception as e:
        return {"error": str(e)}

def download_youtube_video(video_url):
    try:
        yt = YouTube(video_url)
        
        # Get highest resolution video-only stream
        video_stream = yt.streams.filter(file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        if not video_stream or not audio_stream:
            return "❌ Video or audio stream not found."

        video_file = video_stream.download(output_path="downloads/", filename_prefix="video_")
        audio_file = audio_stream.download(output_path="downloads/", filename_prefix="audio_")

        # Prepare output filename
        sanitized_title = "".join(c for c in yt.title if c.isalnum() or c in (' ', '.', '_')).rstrip()
        combined_file = f"downloads/{sanitized_title}_combined.mp4"

        # Combine using ffmpeg
        command = f"ffmpeg -y -i \"{video_file}\" -i \"{audio_file}\" -c:v copy -c:a aac \"{combined_file}\""
        os.system(command)

        # Cleanup
        os.remove(video_file)
        os.remove(audio_file)

        return combined_file

    except Exception as e:
        return f"❌ Error: {str(e)}"


# Streamlit App
st.set_page_config(page_title="YouTube Scraper & Downloader", layout="centered")
st.title("📽️ YouTube Scraper + Downloader (No API)")

# Add some styling
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        background-color: #f0f4f8;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #4169E1;
    }
    .stAlert {
        border-radius: 10px;
    }
    .stImage {
        border-radius: 10px;
        border: 5px solid #d3d3d3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

url = st.text_input("Enter YouTube Video URL")

col1, col2 = st.columns([2, 1])

with col1:
    if st.button("Scrape Video Info"):
        if "youtube.com/watch?v=" not in url:
            st.error("❌ Invalid YouTube URL.")
        else:
            st.info("🔍 Scraping video details...")
            video_data = scrape_youtube_video_details(url)

            if "error" in video_data:
                st.error(f"❌ {video_data['error']}")
            else:
                st.subheader("🎬 Video Title")
                st.write(video_data['title'])

                st.subheader("📝 Video Description")
                st.write(video_data['description'])

                if video_data['thumbnail']:
                    st.image(video_data['thumbnail'], caption="Video Thumbnail", width=400)

with col2:
    if st.button("Download Video"):
        if "youtube.com/watch?v=" not in url:
            st.error("❌ Invalid YouTube URL.")
        else:
            st.info("⬇️ Downloading video...")
            result = download_youtube_video(url)
            if "downloads/" in result:
                st.success("✅ Video downloaded successfully!")
                st.write(f"📂 File path: {result}")
            else:
                st.error(f"❌ Download failed: {result}")