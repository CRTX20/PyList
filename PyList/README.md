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

## Configurazione ambiente
1. Copia il file `.env.example` e rinominalo in `.env`:
   ```bash
   cp .env.example .env
   ```
2. Inserisci le tue credenziali Telegram e Spotify nel file `.env`.

## Esecuzione
1. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
2. Avvia lo script principale:
   ```bash
   python main.py
   ```

## Struttura del progetto
- `main.py`: entry point del progetto
- `src/telegram_utils.py`: funzioni per Telegram
- `src/spotify_utils.py`: funzioni per Spotify
- `config.py`: carica le variabili d'ambiente dal file `.env`
- `.env.example`: esempio di configurazione
- `requirements.txt`: dipendenze Python

## Note di sicurezza
- Non committare mai il file `.env` o `config.py` con dati sensibili su repository pubblici.
- Il file `.gitignore` è già configurato per escludere questi file.
