import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "1269156180:AAFrdydVaAgL_19aYkXhSUVO064sNjD0hLA"

admins = [
    "266039426",
    # "ADMIN_ID",
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
 
PHOTO_PATH="C:/Users/RobertTes/Documents/Python/Telegram_bot/documents/photos/meme.jpg"