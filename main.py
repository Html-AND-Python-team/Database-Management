import json
from pathlib import Path
import time as tm
import os

BASE_DIR = Path(__file__).resolve().parent

def load_db():
    with open(BASE_DIR / "database.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    with open(BASE_DIR / "database.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
    
    print("======#Added#======")

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    tm.sleep(0.5)


def add_programming_language(name, id, extensions, difficulty):

    db = load_db()

    new_language = {
        "id": id,
        "name": name,
        "extensions": extensions,
        "difficulty": difficulty
    }

    db["programming_languages"].append(new_language)

    save_db(db)

def add_operative_system(name, base, package_extensions, family):

    db = load_db()

    new_OS = {
        "base": base,
        "name": name,
        "package-extensions": package_extensions,
        "family": family,
    }

    db["operative_systems"].append(new_OS)

    save_db(db)

def main():
    choose = input("You want to add an operative_system (1), or programming language (2)\n\n >_")

    if choose == "2":

        while True:
            id = input("id: ")
            name = input("name: ")
            extensions = input("extensions: ")
            difficulty = input("difficulty: ")

            add_programming_language(id, name, extensions, difficulty)

    elif choose == "1":

        while True:
            id = input("base: ")
            name = input("name: ")
            extensions = input("package_extensions: ")
            difficulty = input("family: ")

            add_operative_system(id, name, extensions, difficulty)

main()