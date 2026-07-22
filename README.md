# PlaylistsTransfer

Migrar tus playlists de Spotify a YouTube Music.

## Setup

```bash
pip install -r requirements.txt
cp .env   # Completar con tus credenciales
```

## APIs

- Spotify Web API (OAuth)
- YouTube Data API v3 (OAuth)

## Archivos sensibles (no commiteados)

- `.env` — Client ID/Secret de ambas APIs
- `storage/.spotify_cache` — Token de Spotify
- `storage/.youtube_token.pickle` — Token de YouTube
