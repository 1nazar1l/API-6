import requests
import random
import os


def download_picture(image_link, file_path):
    response = requests.get(image_link)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)

def make_random_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    last_num = response.json()["num"]
    num = random.randint(1, last_num)
    return num


def get_comic():
    num = make_random_number()
    url = f"https://xkcd.com/{num}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()

    comics_info = response.json()
    img_url = comics_info["img"]
    coment = comics_info["alt"]

    file_path = os.path.join("images", "comic.png")
    download_picture(img_url, file_path)
    
    return coment

