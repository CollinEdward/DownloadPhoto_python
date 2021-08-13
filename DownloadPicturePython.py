import requests
import random

def download_picture():
    response = requests.get(input("Type URL of photo: "))
    with open("Image" + str(random.randint(1,999)) + ".png", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    download_picture()