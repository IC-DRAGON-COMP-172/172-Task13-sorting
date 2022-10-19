import pytest
from poetry_collection import PoetryCollection


def example_poem_data():
    test_list = []
    test_list.append({"title": "poem1", "author": "author1", "lines": ["line1", "line2"]})
    test_list.append({"title": "poem2", "author": "author1", "lines": ["line1", "line2", "line3"]})
    test_list.append({"title": "poem3", "author": "author2", "lines": ["line1", "line2"]})
    test_list.append({"title": "poem4", "author": "author3", "lines": []})
    test_list.append({"title": "poem5", "author": "author2", "lines": ["line1 is a really long line comparatively", "line2 is also a bit long"]})
    test_list.append({"title": "poem6", "author": "author3", "lines": ["many", "short", "lines", "here"]})
    test_list.append({"title": "poem7", "author": "author2", "lines": ["line1", "line2"]})
    return test_list


def test_creating_collection():
    my_poetry_collection = PoetryCollection(example_poem_data())
    print(my_poetry_collection)


def test_sort_by_poem_length():
    pass


def test_sort_by_title():
    pass


def test_sort_by_title_length():
    pass


