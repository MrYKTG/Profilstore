# Don't Remove Credit
# Made by @MrYKTG https://github.com/MrYKTG
# @mrxeontg @xeonbotz
# Ask Doubt on telegram @Mrxeontg
# Copyright (c) 2026 XeonBotz
# All Rights Reserved.
import logging
import os
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "bot.log"
PORT = '8000'
OWNER_ID = 821215952
MSG_EFFECT = 5046500389126442

# BOT CONFIGURATION
# ===========================

# Telegram API Credentials (Get from https://my.telegram.org)
API_ID = 15529802
API_HASH = "92bcb6aa798a6f1feadbc917fccb54d3"
BOT_TOKEN = ""

# ===========================
# DATABASE
# ===========================

# MongoDB Connection String
DATABASE_URI = ""
DATABASE_NAME = "OFLIX"

# ===========================
# CHANNELS
# ===========================

# Main Database Channel ID (where files are stored)
DB_CHANNEL = -1003536384063

# Force Subscribe Channels (users must join these)
FORCE_SUB_CHANNELS = []

# ===========================
# ADMIN
# ===========================

# Admin User IDs (can use admin commands)
ADMINS = [6048003536, 821215952, 8365451390]

# ===========================
# SERVER (Optional)
# ===========================

# Use webhook instead of polling
WEBHOOK = False

# CUSTOMIZATION (Optional)
# ===========================

# Auto delete timer (seconds, 0 to disable)
AUTO_DELETE = 300

# Protect content (prevent forwarding)
PROTECT_CONTENT = False

# Disable share button
DISABLE_BUTTON = False

# AroLinks URL Shortener Configuration
AROLINKS_API_TOKEN = "d5911095597018fad72bf9ad1df544163b1520db"
AROLINKS_API_URL = "https://shortxlinks.com"

# URL Shortener Providers Configuration
URL_SHORTENERS = {
    'arolinks': {
        'name': 'Shortxlinks',
        'api_url': 'https://shortxlinks.com/api',
        'api_token': AROLINKS_API_TOKEN,
        'format': 'text',
        'active': True
    }
}

# BYPASS ATTEMPT MEDIA
# ===========================
BYPASS_ATTEMPT_MEDIA = "https://videotourl.com/videos/1788160021118-5b825ba1-c273-4df3-9c10-1649b6c73ee7.mp4 https://i.postimg.cc/4ykP3SHc/IMG-20250927-131101-178.jpg"

MYPLAN_IMG = "https://i.postimg.cc/L6D7Vzcm/46Lv-Lz-MD19tzyo-Pc7HUf4PPvi62.jpg"

# Don't Remove Credit
# Made by @MrYKTG https://github.com/MrYKTG
# @mrxeontg @xeonbotz
# Ask Doubt on telegram @Mrxeontg
# Copyright (c) 2026 XeonBotz
# All Rights Reserved.

# ===========================
# PERMANENT LINK SYSTEM
# ===========================
# When True, the bot sends a website-based permanent link
# instead of a raw t.me link. The same URL survives bot bans.
PERMANENT_LINKS = os.environ.get("PERMANENT_LINKS", "True").lower() == "true"

# The gateway domain — same for ALL your bots.
GATEWAY_BASE_URL = os.environ.get("GATEWAY_BASE_URL", "https://xeonflix.netlify.app")

# ┌─────────────────────────────────────────────────────────────┐
# │  CHANGE THIS PER BOT:                                        │
# │    Bot 1  →  "Neostart"                                      │
# │    Bot 2  →  "Neostart2"                                     │
# │    Bot 3  →  "Neostart3"                                     │
# │    Bot 4  →  "Neostart4"                                     │
# └─────────────────────────────────────────────────────────────┘
PERMANENT_START_POINT = os.environ.get("PERMANENT_START_POINT", "VEXON")

# ┌─────────────────────────────────────────────────────────────┐
# │  CHANGE THIS PER BOT:                                        │
# │    Bot 1  →  "https://wee-dot-yedhuku2004-543d97f6.koyeb.app"
# │    Bot 2  →  "https://leading-randee-yedhuku2003-0e35c718.koyeb.app"
# │    Bot 3  →  "https://eonofx1bot.onrender.com"               │
# │    Bot 4  →  "https://xsaga-h9af.onrender.com"               │
# └─────────────────────────────────────────────────────────────┘
API_BASE_URL = os.environ.get(
    "API_BASE_URL",
    "https://dominant-marla-yedhuku20005-e5fcc630.koyeb.app"
)

# Lifetime for the /access/<hex>?url=... masking tokens (minutes)
ACCESS_TOKEN_EXPIRY_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRY_MINUTES", "10"))


# ===========================
# ===========================
# PRO CAPTION SYSTEM
# ===========================
# Enable/disable PRO custom caption (True/False)
ENABLE_PRO_CAPTION = os.environ.get("ENABLE_PRO_CAPTION", "True").lower() == "true"

# ──────────────────────────────────────────────────────────────
#  🎨 PRO_CUSTOM_CAPTION — HOW TO USE
# ──────────────────────────────────────────────────────────────
#  Only ONE template should be active at a time.
#  To activate an option:
#     1. UNCOMMENT the option you want (remove the leading #)
#     2. COMMENT OUT all the other options (add # at the start)
#     3. Save the file and restart the bot.
#
#  If you leave ALL options commented, the bot uses the fallback below
#  (Option B is the built-in default when no env var is set).
#
#  AVAILABLE PLACEHOLDERS:
#     {previouscaption} / {caption}  → original DB caption (HTML) or filename
#     {filename} / {file_name}       → original filename
#     {filesize} / {file_size}       → human-readable size (e.g. "1.2 GiB")
#     {duration}                     → video/audio duration (e.g. "1h 23m")
#     {bot_username} / {bot}         → current bot's @username
# ──────────────────────────────────────────────────────────────

# ┌─────────────────────────────────────────────────────────────┐
# │  OPTION A — Simple branding (adds a footer line below)       │
# │  Result:  [original caption]                                 │
# │           🎬 Powered by @Xeonflix                            │
# └─────────────────────────────────────────────────────────────┘
#PRO_CUSTOM_CAPTION = "<b>{previouscaption}</b>\n\n🎬 Powered by @Xeonflix"


# ┌─────────────────────────────────────────────────────────────┐
# │  OPTION B — Link wrap (DEFAULT — used if nothing else set)   │
# │  Result:  [original caption]  ← clickable, opens @Xeonflix   │
# └─────────────────────────────────────────────────────────────┘
#PRO_CUSTOM_CAPTION = "<a href='https://t.me/Xeonflix'><b>{previouscaption}</b></a>"


# ┌─────────────────────────────────────────────────────────────┐
# │  OPTION C — Full metadata card (filename + size + duration)  │
# │  Result:  ┌─────────────────────────────────┐                │
# │           │ [filename]                      │                │
# │           │ 📦 1.2 GiB   ⏱ 1h 23m           │                │
# │           │                                 │                │
# │           │ [original caption in quote]     │                │
# │           │                                 │                │
# │           │ 🔗 @your_bot_username           │                │
# │           └─────────────────────────────────┘                │
# └─────────────────────────────────────────────────────────────┘
#PRO_CUSTOM_CAPTION = (
#    "<b>{filename}</b>\n"
#    "📦 {filesize}   ⏱ {duration}\n\n"
#    "<blockquote>{previouscaption}</blockquote>\n\n"
#    "🔗 @{bot_username}"
#)


# ──────────────────────────────────────────────────────────────
#  ACTIVE TEMPLATE  ← uncomment the one you picked above,
#  or leave the env-var default (Option B) as-is.
# ──────────────────────────────────────────────────────────────
# Don't Remove Credit
# Made by @MrYKTG https://github.com/MrYKTG
# @mrxeontg @xeonbotz
# Ask Doubt on telegram @Mrxeontg
# Copyright (c) 2026 XeonBotz
# All Rights Reserved.
PRO_CUSTOM_CAPTION = os.environ.get(
    "PRO_CUSTOM_CAPTION",
    "<a href='https://t.me/Xeonflix'><b>{previouscaption}</b></a>"
)


def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
