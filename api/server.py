from fastapi import FastAPI, status
from fastapi.responses import JSONResponse


class TelegramAPI:
    def __init__(self, settings):
        self.settings = settings

        self.app = FastAPI()
        self.routes()

    def routes(self):
        @self.app.get("/notify")
        def notify():

            # TODO; Send a notification via telegram.

            return JSONResponse(
                content={"ok": True},
                status_code=status.HTTP_200_OK
            )

        @self.app.get("/config")
        def config():
            return self.settings.get_config()

        # TODO:
        # @self.app.put("/config")
        # def update_config():
        #     return

    def run(self, host="0.0.0.0", port=5001):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)
