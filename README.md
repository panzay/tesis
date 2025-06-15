Here’s a **`README.md`** template for your meeting-transcription Flask app. Just drop this into your project root and update as needed.


# Meeting Transcription Service

A real-time meeting transcription backend using Azure Speech Services, Flask-SocketIO, and SQLite. Every recognized utterance is saved to a local database and broadcast to connected clients.

---

## Features

- **Continuous speech recognition** via Azure Cognitive Services
- **Real-time updates** to web clients using Flask-SocketIO
- **Persistent storage** of transcripts in SQLite
- **Rotating file logging** for debug/production
- Easy configuration via a `.env` file

---

## Tech Stack

- Python 3.9+
- Flask
- Flask-SocketIO
- Flask-SQLAlchemy
- Azure Cognitive Services Speech SDK
- SQLite (via SQLAlchemy)
- python-dotenv

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/meeting-transcription.git
   cd meeting-transcription

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Copy `.env.example` to `.env`**

   ```bash
   cp .env.example .env
   ```

2. **Edit `.env`** and fill in your keys:

   ```dotenv
   # Azure Speech Services
   SPEECH_KEY=your-azure-speech-key
   SPEECH_REGION="southeastasia"

   # Azure Blob Storage (optional, if you upload recordings)
   BLOB_SAS_TOKEN=your-blob-sas-token
   BLOB_SAS_URL=https://<account>.blob.core.windows.net/<container>

   # Database & Flask
   SQLALCHEMY_DATABASE_URI="sqlite:///transcripts.db"
   SECRET_KEY="secret-key-for-flask"
   ```

3. **Verify** that `config.py` reads from your `.env` and points `SQLALCHEMY_DATABASE_URI` at `transcripts.db`.

---

## Usage

1. **Initialize & run** the app:

   ```bash
   python app.py
   ```

2. **Open** your browser to `http://localhost:5000`

   * Client connects via SocketIO
   * Speak into your default microphone
   * Each recognized phrase appears on screen and is saved in `transcripts.db`

3. **Inspect the database** (optional):

   ```bash
   sqlite3 transcripts.db
   sqlite> .tables
   transcript
   sqlite> SELECT * FROM transcript LIMIT 5;

   # quit
   sqlite> .quit
   ```

---

## Project Structure

```
meeting-transcription/
├── app.py             # Main Flask + SocketIO + speech-to-text logic
├── config.py          # Configuration & SQLAlchemy URI
├── requirements.txt   # pip dependencies
├── transcripts.db     # Generated SQLite file
├── .env.example       # Example environment variables
└── templates/
    └── index.html     # Simple client UI for testing
```

---

## Logging

* Logs are written to `app.log` with a rotating handler
* Check `app.log` for INFO, WARNING, and ERROR entries

---
