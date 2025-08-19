from youtube_transcript_api import YouTubeTranscriptApi

# video_id = "youtube link id -  C2sNXuudTI7A"
video_id = "C2sNXuudTI7A"

try:
    # Fetch Hindi transcript (manual or auto-generated)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi', 'hi-en']  )
    text = " ".join([entry['text'] for entry in transcript])
    print(text)
except Exception as e:
    print(f"Error: {e}")

