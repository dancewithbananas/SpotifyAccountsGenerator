import random
import string
import time

import colorama
import names
import pyautogui
from PIL import Image
import requests
import psutil
import yaml
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
colorama.init()


def repeat():
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    with open('config.yaml') as f:
        Year = yaml.load(f, Loader=yaml.FullLoader).get("Year")
    with open('config.yaml') as f:
        ChanceMale = int(yaml.load(f, Loader=yaml.FullLoader).get("ChanceMale"))

    email = random_char(12)
    mouse = pyautogui
    file = open("Accounts.txt", "a+")

    mouse.getWindowsWithTitle("Spotify")[0].show()
    mouse.getWindowsWithTitle("Spotify")[0].maximize()
    mouse.moveTo(mouse.getWindowsWithTitle("Spotify")[0].centerx, mouse.getWindowsWithTitle("Spotify")[0].centery)
    mouse.click()
    mouse.press("TAB")
    mouse.press("TAB")
    mouse.press("TAB")
    mouse.press("TAB")
    mouse.press("TAB")
    mouse.press("TAB")
    mouse.press("ENTER")

    time.sleep(1)

    # Email
    mouse.typewrite(email)
    mouse.hotkey('altright', '2')
    mouse.typewrite("gmail.com")
    mouse.press("TAB")

    # Password
    password = random_char(10)
    mouse.typewrite(password)

    # Random name
    mouse.press("TAB")
    mouse.typewrite(names.get_first_name() + " " + names.get_last_name())
    mouse.press("TAB")
    mouse.press("ENTER")

    # Month of born date
    time.sleep(1)
    randomize = random.randint(1, 12)
    i = 0
    while i < randomize:
        mouse.press("down")
        i = i + 1

    # Day of born date
    mouse.press("TAB")
    mouse.typewrite(random.randint(1, 30).__str__())
    mouse.press("TAB")

    # Year of born date
    mouse.typewrite(random.randint(int(Year.split("-")[0]), int(Year.split("-")[1])).__str__())
    randomgender = random.randint(1, 100)
    mouse.press("TAB")

    # Male
    if 1 <= randomgender <= ChanceMale:
        mouse.press("down")
    else:
        # Female
        mouse.press("down")
        mouse.press("up")

    if randomgender != 0:
        mouse.press("TAB")
        mouse.press("TAB")
        mouse.press("TAB")
        mouse.press("ENTER")

        time.sleep(5)
        x, y = mouse.locateCenterOnScreen(Image.open(requests.get("https://i.imgur.com/rvOke0m.png", stream=True).raw))
        mouse.moveTo(x, y)
        mouse.click()
        mouse.press("TAB")
        mouse.press("TAB")
        mouse.press("ENTER")
        mouse.press("down")
        mouse.press("down")
        mouse.press("down")
        mouse.press("down")
        mouse.press("down")
        mouse.press("down")
        mouse.press("ENTER")
        file.write(email.__str__() + "@gmail.com:" + password.__str__() + '\n')
        file.close()


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


if checkIfProcessRunning("Spotify"):
    gen = 0
    bots = input("How many accounts do you want to generate?")
    while gen < int(bots):
        time.sleep(1.5)
        repeat()
        gen = gen + 1
    else:
        print(f"{colorama.Fore.GREEN}" + bots + " Generated!")
else:
    input(f"{colorama.Fore.RED}" + "Error: Did not find Spotify process, please open the Spotify client!")
