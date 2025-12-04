# Tele Jam API

### A simple Telegram notification api service - to centralize logic for my telegram alerts notifications.

#### To send a bot a message

- POST `<base_url>:<port>/notify/bot/<str:bot_name>`
- param: `<str:bot_name>`
- body: `["Hello", "\n\n", "How are thee?😀"]`

configs/bot.json config:
```
{
    "bot-name-1": {
        "active": true,
        "label": "Bot Name 1",
        "slug": "bot-name-1",
        "env_key": "botname1_telegram_token"
    },
    "bot-name-2": {
        "active": true,
        "label": "Bot Name 2",
        "slug": "bot-name-2",
        "env_key": "botname2_telegram_token"
    }
}
```

configs/config.json:
```
{
    "host": "0.0.0.0",
    "port": 5002,

    "notifications": true
}
```

.env:
```
telegram_chat_ID=""
botname1_telegram_token="" <<<< botname must match the bot.json env_key key value
```
