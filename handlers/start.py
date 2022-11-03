from config import *
from utils import *


def start_menu(status: bool):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(
        text=get_string("Visit Website", LANGUAGE), url="www.google.com"
    )

    b = types.InlineKeyboardButton(
        text=get_string("Join Public Chat", LANGUAGE), url="www.google.com"
    )
    c = types.InlineKeyboardButton(
        text=get_string("Join Private Channel", LANGUAGE), url="www.google.com"
    )

    if status == False:
        keyboard.add(a)
    else:
        keyboard.add(a, b, c)
    return keyboard


def start_menu2():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(
        text=get_string("Register Account", LANGUAGE), callback_data="register"
    )
    b = types.InlineKeyboardButton(
        text=get_string("Share Invitation", LANGUAGE), callback_data="invite"
    )
    c = types.InlineKeyboardButton(
        text=get_string("Contact Agent", LANGUAGE), callback_data="contact"
    )
    d = types.InlineKeyboardButton(
        text=get_string("Go Back", LANGUAGE), callback_data="back"
    )
    keyboard.add(a, b, c, d)
    return keyboard


@bot.message_handler(regexp='Start')
@bot.message_handler(commands=["start"])
def startbot(msg):
    "Ignites the bot application to take action"

    chat, m_id = get_received_msg(msg)
    bot.delete_message(chat.id, m_id)

    bot.send_chat_action(msg.from_user.id, "typing")
    # check user in the database to see if they registered
    user, _ = db_client.get_account(msg.from_user.id)

    if user == None:
        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/nm9NTpZ",
            caption=get_string(
                "You are not a registered user to this bot and as such, can not view it's content.\n\n Click /invitecode to validate your access with a referral code and have access to all the bot's commands.",
                LANGUAGE,
            ),
            reply_markup=start_menu(False),
            parse_mode="html",
        )

    else:

        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/nm9NTpZ",
            caption=get_string(
                f"Welcome Back <b>{user.nickname}</b>,\n\nHere are the bot commands available to your {user.account_type} account.\
                    \n- /start to open default menu\n\nGet Yourself familiar by joining the invite room for more info and news update.",
                LANGUAGE,
            ),
            reply_markup=start_menu(True),
            parse_mode="html",
        )

        bot.send_video(
            msg.from_user.id,
            video=open("vid1.mp4", "rb"),
            supports_streaming=True,
            allow_sending_without_reply=True,
            reply_markup=start_menu2()
        )


@bot.message_handler(regexp="^Back")
def startbotn(msg):
    startbot(msg)


# photo='https://ibb.co/nm9NTpZ',
