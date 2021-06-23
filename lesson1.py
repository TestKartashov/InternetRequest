from pprint import pprint
from dotenv import load_dotenv
from github import Github
import json
import requests

##1. Посмотреть документацию к API GitHub,
# разобраться как вывести список репозиториев
# для конкретного пользователя, сохранить
# JSON-вывод в файле *.json.

def print_repo(repo):
    return repo.full_name

def requestGit(username):
    g = Github()
    user = g.get_user(username)
    lt = []
    for repo in user.get_repos():
        lt.append(print_repo(repo))
    return lt


def saveList(lt):
    with open('data.json', 'w') as fp:
        json.dump(lt, fp, indent=2)


def pipeline(name):
    saveList(requestGit(name))


if __name__ == "__main__":
    pipeline("TestKartashov")
