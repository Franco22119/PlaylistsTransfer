import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.credentials import Credentials
from google.auth.transport.requests import Request
import pickle

from config.settings import YT_CLIENT_ID, YT_CLIENT_SECRET

YT_SCOPES = ["https://www.googleapis.com/auth/youtube"]
YT_TOKEN_PATH = "storage/.youtube_token.pickle"


def get_youtube_credentials() -> Credentials:
    creds = None

    if os.path.exists(YT_TOKEN_PATH):
        with open(YT_TOKEN_PATH, "rb") as f:
            creds = pickle.load(f)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(YT_TOKEN_PATH, "wb") as f:
            pickle.dump(creds, f)
        return creds

    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": YT_CLIENT_ID,
                "client_secret": YT_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["http://localhost"],
            }
        },
        scopes=YT_SCOPES,
    )
    creds = flow.run_local_server(open_browser=True)

    with open(YT_TOKEN_PATH, "wb") as f:
        pickle.dump(creds, f)

    return creds
