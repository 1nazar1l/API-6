import os
from dotenv import load_dotenv
from telegram import Bot
from fetch_comics import get_comic


def main():
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    coment = get_comic()
    bot_token = os.environ["TELEGRAM_TOKEN"]
    bot = Bot(token=bot_token)
    chat_id = os.environ["CHAT_ID"]
    bot.send_message(chat_id, coment)
    try:
        with open(os.path.join("images", "comic.png"), "rb") as images:
            bot.send_document(chat_id, document=images)
    finally:
        os.remove(os.path.join("images", "comic.png"))
    


if __name__ == '__main__':
    main()