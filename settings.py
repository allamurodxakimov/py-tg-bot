from dotenv import load_dotenv
import os

load_dotenv()

def get_token() -> str:
    TOKEN = os.getenv('TOKEN')
    if not TOKEN:
        raise ValueError('TOKEN mavjud emas.')

    return TOKEN
