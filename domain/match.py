from dataclasses import dataclass
from domain.track import Track


@dataclass
class Match:
    source: Track
    youtube_id: str | None
    youtube_title: str | None
    confidence: float
