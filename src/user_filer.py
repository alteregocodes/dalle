from os import getenv

from dotenv import load_dotenv
from telegram.ext.filters import User

load_dotenv()

USER_FILTER = User(username=getenv("ALLOWED_USERNAMES", "").split(), allow_empty=True)
