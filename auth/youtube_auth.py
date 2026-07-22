import os
from ytmusicapi import YTMusic, setup

YT_HEADERS_PATH = "storage/youtube_headers.json"


def get_youtube_client() -> YTMusic:
    if not os.path.exists(YT_HEADERS_PATH):
        print("=== Configuracion inicial de YouTube Music ===")
        setup(filepath=YT_HEADERS_PATH)

    return YTMusic(YT_HEADERS_PATH)
