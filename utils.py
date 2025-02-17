import json

def load_banned_words():
    try:
        with open("database/banned_words.json", "r") as file:
            data = json.load(file)
            return set(data.get("banned_words", []))
    except FileNotFoundError:
        return set()
