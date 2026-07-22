from dataclasses import dataclass, field
from domain.track import Track


@dataclass
class Playlist:
    id: str
    name: str
    description: str
    owner: str
    tracks: list[Track] = field(default_factory=list)
