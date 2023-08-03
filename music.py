# import required libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
from pytube import YouTube
import os

# set configurations
SPOTIFY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback' #YOU CAN KEEP THIS WEBSITE
SPOTIFY_PLAYLIST_URI = 'YOUR_SPOTIFY_PLAYLIST_ID/URL'
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'

# set up spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="playlist-read-private"))

# get playlist
results = sp.playlist(SPOTIFY_PLAYLIST_URI)

# set the developer key and the service name and version
DEVELOPER_KEY = YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# build the youtube service
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Loop through the tracks and download the audio for each song
for item in results['tracks']['items']:
    song_name = item['track']['name']

    # search for the song on YouTube
    try:
        search_response = youtube.search().list(
            q=song_name,
            part="id,snippet",
            maxResults=1
        ).execute()

        videos = []

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append('%s (%s)' % (search_result["snippet"]["title"],
                                           search_result["id"]["videoId"]))

        if not videos:
            print(f"Video not found for '{song_name}'. Skipping...")
            continue

        # get the youtube url
        youtube_url = 'https://www.youtube.com/watch?v=' + search_response["items"][0]["id"]["videoId"]

        # download the video as audio
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if not audio_stream:
            print(f"Could not find audio stream for '{song_name}'. Skipping...")
            continue

        audio_stream.download(r"PATH_FOLDER", filename=song_name + ".mp3") #CHANGE PATH FOLDER TO WHERE YOU WANT THE MP3 MUSIC FILES TO BE SAVED

        print(f"{song_name} - Download complete!")

    except Exception as e:
        print(f"Error occurred while processing '{song_name}': {e}")

print('All songs download complete!')
