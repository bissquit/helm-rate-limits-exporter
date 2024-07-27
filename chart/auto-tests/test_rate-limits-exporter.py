import os
import re
import requests


url = os.getenv('APP_URL', 'http://0.0.0.0:8080')


def test_status():
    r = requests.get(url)
    assert r.status_code == 200


def test_root():
    r = requests.get(url)
    assert re.search(r'metrics', r.text)
