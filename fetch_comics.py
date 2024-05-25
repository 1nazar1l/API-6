import requests
import os
import random


def download_picture(image_link, filename):
    os.makedirs('images', exist_ok=True)
    response = requests.get(image_link)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def random_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    last_num = response.json()["num"]
    num = random.randint(1, last_num)
    return num


def make_comics():
    num = random_number()
    url = f"https://xkcd.com/{num}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    img_url = response.json()["img"]
    coment = response.json()["alt"]
    filename = "images/comics.png"
    download_picture(img_url, filename)
    return coment
