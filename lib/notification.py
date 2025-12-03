import os
import telebot

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("telegram_token")
TELEBOT_ADMIN_ALIAS = os.getenv("telegram_chat_ID")

# TODO;


class Notification():
    """ Basic Notification class for Telebot. """

    def __init__(self):
        """ initialize baby. """

        # TODO; Get this from the config
        self.notifications = True

        self.bot = telebot.TeleBot(BOT_TOKEN)
        self.ADMIN_ID = TELEBOT_ADMIN_ALIAS

    def send_notification(self, text):
        """ Send notification to chat ID only. 
        :param text: string """

        if self.notifications == True:
            try:
                self.bot.send_message(chat_id=self.ADMIN_ID,
                                      allow_sending_without_reply=True, text=str(text))
            except Exception as e:
                print('TeleBot error?!')
                print(e)


if __name__ == "__main__":

    BotNot = Notification()
    BotNot.send_notification("Hellos! ✅")
