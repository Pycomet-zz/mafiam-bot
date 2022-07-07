from config import *
from utils import *


def start_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=get_string("Join Public Group", LANGUAGE), callback_data="public-group")
    keyboard.add(a)
    return keyboard
 

@bot.message_handler(commands=['start'])
def startbot(msg):
    # import pdb; pdb.set_trace()
    user.id = msg.from_user.id
    "Ignites the bot application to take action"

    bot.send_photo(
        msg.from_user.id,
        photo='https://ibb.co/kxffVvt'
        
    )

    bot.send_message(
        msg.from_user.id,
        get_string("Welcome To The Registration Bot. Get Yourself familiar by joining the invite room for more info and news update.", LANGUAGE),
        reply_markup=start_menu()
    )

    

@bot.message_handler(regexp="^Back")
def startbotn(msg):
    startbot(msg)




# photo='https://ibb.co/nm9NTpZ',