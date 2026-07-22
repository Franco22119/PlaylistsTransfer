from concurrent.futures import ThreadPoolExecutor, as_completed

from clients.youtube_client import YouTubeClient
from domain.match import Match
from domain.track import Track


class TrackMatcher:
    def __init__(self, youtube_client: YouTubeClient, max_workers: int = 10):
        self._yt = youtube_client
        self._max_workers = max_workers

    def match_tracks(self, tracks: list[Track]) -> list[Match]:
        matches: list[Match | None] = [None] * len(tracks)
        with ThreadPoolExecutor(max_workers=self._max_workers) as pool:
            future_map = {
                pool.submit(self._search_single, idx, t): idx
                for idx, t in enumerate(tracks)
            }
            for future in as_completed(future_map):
                idx = future_map[future]
                matches[idx] = future.result()
        return matches

    def _search_single(self, idx: int, track: Track) -> Match:
        try:
            result = self._yt.search_track(track.title, track.artist)
            if result:
                video_id, video_title = result
                return Match(
                    source=track,
                    youtube_id=video_id,
                    youtube_title=video_title,
                    confidence=1.0,
                )
            return Match(
                source=track,
                youtube_id=None,
                youtube_title=None,
                confidence=0.0,
            )
        except Exception:
            return Match(
                source=track,
                youtube_id=None,
                youtube_title=None,
                confidence=0.0,
            )
