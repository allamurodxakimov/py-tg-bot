from dotenv import load_dotenv
import os

load_dotenv()

def get_token() -> str:
    return os.getenv('TOKEN')
