import asyncio
import logging
import os
import re
from flask import Flask, request
from datetime import date
import goslate
import telebot
from telebot import types
from pymongo import MongoClient
import pymongo


from dotenv import load_dotenv
load_dotenv()

from models import User

user = User
LANGUAGE = user.language

# # Language setup
# os.environ["LANGUAGE"] = "en"
# LANGUAGE = os.getenv("LANGUAGE")
translator = goslate.Goslate()

# Logging Setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv('TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

DEBUG = True
SERVER_URL = os.getenv("SERVER_URL")

DATABASE_STRING = os.getenv("DATABASE_STRING")
client = MongoClient(DATABASE_STRING)


bot = telebot.TeleBot(token=TOKEN)
app = Flask(__name__)
