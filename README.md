# Комиксы для телеграмм канала

Скачивает прикольные комиксы от `xkcd`, а также отправляет их в телеграмм канал.

## Как установить



Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
Для работы кода нужно создать .env файл в котором нужно указать `TELEGRAM_TOKEN` и `CHAT_ID`. Первый токен можно получить при создании телеграмм бота.Как создать бота можно узнать на [этом](https://sendpulse.com/ru/knowledge-base/chatbot/telegram/create-telegram-chatbot) сайте.
Второй токен можно получить создав свой канал в телеграмме.
```
TELEGRAM_TOKEN=ваш токен
CHAT_ID=ваш токен
```


## Как запускать скрипты 

Для скачивания и отправки комиксов в телеграмм нужно запустить `sending_comics_to_TG.py`. Запустить файл можно через терминал:

```
python sending_comics_to_TG.py
```
## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).