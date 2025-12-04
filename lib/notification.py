import os
import json
import telebot

from lib.utils import write_to_json

from dotenv import load_dotenv
load_dotenv()

TELEBOT_ADMIN_ALIAS = os.getenv("telegram_chat_ID")


class Notification:
    """ Basic Notification class for Telebot. """

    def __init__(self, settings):
        """ initialize baby. """

        self.settings = settings
        self.manifest = settings.manifest

        self.ADMIN_ID = TELEBOT_ADMIN_ALIAS

    def send_notification(self, text, BOT_TOKEN):
        """ Send notification to chat ID only. """

        bot = telebot.TeleBot(BOT_TOKEN)
        notifications = self.settings.get_setting("notifications")

        if notifications == True:
            try:
                res = bot.send_message(
                    chat_id=self.ADMIN_ID,
                    allow_sending_without_reply=True,
                    text=str(text)
                )

                if res:
                    payload = res.json

                    # Write out the response from the last notification sent.
                    if isinstance(payload, str):
                        payload = json.loads(payload)
                        write_to_json(self.manifest, payload)

                return True

            except Exception as e:
                print('TeleBot error?!')
                print(e)

                return False

        else:
            print('Notifications have been turned off.')


if __name__ == "__main__":

    BotNot = Notification()
    BotNot.send_notification("Hellos! ✅")
