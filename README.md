# Spotify to YouTube Downloader

This is a Python script that allows you to download audio tracks from a Spotify playlist and fetches the corresponding YouTube videos to convert them into MP3 format.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- A Spotify developer account to get the Spotify client credentials.
- A Google Cloud project with the YouTube Data API enabled to get the YouTube API key.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/spotify-youtube-downloader.git
   cd spotify-youtube-downloader
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install spotipy google-api-python-client pytube
   ```

### Configuration

Before running the script, you need to configure the necessary credentials and playlist URI.

1. **Spotify Credentials**

   - Create a Spotify developer account at https://developer.spotify.com/.
   - Obtain the Client ID and Client Secret from the Spotify dashboard.
   - Replace `'YOUR_SPOTIFY_CLIENT_ID'` and `'YOUR_SPOTIFY_CLIENT_SECRET'` in the script with your actual credentials.

2. **YouTube API Key**

   - Go to the Google Cloud Console at https://console.cloud.google.com/.
   - Create a new project (if you don't have one) and enable the YouTube Data API for the project.
   - Create credentials for the API and get the API key.
   - Replace `'YOUR_YOUTUBE_API_KEY'` in the script with your actual API key.

3. **Spotify Playlist URI**

   - Open the Spotify app or web player and navigate to the playlist you want to download.
   - Click on the three dots (...) next to the playlist name, then choose "Share" > "Copy Playlist Link."
   - Replace `'YOUR_SPOTIFY_PLAYLIST_ID/URL'` in the script with the copied playlist link.

4. **Path to Folder**
   - Create a folder, this is where the mp3 music files are going to be downloaded
   - copy the path to that folder and paste it into the "PATH_FOLDER"
     
     ```audio_stream.download(r"PATH_FOLDER", filename=song_name + ".mp3") #CHANGE PATH FOLDER TO WHERE YOU WANT THE MP3 MUSIC FILES TO BE SAVED```

### Running the Script

Once you have completed the configuration steps, you are ready to run the script.

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the script using Python:

   ```bash
   python spotify_youtube_downloader.py
   ```

The script will start processing the tracks in the Spotify playlist, searching for corresponding YouTube videos, and downloading the audio for each song. The MP3 files will be saved in the specified folder.

### Note

- If a video cannot be found on YouTube for a particular track or if an audio stream is unavailable, the script will skip the track and continue with the next one.
- Ensure that you have a stable internet connection while running the script.
- Make sure that playlist is around 50-75 songs because anything more than that will cause for the YouTube API to go out of quota (meaning that you reached the free cap). If you have larger playlist, break it down into smaller chunks (playlists) and run one of the chunks everyday and save them to the same folder. Once you finish downloading all of the chunks, all of the music will be found in the same folder, meaning that you basically downloaded the whole playlist.

