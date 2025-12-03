from settings import Settings
from api.server import TelegramAPI

if __name__ == "__main__":

    settings = Settings()
    server = TelegramAPI(settings)

    server.run(host=settings.config.get('host'),
               port=settings.config.get('port'))
