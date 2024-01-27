from telegram.ext import CallbackContext
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    welcome_msg = f'Assalomu alaykum, {user.full_name}'

    bot = context.bot
    bot.send_message(chat_id=user.id, text=welcome_msg)

def ok(update: Update, context: CallbackContext):
    user = update.message.from_user

    bot = context.bot
    bot.send_message(
        chat_id = user.id,
        text = "Yomon",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="Ho'p",
                        request_contact=True,
                    ),
                    KeyboardButton(
                        text="Albata",
                        request_location=True
                    )
                ],
                [
                    KeyboardButton(
                        text="Okay",
                        request_location=True
                    ),
                    KeyboardButton(
                        text="Good",
                        request_contact=True
                    )
                ]
                
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
def til(update:Update, context:CallbackContext):
    user = update.message.from_user
    
    bot = context.bot
    bot.send_message(
        chat_id = user.id,
        text = "Til yoki Bruzerni tanlang ",
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="O'zbek",callback_data='some'),InlineKeyboardButton(text="Ruscha",callback_data="some")],
                [InlineKeyboardButton(text="Google",url="https://www.google.com/"),InlineKeyboardButton(text="Ynadex",url="https://www.yandex.com/")],
            
            ],
            
        )
    )
def echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_message(
        chat_id = user.id, text = message.text,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=f'{message.text} 1'),KeyboardButton(text=f'{message.text} 2')],
                [KeyboardButton(text=f'{message.text} 3'),KeyboardButton(text=f'{message.text} 4')]
            ],
            resize_keyboard=True,
        )
    )

def echo_photo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_photo(
        chat_id=user.id, photo=message.photo[-1],
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=f'rasm 1'),KeyboardButton(text=f'rasm 2')],
                [KeyboardButton(text=f'rasm 3'),KeyboardButton(text=f'rasm 4')],
            ],
            resize_keyboard=True
        )    
    )

def echo_audio(update:Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_audio(chat_id = user.id, audio = message.audio)

def echo_video(update:Update, context:CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_video(chat_id = user.id, video = message.video)

def echo_document(update:Update, context:CallbackContext):
    user = update.message.from_user
    message = update.message
    bot = context.bot
    bot.send_document(chat_id = user.id, document = message.document.file_id,caption = message.caption)

def echo_dice(update:Update, context:CallbackContext):
    user = update.message.from_user
    message = update.message
    bot = context.bot
    bot.send_dice(chat_id = user.id, text = message.dice.emoji)

def echo_animation(update:Update, contaxt:CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = contaxt.bot
    bot.send_animation(chat_id = user.id, text = message.animation.file_id)

def echo_contact(update:Update, context:CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_contact(chat_id = user.id, text = message.forward_from)

def echo_location(update:Update, contaxt:CallbackContext):
    user = update.message.from_user
    message = update.message
    bot = contaxt.bot
    bot.send_location(user.id, message.location)

