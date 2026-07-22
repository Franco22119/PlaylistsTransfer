import time
from googleapiclient.discovery import build
from google.auth.credentials import Credentials
from googleapiclient.errors import HttpError


class YouTubeClient:
    def __init__(self, credentials: Credentials):
        self._yt = build("youtube", "v3", credentials=credentials)

    def search_track(self, title: str, artist: str) -> tuple[str, str] | None:
        query = f"{title} {artist}"
        request = self._yt.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=1,
        )
        response = request.execute()
        items = response.get("items", [])
        if items:
            return (
                items[0]["id"]["videoId"],
                items[0]["snippet"]["title"],
            )
        return None

    def create_playlist(self, name: str, description: str) -> str:
        request = self._yt.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": name,
                    "description": description,
                },
                "status": {"privacyStatus": "public"},
            },
        )
        response = request.execute()
        return response["id"]

    def add_tracks(self, playlist_id: str, video_ids: list[str]):
        for i, video_id in enumerate(video_ids):
            self._insert_with_retry(playlist_id, video_id)
            if i < len(video_ids) - 1:
                time.sleep(0.5)

    def _insert_with_retry(self, playlist_id: str, video_id: str, retries: int = 3):
        for attempt in range(retries):
            try:
                self._yt.playlistItems().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": playlist_id,
                            "resourceId": {
                                "kind": "youtube#video",
                                "videoId": video_id,
                            },
                        }
                    },
                ).execute()
                return
            except HttpError as e:
                if e.resp.status in (409, 503) and attempt < retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise
