from clients.spotify_client import SpotifyClient
from clients.youtube_client import YouTubeClient
from domain.playlist import Playlist
from services.track_matcher import TrackMatcher


class PlaylistMigrator:
    def __init__(self, spotify: SpotifyClient, youtube: YouTubeClient):
        self._sp = spotify
        self._yt = youtube
        self._matcher = TrackMatcher(youtube)

    def migrate(self, playlist: Playlist):
        print(f"Migrando: {playlist.name} ({len(playlist.tracks)} tracks)")

        matches = self._matcher.match_tracks(playlist.tracks)
        matched = [m for m in matches if m.youtube_id]
        print(f"  Matches: {len(matched)}/{len(playlist.tracks)}")

        yt_id = self._yt.create_playlist(playlist.name, playlist.description)
        video_ids = [m.youtube_id for m in matched]
        self._yt.add_tracks(yt_id, video_ids)
        print(f"  Creada: https://music.youtube.com/playlist?list={yt_id}")
