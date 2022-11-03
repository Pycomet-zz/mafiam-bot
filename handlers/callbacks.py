from config import *
from utils import *
from .register import register_user
from .invite import invite_user
from .start import startbot

# Callback Handlers For Menu Button


@bot.callback_query_handler(
    func=lambda c: c.data in ["register", "invite", "contact", "back"]
)
def button_callback_answer(call):
    """
    Button Response
    """

    bot.send_chat_action(call.from_user.id, "typing")
    # ADDING THE GENDER
    if call.data == "register":

        register_user(call)

    elif call.data == "invite":

        invite_user(call)

    elif call.data == "contact":

        print("No contact yet")

    elif call.data == "back":

        startbot(call)

    else:
        pass
