import requests


def get_poems_json(author=None):
    if author is None:
        response = requests.get("https://poetrydb.org/poemcount/3162")
    else:
        response = requests.get("https://poetrydb.org/author/" + author)
    return response.json()

