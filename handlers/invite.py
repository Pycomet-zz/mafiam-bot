from config import *
from utils import *


@bot.message_handler(commands=["invitecode"])
def invitebot(msg):
    "Ignites The Invite Code Assessment"

    user, _ = db_client.get_account(msg.from_user.id)

    if user == None:

        bot.send_photo(msg.from_user.id, photo="https://ibb.co/kxffVvt")

        question = bot.send_message(
            msg.from_user.id,
            get_string(
                "Please enter your invite code here ? (If you have no code, use 000000)",
                LANGUAGE,
            ),
        )
        bot.register_next_step_handler(question, get_invite_code)

    else:
        print(user)

        bot.send_message(
            msg.from_user.id,
            get_string(f"Your referral code - <b>{user.code}</b>", LANGUAGE),
            parse_mode="html",
        )


def get_invite_code(msg):
    ref_code = msg.text

    # validate ref_code
    user = db_client.get_account_by_ref(code=ref_code)

    if user == None:
        bot.send_message(
            msg.from_user.id,
            get_string(
                "Sorry, but you entered an invalid referral code. Click on /invitecode to try again...",
                LANGUAGE,
            ),
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
            bot.send_message(
                msg.from_user.id,
                get_string(
                    "<b>Congratulations! Welcome aboard</b> \n\n Click /register to get an account right away and join the chat forums for news update.",
                    LANGUAGE,
                ),
                parse_mode="html",
            )
