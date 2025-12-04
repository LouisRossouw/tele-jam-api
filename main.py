from settings import Settings
from lib.notification import Notification

from api.server import TelegramAPI

if __name__ == "__main__":

    settings = Settings()
    notification = Notification(settings)

    server = TelegramAPI(settings, notification)

    server.run(host=settings.host, port=settings.port)
