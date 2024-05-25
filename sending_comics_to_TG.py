import os
from dotenv import load_dotenv
from telegram import Bot
from fetch_comics import make_comics


def main():
    load_dotenv()
    coment = make_comics()
    bot_token = os.environ["TELEGRAM_TOKEN"]
    bot = Bot(token=bot_token)
    chat_id = os.environ["CHAT_ID"]
    bot.send_message(chat_id, coment)
    with open("images/comics.png", "rb") as images:
        bot.send_document(chat_id, document=images)


if __name__ == '__main__':
    main()