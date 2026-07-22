from ytmusicapi import YTMusic


class YouTubeClient:
    def __init__(self, yt: YTMusic):
        self._yt = yt

    def search_track(self, title: str, artist: str) -> tuple[str, str] | None:
        query = f"{title} {artist}"
        results = self._yt.search(query, filter="songs", limit=1)
        if results:
            video_id = results[0].get("videoId")
            video_title = results[0].get("title", "")
            if video_id:
                return (video_id, video_title)
        return None

    def create_playlist(self, name: str, description: str) -> str:
        return self._yt.create_playlist(name, description)

    def add_tracks(self, playlist_id: str, video_ids: list[str]):
        self._yt.add_playlist_items(playlist_id, video_ids)
