import requests
from poem import Poem
from poem_api import get_poems_json


class PoetryCollection:
    def __init__(self, poem_json_list):
        self.poem_list = []
        for poem_json in poem_json_list:
            self.poem_list.append(Poem(poem_json))

    def __str__(self):
        return self.poem_list.__str__()

    def sort_by_poem_length(self):
        """:post: poem list is ordered by number of characters in poems, least to greatest"""
        pass

    def sort_by_title(self):
        """:post: poem list is ordered alphabetically by title"""
        pass

    def sort_by_title_length(self):
        """:post: poem list is ordered by number of characters in the title of the poems, greatest to least"""
        pass


def real_sorts_in_action():
    """use get_poems_json from poem_api to fetch some real data, run and print results of each sort to show it working"""
    pass


def main():
    real_sorts_in_action()


if __name__ == "__main__":
    main()
