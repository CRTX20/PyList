import logging
import csv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SPOTIFY_SCOPE

def save_links_to_csv(links, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["spotify_link"])
        for link in links:
            writer.writerow([link])
    logging.info(f"Saved {len(links)} links to {filename}")

def get_existing_track_ids(sp, playlist_id):
    existing_tracks = []
    results = sp.playlist_items(playlist_id)
    while results:
        for item in results["items"]:
            existing_tracks.append(item["track"]["id"])
        if results["next"]:
            results = sp.next(results)
        else:
            break
    return set(existing_tracks)

def add_tracks_to_playlist(links, playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SPOTIFY_SCOPE
    ))
    track_ids = [link.split('/')[-1] for link in links]
    try:
        existing_track_ids = get_existing_track_ids(sp, playlist_id)
    except Exception as e:
        logging.error(f"Error fetching playlist tracks: {e}")
        return
    new_track_ids = [track_id for track_id in track_ids if track_id not in existing_track_ids]
    for track_id in new_track_ids:
        logging.info(f"New track to add: {track_id}")
    if new_track_ids:
        try:
            sp.playlist_add_items(playlist_id, new_track_ids)
            logging.info(f"Added {len(new_track_ids)} new tracks to the Spotify playlist.")
        except Exception as e:
            logging.error(f"Error adding tracks to playlist: {e}")
    else:
        logging.info("No new tracks to add.")

