from os import environ

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv

load_dotenv()

token = environ.get('BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())