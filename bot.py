from settings import get_token
from telegram import Bot

TOKEN = get_token()

bot = Bot(TOKEN)

last_update = bot.get_updates()[-1]

user = last_update.message.from_user
message = last_update.message

bot.send_message(
    chat_id=user.id,
    text=message.text
)
