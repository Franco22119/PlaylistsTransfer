import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:8888/callback"
SPOTIFY_SCOPES = [
    "playlist-read-private",
    "playlist-read-collaborative",
]
SPOTIFY_API_BASE = "https://api.spotify.com/v1"

YT_CLIENT_ID = os.getenv("YT_CLIENT_ID", "")
YT_CLIENT_SECRET = os.getenv("YT_CLIENT_SECRET", "")

DEFAULT_MAX_WORKERS = 10
REQUEST_TIMEOUT = 30
BATCH_SIZE = 50
