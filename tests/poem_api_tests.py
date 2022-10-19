import pytest
from poem_api import get_poems_json


def test_get_poems():
    assert len(get_poems_json()) == 3162
    assert len(get_poems_json("whitman")) == 67
    assert len(get_poems_json(author="seeger")) == 6


