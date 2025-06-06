# main.py
"""
Entry point for the PyList project.
"""
from src.telegram_utils import fetch_spotify_links_from_telegram
from src.spotify_utils import add_tracks_to_playlist, save_links_to_csv
from config import CSV_FILENAME, PLAYLIST_ID


def main():
    links = fetch_spotify_links_from_telegram()
    save_links_to_csv(links, CSV_FILENAME)
    add_tracks_to_playlist(links, PLAYLIST_ID)


if __name__ == "__main__":
    main()

