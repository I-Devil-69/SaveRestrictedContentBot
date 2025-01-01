#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("29419742", default=None, cast=int)
API_HASH = config("e2ffa892d1c47a8ad81d3d49fdf4f7b1", default=None)
BOT_TOKEN = config("7208177037:AAFVBPx_nGs3AgR7-kozox8gfdpYlr1_mMI", default=None)
SESSION = config("BQE8lCYAl5c6yWn_J8wYG5EtxPOLd_7TrR7PHQn_07IC6oaB22WbctrgJrwqsh4BWG5oruJ1q_fz3j4S3tdw7Zn50T5UxOrXQiLsGcTOfwPAQyV_M5s0oeMPruwz7diP8Y3d86Vh3Uj1A_ddGA_XCAtAxjl2BD64z9KZ2X73UugpabgLXX74vEzOqI28bsbTUz9OC3TIdLLxMkmU2oZA7l-EEOqnThjQQWUrp-OxQZdbS6BB9eoJ9pKAGfIvhS5y8wBmyY4CsQrF1KyVL_i-OjP8WaKdyWPb2RlW4u2YazlZZxM7-dLkywRMjnbz0Is-uTMv400WfVlgmWOHzwDr_qVFhcILRgAAAAGRAfg3AA", default=None)
FORCESUB = config("demonarmy", default=None)
AUTH = config("6727792695", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
