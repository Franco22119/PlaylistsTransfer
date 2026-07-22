import spotipy

from domain.playlist import Playlist
from domain.track import Track


class SpotifyClient:
    def __init__(self, sp: spotipy.Spotify):
        self._sp = sp

    def get_user_playlists(self) -> list[Playlist]:
        results = self._sp.current_user_playlists()
        playlists = []
        for item in results.get("items", []):
            try:
                tracks = self._get_tracks(item["id"])
                playlists.append(
                    Playlist(
                        id=item["id"],
                        name=item["name"],
                        description=item.get("description", ""),
                        owner=item["owner"]["id"],
                        tracks=tracks,
                    )
                )
            except spotipy.SpotifyException:
                continue
        return playlists

    def _get_tracks(self, playlist_id: str) -> list[Track]:
        tracks = []
        offset = 0
        while True:
            results = self._sp.playlist_items(playlist_id, offset=offset)
            for item in results.get("items", []):
                t = item.get("track") or item.get("item")
                if not t:
                    continue
                tracks.append(
                    Track(
                        id=t["id"],
                        title=t["name"],
                        artist=t["artists"][0]["name"],
                        album=t["album"]["name"],
                        duration_ms=t["duration_ms"],
                    )
                )
            if not results.get("next"):
                break
            offset += len(results["items"])
        return tracks
