# Simple OpenAI image model Telegram bot

A simple and unofficial Telegram bot wrapping [OpenAI API](https://openai.com/blog/openai-api/) image models (like [DALL·E](https://openai.com/dall-e-3)), build with [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot)!

Just send a prompt and the bot will respond with a generated image!



## Requirements

This bot was built with `Python 3.12`, [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) and [`openai-python`](https://github.com/openai/openai-python).
Full list of Python requirements is in the `requirements.txt` file, you can use it to install all of them.



## Configuration

Configuration is done through a `.env` file. You can copy example file `.env.example` as `.env` and fill required parameters.

```commandline
cp .env.example .env
```


### Telegram bot

Only required parameter is a [bot token](https://core.telegram.org/bots#creating-a-new-bot).

You can also restrict who can access the bot via `ALLOWED_USERNAMES`.
You can specify multiple usernames delimited by space.
If you don't want to restrict the bot at all you can remove this parameter or leave it empty.


### OpenAI API

There are two required parameters - [API key](https://platform.openai.com/account/api-keys) and [used model](https://platform.openai.com/docs/models/dall-e).

```dotenv
OPENAI_TOKEN='<your secret API key>'
OPENAI_MODEL='dall-e-3 or dall-e-2'
```

Through `.env` you can also configure level of logging of OpenAI API through `OPENAI_LOG` parameter.
You can set it to `debug` or `info`.
```dotenv
OPENAI_LOG='debug or info'
```



## Commands

* `/again` - generates new image for last received prompt
* `/start` or `/help` - prints a simple start message



## Running the bot

You can run the bot from the source code directly, or in a Docker container.


### From source code

1. Create a Telegram bot via [BotFather](https://core.telegram.org/bots#6-botfather)
2. Create [OpenAI API key](https://platform.openai.com/account/api-keys)
3. Install all packages from `requirements.txt`
4. Fill `.env` file
5. Run `main.py` file with Python


### Docker

1. Create a Telegram bot via [BotFather](https://core.telegram.org/bots#6-botfather)
2. Create [OpenAI API key](https://platform.openai.com/account/api-keys)
3. Fill `.env` file
4. Run `docker compose up -d --build` in terminal

Note that `.env` file is used only for loading environment variables into Docker container through compose.
The file itself isn't added to the container.



## Disclaimer

This bot is in no way affiliated, associated, authorized, endorsed by, or in any way officially connected with OpenAI.
This is an independent and unofficial project.
Use at your own risk.
