from pprint import pprint
from dotenv import load_dotenv

import requests


def requestGit():
    url = "https://api.github.com"
    return requests.get(url)


def saveList(list):
    pprint(list)


def pipeline():
    saveList(requestGit())


if __name__ == "__main__":
    pipeline()
