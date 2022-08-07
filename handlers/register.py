from config import *
from utils import *
from models import Account


def gender_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="🚹", callback_data="male")
    b = types.InlineKeyboardButton(text="🚺", callback_data="female")
    keyboard.add(a, b)
    return keyboard


@bot.message_handler(commands=["register"])
def register_user(msg):
    "Register Msg Handler"

    bot.reply_to(
        msg,
        get_string(
            "Getting registered to this bot is pretty simple, following the steps of the questions below;",
            LANGUAGE,
        ),
    )

    bot.send_photo(msg.from_user.id, photo="https://ibb.co/nm9NTpZ")

    question = bot.send_message(
        msg.from_user.id, get_string("Please input your nickname ?", LANGUAGE)
    )
    bot.register_next_step_handler(question, get_name)


def get_name(msg):
    "Ask the gender of the user"

    name = msg.text

    if name == "":
        name = msg.from_user.first_name

    account = Account(name, int(msg.from_user.id))

    isNew = db_client.save_account(account)

    if isNew:
        bot.send_photo(msg.from_user.id, photo="https://ibb.co/nm9NTpZ")
        bot.send_message(
            msg.from_user.id,
            get_string(
                "Please select your gender from the following options", LANGUAGE
            ),
            reply_markup=gender_menu(),
        )

    else:
        bot.send_message(
            msg.from_user.id,
            get_string("You are already a registered member! Move along", LANGUAGE),
        )


def get_secret_question(msg):
    "Ask Secret Question"
    secret_question = msg.text

    status = db_client.update_account(
        msg.from_user.id, {"secretQuestion": secret_question}
    )

    if status == True:
        bot.send_photo(msg.from_user.id, photo="https://ibb.co/nm9NTpZ")

        question = bot.send_message(
            msg.from_user.id,
            get_string(
                f"Please enter the answer to your secret question - {secret_question} ?",
                LANGUAGE,
            ),
        )
        bot.register_next_step_handler(question, get_secret_answer)


def get_secret_answer(msg):
    answer = msg.text

    status = db_client.update_account(msg.from_user.id, {"secretAnswer": answer})

    if status == True:
        user, u_id = db_client.get_account(msg.from_user.id)

        ref_code = str(u_id)[:6]
        db_client.update_account(msg.from_user.id, {"code": ref_code})

        bot.send_photo(msg.from_user.id, photo="https://ibb.co/nm9NTpZ")
        bot.send_message(
            msg.from_user.id,
            get_string(f"Welcome to the club {user.nickname}!", LANGUAGE),
        )


# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def button_callback_answer(call):
    """
    Button Response
    """

    # ADDING THE GENDER
    if call.data == "male" or call.data == "female":

        status = db_client.update_account(call.from_user.id, {"sex": call.data})

        if status == True:
            question = bot.send_message(
                call.from_user.id,
                get_string(
                    "Please enter your own custom secret question ? (NOTE:- This must remain exclusively hidden to you alone)",
                    LANGUAGE,
                ),
            )
            bot.register_next_step_handler(question, get_secret_question)

    else:
        pass
