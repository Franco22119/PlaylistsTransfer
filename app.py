from auth.spotify_auth import get_spotify_client
from auth.youtube_auth import get_youtube_credentials
from clients.spotify_client import SpotifyClient
from clients.youtube_client import YouTubeClient
from services.playlist_migrator import PlaylistMigrator


def main():
    sp = get_spotify_client()
    yt = YouTubeClient(get_youtube_credentials())

    spotify = SpotifyClient(sp)
    migrator = PlaylistMigrator(spotify, yt)

    playlists = spotify.get_user_playlists()
    disponibles = [p for p in playlists if p.tracks]

    if not disponibles:
        print("No hay playlists con tracks para migrar.")
        return

    print("Playlists disponibles:")
    for i, p in enumerate(disponibles, 1):
        print(f"  {i}. {p.name} ({len(p.tracks)} tracks)")

    eleccion = input("\nNúmero de la playlist a migrar (o 't' para migrar todas): ").strip()
    if eleccion.lower() == "t":
        for p in disponibles:
            migrator.migrate(p)
    else:
        try:
            idx = int(eleccion) - 1
            migrator.migrate(disponibles[idx])
        except (ValueError, IndexError):
            print("Opción inválida.")


if __name__ == "__main__":
    main()
