import json


def find_personal_score(name: str) -> int:
    with open("highscores.json", "r") as scores:
        highscores = json.load(scores)["highscores"]
    for username, score in highscores:
        if username == name:
            return score
    return 0
