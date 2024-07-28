import os
import re
import requests


url = os.getenv('APP_URL', 'http://0.0.0.0:8080')


def test_status():
    r = requests.get(url)
    assert r.status_code == 200
    assert r.encoding == 'utf-8'


def test_metrics():
    r = requests.get(f'{url}/metrics')
    assert re.search(r'dockerhub_ratelimit_scrape_error\{.*\} 0|1', r.text)


def test_healthz():
    r = requests.get(f'{url}/healthz')
    assert r.text == 'Ok'
