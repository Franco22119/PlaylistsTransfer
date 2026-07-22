from googleapiclient.discovery import build
from google.auth.credentials import Credentials


class YouTubeClient:
    def __init__(self, credentials: Credentials):
        self._yt = build("youtube", "v3", credentials=credentials)

    def search_track(self, title: str, artist: str) -> str | None:
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
            return items[0]["id"]["videoId"]
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
        for video_id in video_ids:
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
