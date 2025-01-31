# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23011537"))
API_HASH = getenv("API_HASH", "cd59a9fc8cbdca6ae2b405f149cc3c8a")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5389632871").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-4707203003")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002148792713"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "2500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
