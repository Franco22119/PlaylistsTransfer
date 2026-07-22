# PlaylistsTransfer

Migra tus playlists de Spotify a YouTube Music.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # Completar con tus credenciales
```

## Uso

```bash
# Exportar playlists de Spotify
python -c "from auth.spotify_auth import get_spotify_client
from clients.spotify_client import SpotifyClient
sp = get_spotify_client()
for p in SpotifyClient(sp).get_user_playlists():
    print(f'{p.name} ({len(p.tracks)} canciones)')"

# Buscar un track en YouTube
python -c "from auth.youtube_auth import get_youtube_credentials
from clients.youtube_client import YouTubeClient
yt = YouTubeClient(get_youtube_credentials())
print(yt.search_track('Diamante Roto', 'El Mató a un Policía Motorizado'))"
```

## APIs

- Spotify Web API (OAuth)
- YouTube Data API v3 (OAuth)

## Archivos sensibles (no commiteados)

- `.env` — Client ID/Secret de ambas APIs
- `storage/.spotify_cache` — Token de Spotify
- `storage/.youtube_token.pickle` — Token de YouTube
