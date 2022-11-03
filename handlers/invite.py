from config import *
from utils import *


@bot.message_handler(commands=["invitecode"])
def invite_user(msg):
    "Ignites The Invite Code Assessment"

    user, _ = db_client.get_account(msg.from_user.id)

    if hasattr(msg, "message_id"):
        chat, m_id = get_received_msg(msg)
        bot.delete_message(chat.id, m_id)

    bot.send_chat_action(msg.from_user.id, "typing")

    if user == None:

        question = bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/C6vztBZ",
            caption=get_string(
                "Please enter your invite code here ? ",
                LANGUAGE,
            ),
        )
        bot.register_next_step_handler(question, get_invite_code)

    else:
        print(user)

        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/C6vztBZ",
            caption=get_string(
                f"You are welcome to invite your friends and family to purchase and be part of our community. \n\nThis would certainly also build your account reputation in the community (⭐ )\n\n<b>Invitation Code - {user.code}</b>",
                LANGUAGE
            ),
            parse_mode="html",
        )

        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/J3Q7Q8k",
            allow_sending_without_reply=True,
        )


def get_invite_code(msg):
    ref_code = msg.text
    chat, m_id = get_received_msg(msg)

    # Delete prev question
    bot.delete_message(chat.id, m_id - 1)

    # validate ref_code
    user = db_client.get_account_by_ref(code=ref_code)

    bot.delete_message(chat.id, m_id)

    bot.send_chat_action(msg.from_user.id, "typing")

    if user == None:
        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/nm9NTpZ",
            caption=get_string(
                "<b>You entered an invalid referral code.</b> \n\nClick on /invitecode to try again...",
                LANGUAGE,
            ),
            parse_mode="html"
        )

    else:

        # register referral
        referral = Referral(
            user_id=user.user_id,
            ref_code=ref_code,
            ref_user_id=msg.from_user.id,
        )
        status = db_client.save_ref(referral=referral)

        if status == False:
            bot.send_message(
                msg.from_user.id,
                get_string(
                    "An error occurred! Please check in with support.", LANGUAGE
                ),
            )

        else:

            bot.send_photo(
                msg.from_user.id,
                photo="https://ibb.co/pfHDP4v",
                caption=get_string(
                    "<b>Congratulations! Welcome aboard</b> \n\n Click /register to get an account right away and join the chat forums for news update.",
                    LANGUAGE,
                ),
                parse_mode="html",
            )

        bot.send_photo(
            msg.from_user.id,
            photo="https://ibb.co/J3Q7Q8k",
            allow_sending_without_reply=True,
        )
