from config import *
from utils import *

def start_menu(msg):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    
    a = types.KeyboardButton(get_string("I Am A Passenger?", LANGUAGE))
    b = types.KeyboardButton(get_string("I Am A Bus Operator?", LANGUAGE))
    c = types.KeyboardButton(get_string("Referral Link", LANGUAGE))
    d = types.KeyboardButton(get_string("About Us", LANGUAGE))
    e = types.KeyboardButton(get_string("Rules & Regulations", LANGUAGE))
    f = types.KeyboardButton(get_string("Language Switcher", LANGUAGE))
    g = types.KeyboardButton(get_string("Contact Us", LANGUAGE))

    keyboard.add(a,b,c,d,e,f,g)
    return keyboard
 

@bot.message_handler(commands=['start'])
def startbot(msg):
    # import pdb; pdb.set_trace()
    user.id = msg.from_user.id
    "Ignites the bot application to take action"

    bot.reply_to(
        msg,
        get_string("Welcome To The Registration Bot. Get Yourself familiar by joining the invite room for more info and news update.", LANGUAGE),
        reply_markup=start_menu(msg)
    )

    

@bot.message_handler(regexp="^Back")
def startbotn(msg):
    startbot(msg)


