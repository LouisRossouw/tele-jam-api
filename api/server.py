from typing import List
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from lib.format_telegram import build_txt
from lib.bot import Bot

from dotenv import load_dotenv
load_dotenv()


class TelegramAPI:
    def __init__(self, settings, notification):
        self.settings = settings
        self.notification = notification

        self.app = FastAPI()
        self.routes()

    def routes(self):
        @self.app.get("/notify/bot/{bot_name}")
        def notify(bot_name: str, text: List[str]):

            bot = Bot(bot_name)
            formatted_txt = build_txt(text)

            has_sent = False

            if bot.active:
                has_sent = self.notification.send_notification(
                    formatted_txt, bot.token)

            context = {
                "ok": True if bot.active and has_sent else False,
                "bot_active": bot.active,
                "bot": bot.label,
            }

            return JSONResponse(
                content=context,
                status_code=status.HTTP_200_OK
            )

        @self.app.get("/config")
        def config():
            return self.settings.get_config()

    def run(self, host="0.0.0.0", port=5001):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)
