from config import *
from utils import *


# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """


    # ADDING THE GENDER
    if call.data == "male" or call.data == "female":
        user = get_account(call.from_user.id)
        print(user)

        status = db_client.update_account(
            call.from_user.id,
            { "sex": call.data }
        )

        if status == True:
            question = bot.send_message(
                call.from_user.id,
                get_string(
                    "Please enter your own custom secret question ? (NOTE:- This must remain exclusively hidden to you alone)",
                    LANGUAGE
                )
            )
            bot.register_next_step_handler(question, get_secret_question)
            
        print(status)


    else:
        pass
