import spotipy
from spotipy.oauth2 import SpotifyOAuth

from config.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SPOTIFY_SCOPES


def get_spotify_client() -> spotipy.Spotify:
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=" ".join(SPOTIFY_SCOPES),
        cache_path="storage/.spotify_cache",
        open_browser=True,
    )
    return spotipy.Spotify(auth_manager=auth_manager)
