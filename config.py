import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME","BABInfjC_W4KZifhmhu1FX8zkr8bSjW70MCO7FWXEFsLD4IaCFH26xNSnlLw72qMiM2_4aVe3XYoN8YtKxKfCFVqg2uiQyDWbZa5xbTohsv1CisXXC-j17csHBpnuBfjsTyzKpgLkrYW6GnuCM9qz5umFiBxFiuCzBHQo-Fb8XRBWFVqR4co6j0howOXyWTl6vmVj3fd35heSnE5wOyKUedd92ZspI6OG9DvayScnl067KZ5PEOImQyCEGX-jZmsFkiMxiKTXEg20LaI1HZTtLgUXnFyyKBKXDvApwgS0pBWfTcB04uvKdmzEw6xGVrRqPCy2EUkz_Cu4dFhxfixe89WAAAAAUggB3AA")
BOT_TOKEN = getenv("BOT_TOKEN","5819189910:AAFsNCM_SCenvQ1bXQNFPs9dtBOFbbL99V8")
API_ID = int(getenv("API_ID","10858814"))
MONGODB_URL = getenv("MONGODB_URL")
API_HASH = getenv("API_HASH","31c0f952162f1c1fadf4e38bbd098a4d")
OWNER_NAME = getenv("OWNER_NAME", "JABWA")
MONGODB_URL = getenv("MONGODB_URL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "updateLaith")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/3470a632a034837abe424.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
FORCE_SUBSCRIBE_TEXT = getenv("SUBSCRIBE_TEXT", f"عليك الاشتراك في قناة البوت لتتمكن من استخدامة \n- @{UPDATES_CHANNEL}")
SUBSCRIBE = getenv("SUBSCRIBE", "no")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1965534755").split()))
