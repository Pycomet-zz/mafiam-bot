import asyncio
import logging
import os
import re
from flask import Flask, request
from datetime import date
from googletrans import Translator
import telebot
from telebot import types

from dotenv import load_dotenv
load_dotenv()

from models import User

user = User
LANGUAGE = user.language

# # Language setup
# os.environ["LANGUAGE"] = "en"
# LANGUAGE = os.getenv("LANGUAGE")
translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])

# Logging Setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv('TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

DEBUG = False
SERVER_URL = os.getenv("SERVER_URL")

bot = Client(api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
app = Flask(__name__)
