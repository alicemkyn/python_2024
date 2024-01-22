import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Spotify credentials
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''

# YouTube credentials
YOUTUBE_API_KEY = ''
YOUTUBE_PLAYLIST_ID = ''

# Spotify authentication
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

# YouTube authentication
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


# Get Spotify playlist
def get_spotify_playlist(username):
    playlists = sp.playlist(username)
    return playlists['items']


# Create an empty playlist on YouTube Music
def create_youtube_playlist(title):
    request_body = {
        'snippet': {
            'title': title,
            'description': 'Playlist created using Python script'
        }
    }

    try:
        playlist = youtube.playlists().insert(
            part='snippet',
            body=request_body
        ).execute()

        return playlist['id']

    except HttpError as e:
        print(f'An error occurred: {e}')
        return None


# Fetch Spotify playlist and create corresponding empty playlist on YouTube
# Music
def transfer_playlists(username):
    spotify_playlists = get_spotify_playlist(username)

    for playlist in spotify_playlists:
        spotify_playlist_name = playlist['name']
        youtube_playlist_id = create_youtube_playlist(spotify_playlist_name)

        if youtube_playlist_id:
            print(
                f'Playlist "{spotify_playlist_name}" transferred. YouTube ID :\
{youtube_playlist_id}')
        else:
            print(f'Failed to transfer playlist "{spotify_playlist_name}"')


# Replace 'your_spotify_username'with your actual username
transfer_playlists('your_spotify_username')
