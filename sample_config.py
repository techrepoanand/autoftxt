import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7184992749:AAFTsquTVUItAYy3iaemoya6K1nlaMfPaLI")

    APP_ID = int(os.environ.get("APP_ID", "28156285"))

    API_HASH = os.environ.get("API_HASH", "93694f0328daa5b515c9523a0d0dd86d")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "@WatchingCenter")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6777494089").split())
