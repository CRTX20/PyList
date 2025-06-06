import logging
import re
from telethon.sync import TelegramClient
from config import API_ID, API_HASH, SESSION_NAME, CHAT_ID

def extract_spotify_links(text):
    if not text:
        return []
    return re.findall(r"https?://open\.spotify\.com/track/[a-zA-Z0-9]+", text)


def fetch_spotify_links_from_telegram():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    spotify_links = []
    try:
        with client:
            logging.info("Connected to Telegram.")
            chat = client.get_entity(CHAT_ID)
            for message in client.iter_messages(chat, limit=400):
                links = extract_spotify_links(message.text)
                spotify_links.extend(links)
    except Exception as e:
        logging.error(f"Error fetching messages: {e}")
        return []
    logging.info(f"Found {len(spotify_links)} Spotify links.")
    return spotify_links

