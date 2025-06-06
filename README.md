# PyList: Telegram to Spotify Playlist Sync

## Purpose

PyList is a Python project designed to automate the process of collecting Spotify track links shared in a Telegram group or channel and adding them to a specific Spotify playlist. This tool helps music communities and curators keep their Spotify playlists up-to-date with tracks recommended or shared in their Telegram chats, without manual copy-pasting or duplicate entries.

## Features
- Connects to a Telegram group or channel and scans recent messages for Spotify track links.
- Adds new tracks to a specified Spotify playlist, skipping tracks already present.
- Avoids adding duplicate tracks.

## How It Works
1. The script connects to Telegram using your API credentials and scans messages for Spotify track links.
2. It extracts the track IDs from the links.
3. It checks your chosen Spotify playlist for existing tracks to avoid duplicates.
4. It adds any new tracks found in Telegram to your Spotify playlist.

## Use Cases
- Community-driven playlists: Let your Telegram group curate a Spotify playlist together.
- Automated music archiving: Never miss a track shared in your chat.
- Playlist management for music curators and DJs.

## Getting Started
See the rest of this README for setup and usage instructions.

## Environment Configuration
1. Copy the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Enter your Telegram and Spotify credentials in the `.env` file.

## Running the Script
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the main script:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py`: project entry point
- `src/telegram_utils.py`: Telegram functions
- `src/spotify_utils.py`: Spotify functions
- `config.py`: loads environment variables from the `.env` file
- `.env.example`: configuration example
- `requirements.txt`: Python dependencies

