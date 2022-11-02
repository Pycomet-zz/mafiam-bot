from config import *
from utils import *
from models import Account


def gender_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="🚹  Male", callback_data="male")
    b = types.InlineKeyboardButton(text="🚺 Female", callback_data="female")
    keyboard.add(a, b)
    return keyboard


@bot.message_handler(commands=["register"])
def register_user(msg):
    "Register Msg Handler"

    chat, m_id = get_received_msg(msg)
    bot.delete_message(chat.id, m_id)

    bot.send_chat_action(msg.from_user.id, "typing")

    bot.send_message(
        msg.from_user.id,
        get_string(
            "Getting registered to this bot is pretty simple, following the steps of the questions below;",
            LANGUAGE,
        ),
    )

    question = bot.send_photo(
        msg.from_user.id,
        photo="https://ibb.co/nm9NTpZ",
        caption=get_string("Input your nickname here 👇", LANGUAGE),
    )

    bot.register_next_step_handler(question, get_name)


def get_name(msg):
    "Ask the gender of the user"

    name = msg.text
    chat, m_id = get_received_msg(msg)

    # Delete prev question
    bot.delete_message(chat.id, m_id - 1)

    if name == "":
        name = msg.from_user.first_name

    account = Account(name, int(msg.from_user.id), account_type="受付中")

    isNew = db_client.save_account(account)

    bot.delete_message(chat.id, m_id)

    bot.send_chat_action(msg.from_user.id, "typing")

    if isNew:
        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/nm9NTpZ",
            caption=get_string(
                "Pick your gender from the options below 👇", LANGUAGE),
            reply_markup=gender_menu()
        )

    else:
        bot.send_message(
            msg.from_user.id,
            get_string(
                "You are already a registered member! Move along", LANGUAGE),
        )


def get_secret_question(msg):
    "Ask Secret Question"
    secret_question = msg.text
    chat, m_id = get_received_msg(msg)

    # Delete prev question
    bot.delete_message(chat.id, m_id - 1)

    status = db_client.update_account(
        msg.from_user.id, {"secretQuestion": secret_question}
    )

    bot.delete_message(chat.id, m_id)

    bot.send_chat_action(msg.from_user.id, "typing")

    if status == True:
        question = bot.send_message(
            msg.from_user.id,
            get_string(
                f"Enter the answer to your secret question👇 ",
                LANGUAGE
            )
        )

        bot.register_next_step_handler(question, get_secret_answer)


def get_secret_answer(msg):
    answer = msg.text
    chat, m_id = get_received_msg(msg)

    # Delete prev question
    bot.delete_message(chat.id, m_id - 1)

    bot.send_chat_action(msg.from_user.id, "typing")

    status = db_client.update_account(
        msg.from_user.id, {"secretAnswer": answer})

    bot.delete_message(chat.id, m_id)

    bot.send_chat_action(msg.from_user.id, "upload_document")

    if status == True:
        user, u_id = db_client.get_account(msg.from_user.id)

        ref_code = str(u_id)[:6]
        db_client.update_account(msg.from_user.id, {"code": ref_code})

        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/nm9NTpZ",
            caption=get_string(
                f"🎉<b>Welcome to MAFIAM CLUB {user.nickname},🎉 \n\nClick /start to get started exploring...</b>",
                LANGUAGE,
            ),
            parse_mode="html",
        )


# Callback Handlers
@bot.callback_query_handler(func=lambda c: c.data in ["male", "female"])
def button_callback_answer(call):
    """
    Button Response
    """

    bot.send_chat_action(call.from_user.id, "typing")
    # ADDING THE GENDER
    if call.data == "male" or call.data == "female":
        # Delete prev question
        bot.delete_message(call.from_user.id, call.message.message_id)

        status = db_client.update_account(
            call.from_user.id, {"sex": call.data})

        if status == True:

            question = bot.send_photo(
                call.from_user.id,
                photo="https://ibb.co/nm9NTpZ",
                caption=get_string(
                    f"Enter your own custom secret question here👇 \n<b>(📌 write in a safe place)</b>\n<b>(📌 This question remains exclusive to you alone)</b>",
                    LANGUAGE,
                ),
                parse_mode="html",
            )

            bot.register_next_step_handler(question, get_secret_question)

    else:
        print("invalid callback passed")
        pass
